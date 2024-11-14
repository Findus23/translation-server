from _bergamot import ResponseOptions
from bergamot import REPOSITORY

config = ServiceConfig(numWorkers=1, logLevel="off")
service = Service(config)

models = [
    service.modelFromConfigPath(
        REPOSITORY.modelConfigPath("browsermt", model)
    )
    for model in ["de-en-base"]
]

# Configure a few options which require how a Response is constructed
options = ResponseOptions(
    alignment=False, qualityScores=False, HTML=False
)
