import os
from typing import Union, Literal, Optional

from fast_langdetect import detect_multilingual, detect
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, confloat
from starlette.middleware.cors import CORSMiddleware

from config import api_key_secret

os.environ["OMP_NUM_THREADS"] = "1"

from _bergamot import ServiceConfig, Service, ResponseOptions, VectorString
from bergamot import REPOSITORY

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = Service(ServiceConfig(numWorkers=1, logLevel="info", cacheSize=100))


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class TranslateRequest(BaseModel):
    q: str | list[str]
    source: str
    target: str
    format: Literal["text", "html"]
    alternatives: Optional[int]
    api_key: str


class TranslateResponse(BaseModel):
    translatedText: list[str]


@app.post("/translate")
def translate(request: TranslateRequest):
    if request.api_key != api_key_secret:
        raise HTTPException(status_code=401, detail="invalid API key")

    sources = request.q
    source_lang = request.source
    target_lang = request.target
    if type(sources) == str:
        sources = [sources]
    options = ResponseOptions(
        alignment=False, qualityScores=False, HTML=request.format == "html"
    )

    if source_lang == "auto":
        source_lang = detect(sources[0].replace("\n", ""), low_memory=True).get("lang")

    model_id = REPOSITORY.get_model_identifier_for_translation(source_lang, target_lang)
    if model_id:
        model = service.modelFromConfigPath(REPOSITORY.modelConfigPath("browsermt", model_id))
        responses = service.translate(model, VectorString(sources), options)
    else:
        model_ids = REPOSITORY.get_model_identifiers_for_pivot_translation(source_lang, target_lang)
        if not model_ids:
            raise HTTPException(status_code=404, detail="no translation model found")
        model1 = service.modelFromConfigPath(REPOSITORY.modelConfigPath("browsermt", model_ids[0]))
        model2 = service.modelFromConfigPath(REPOSITORY.modelConfigPath("browsermt", model_ids[1]))
        responses = service.pivot(model1, model2, VectorString(sources), options)

    all_texts = [r.target.text for r in responses]
    return TranslateResponse(translatedText=all_texts)


class LanguageResponseEntry(BaseModel):
    code: str
    name: str
    targets: set[str]


@app.get("/languages")
def languages() -> list[LanguageResponseEntry]:
    from_languages = [
        LanguageResponseEntry.model_validate(v)
        for k, v in
        REPOSITORY.models_by_lang_code().items()
    ]
    return from_languages


class DetectedLanguage(BaseModel):
    confidence: confloat(le=100, ge=0)
    language: str


class DetectRequest(BaseModel):
    q: str
    api_key: str


@app.post("/detect")
def detect_language(request: DetectRequest) -> list[DetectedLanguage]:
    if request.api_key != api_key_secret:
        raise HTTPException(status_code=401, detail="invalid API key")
    all_languages = []
    result = detect_multilingual(text=request.q.replace("\n", ""), low_memory=True)
    for r in result:
        lang = DetectedLanguage(confidence=r["score"] * 100, language=r["lang"])
        all_languages.append(lang)
    return all_languages
