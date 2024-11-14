from typing import ClassVar, Iterable, Iterator, overload

FAITHFUL: ConcatStrategy
SPACE: ConcatStrategy
__version__: str


class AnnotatedText:
    def __init__(self) -> None:
        """__init__(self: _bergamot.AnnotatedText) -> None"""

    def numSentences(self) -> int:
        """numSentences(self: _bergamot.AnnotatedText) -> int"""

    def numWords(self, arg0: int) -> int:
        """numWords(self: _bergamot.AnnotatedText, arg0: int) -> int"""

    def sentence(self, arg0: int) -> str:
        """sentence(self: _bergamot.AnnotatedText, arg0: int) -> str"""

    def sentenceAsByteRange(self, arg0: int) -> ByteRange:
        """sentenceAsByteRange(self: _bergamot.AnnotatedText, arg0: int) -> _bergamot.ByteRange"""

    def word(self, arg0: int, arg1: int) -> str:
        """word(self: _bergamot.AnnotatedText, arg0: int, arg1: int) -> str"""

    def wordAsByteRange(self, arg0: int, arg1: int) -> ByteRange:
        """wordAsByteRange(self: _bergamot.AnnotatedText, arg0: int, arg1: int) -> _bergamot.ByteRange"""

    @property
    def text(self) -> str: ...


class ByteRange:
    def __init__(self) -> None:
        """__init__(self: _bergamot.ByteRange) -> None"""

    @property
    def begin(self) -> int: ...

    @property
    def end(self) -> int: ...


class ConcatStrategy:
    __members__: ClassVar[dict] = ...  # read-only
    FAITHFUL: ClassVar[ConcatStrategy] = ...
    SPACE: ClassVar[ConcatStrategy] = ...
    __entries: ClassVar[dict] = ...

    def __init__(self, value: int) -> None:
        """__init__(self: _bergamot.ConcatStrategy, value: int) -> None"""

    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""

    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""

    def __index__(self) -> int:
        """__index__(self: _bergamot.ConcatStrategy) -> int"""

    def __int__(self) -> int:
        """__int__(self: _bergamot.ConcatStrategy) -> int"""

    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""

    @property
    def name(self) -> str: ...

    @property
    def value(self) -> int: ...


class Response:
    def __init__(self) -> None:
        """__init__(self: _bergamot.Response) -> None"""

    @property
    def alignments(self): ...

    @property
    def source(self) -> AnnotatedText: ...

    @property
    def target(self) -> AnnotatedText: ...


class ResponseOptions:
    HTML: bool
    alignment: bool
    concatStrategy: ConcatStrategy
    qualityScores: bool
    sentenceMappings: bool

    def __init__(self, qualityScores: bool = ..., alignment: bool = ...
                 , HTML: bool = ..., sentenceMappings: bool = ...,
                 concatStrategy: ConcatStrategy = ...) -> None:
        """__init__(self: _bergamot.ResponseOptions, qualityScores: bool = True, alignment: bool = False, HTML: bool = False, sentenceMappings: bool = True, concatStrategy: _bergamot.ConcatStrategy = <ConcatStrategy.FAITHFUL: 0>) -> None"""


class Service:
    def __init__(self, arg0: ServiceConfig) -> None:
        """__init__(self: _bergamot.Service, arg0: marian::bergamot::AsyncService::Config) -> None"""

    def modelFromConfig(self, *args, **kwargs)->TranslationModel:
        """modelFromConfig(self: _bergamot.Service, arg0: str) -> marian::bergamot::TranslationModel"""

    def modelFromConfigPath(self, *args, **kwargs)->TranslationModel:
        """modelFromConfigPath(self: _bergamot.Service, arg0: str) -> marian::bergamot::TranslationModel"""

    def pivot(self, arg0: TranslationModel, arg1: TranslationModel, arg2: VectorString,
              arg3: ResponseOptions) -> VectorResponse:
        """pivot(self: _bergamot.Service, arg0: marian::bergamot::TranslationModel, arg1: marian::bergamot::TranslationModel, arg2: _bergamot.VectorString, arg3: _bergamot.ResponseOptions) -> _bergamot.VectorResponse"""

    def translate(self, arg0: TranslationModel, arg1: VectorString, arg2: ResponseOptions) -> VectorResponse:
        """translate(self: _bergamot.Service, arg0: marian::bergamot::TranslationModel, arg1: _bergamot.VectorString, arg2: _bergamot.ResponseOptions) -> _bergamot.VectorResponse"""


class ServiceConfig:
    cacheSize: int
    numWorkers: int

    def __init__(self, numWorkers: int = ..., cacheSize: int = ..., logLevel: str = ...) -> None:
        """__init__(self: _bergamot.ServiceConfig, numWorkers: int = 1, cacheSize: int = 0, logLevel: str = 'off') -> None"""


class TranslationModel:
    def __init__(self, *args, **kwargs) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""


class VectorResponse:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _bergamot.VectorResponse) -> None

        2. __init__(self: _bergamot.VectorResponse, arg0: _bergamot.VectorResponse) -> None

        Copy constructor

        3. __init__(self: _bergamot.VectorResponse, arg0: Iterable) -> None
        """

    @overload
    def __init__(self, arg0: VectorResponse) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _bergamot.VectorResponse) -> None

        2. __init__(self: _bergamot.VectorResponse, arg0: _bergamot.VectorResponse) -> None

        Copy constructor

        3. __init__(self: _bergamot.VectorResponse, arg0: Iterable) -> None
        """

    @overload
    def __init__(self, arg0: Iterable) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _bergamot.VectorResponse) -> None

        2. __init__(self: _bergamot.VectorResponse, arg0: _bergamot.VectorResponse) -> None

        Copy constructor

        3. __init__(self: _bergamot.VectorResponse, arg0: Iterable) -> None
        """

    def append(self, x: Response) -> None:
        """append(self: _bergamot.VectorResponse, x: _bergamot.Response) -> None

        Add an item to the end of the list
        """

    def clear(self) -> None:
        """clear(self: _bergamot.VectorResponse) -> None

        Clear the contents
        """

    @overload
    def extend(self, L: VectorResponse) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _bergamot.VectorResponse, L: _bergamot.VectorResponse) -> None

        Extend the list by appending all the items in the given list

        2. extend(self: _bergamot.VectorResponse, L: Iterable) -> None

        Extend the list by appending all the items in the given list
        """

    @overload
    def extend(self, L: Iterable) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _bergamot.VectorResponse, L: _bergamot.VectorResponse) -> None

        Extend the list by appending all the items in the given list

        2. extend(self: _bergamot.VectorResponse, L: Iterable) -> None

        Extend the list by appending all the items in the given list
        """

    def insert(self, i: int, x: Response) -> None:
        """insert(self: _bergamot.VectorResponse, i: int, x: _bergamot.Response) -> None

        Insert an item at a given position.
        """

    @overload
    def pop(self) -> Response:
        """pop(*args, **kwargs)
        Overloaded function.

        1. pop(self: _bergamot.VectorResponse) -> _bergamot.Response

        Remove and return the last item

        2. pop(self: _bergamot.VectorResponse, i: int) -> _bergamot.Response

        Remove and return the item at index ``i``
        """

    @overload
    def pop(self, i: int) -> Response:
        """pop(*args, **kwargs)
        Overloaded function.

        1. pop(self: _bergamot.VectorResponse) -> _bergamot.Response

        Remove and return the last item

        2. pop(self: _bergamot.VectorResponse, i: int) -> _bergamot.Response

        Remove and return the item at index ``i``
        """

    def __bool__(self) -> bool:
        """__bool__(self: _bergamot.VectorResponse) -> bool

        Check whether the list is nonempty
        """

    @overload
    def __delitem__(self, arg0: int) -> None:
        """__delitem__(*args, **kwargs)
        Overloaded function.

        1. __delitem__(self: _bergamot.VectorResponse, arg0: int) -> None

        Delete the list elements at index ``i``

        2. __delitem__(self: _bergamot.VectorResponse, arg0: slice) -> None

        Delete list elements using a slice object
        """

    @overload
    def __delitem__(self, arg0: slice) -> None:
        """__delitem__(*args, **kwargs)
        Overloaded function.

        1. __delitem__(self: _bergamot.VectorResponse, arg0: int) -> None

        Delete the list elements at index ``i``

        2. __delitem__(self: _bergamot.VectorResponse, arg0: slice) -> None

        Delete list elements using a slice object
        """

    @overload
    def __getitem__(self, s: slice) -> VectorResponse:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _bergamot.VectorResponse, s: slice) -> _bergamot.VectorResponse

        Retrieve list elements using a slice object

        2. __getitem__(self: _bergamot.VectorResponse, arg0: int) -> _bergamot.Response
        """

    @overload
    def __getitem__(self, arg0: int) -> Response:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _bergamot.VectorResponse, s: slice) -> _bergamot.VectorResponse

        Retrieve list elements using a slice object

        2. __getitem__(self: _bergamot.VectorResponse, arg0: int) -> _bergamot.Response
        """

    def __iter__(self) -> Iterator[Response]:
        """__iter__(self: _bergamot.VectorResponse) -> Iterator[_bergamot.Response]"""

    def __len__(self) -> int:
        """__len__(self: _bergamot.VectorResponse) -> int"""

    @overload
    def __setitem__(self, arg0: int, arg1: Response) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _bergamot.VectorResponse, arg0: int, arg1: _bergamot.Response) -> None

        2. __setitem__(self: _bergamot.VectorResponse, arg0: slice, arg1: _bergamot.VectorResponse) -> None

        Assign list elements using a slice object
        """

    @overload
    def __setitem__(self, arg0: slice, arg1: VectorResponse) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _bergamot.VectorResponse, arg0: int, arg1: _bergamot.Response) -> None

        2. __setitem__(self: _bergamot.VectorResponse, arg0: slice, arg1: _bergamot.VectorResponse) -> None

        Assign list elements using a slice object
        """


class VectorString:
    @overload
    def __init__(self) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _bergamot.VectorString) -> None

        2. __init__(self: _bergamot.VectorString, arg0: _bergamot.VectorString) -> None

        Copy constructor

        3. __init__(self: _bergamot.VectorString, arg0: Iterable) -> None
        """

    @overload
    def __init__(self, arg0: VectorString) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _bergamot.VectorString) -> None

        2. __init__(self: _bergamot.VectorString, arg0: _bergamot.VectorString) -> None

        Copy constructor

        3. __init__(self: _bergamot.VectorString, arg0: Iterable) -> None
        """

    @overload
    def __init__(self, arg0: Iterable) -> None:
        """__init__(*args, **kwargs)
        Overloaded function.

        1. __init__(self: _bergamot.VectorString) -> None

        2. __init__(self: _bergamot.VectorString, arg0: _bergamot.VectorString) -> None

        Copy constructor

        3. __init__(self: _bergamot.VectorString, arg0: Iterable) -> None
        """

    def append(self, x: str) -> None:
        """append(self: _bergamot.VectorString, x: str) -> None

        Add an item to the end of the list
        """

    def clear(self) -> None:
        """clear(self: _bergamot.VectorString) -> None

        Clear the contents
        """

    def count(self, x: str) -> int:
        """count(self: _bergamot.VectorString, x: str) -> int

        Return the number of times ``x`` appears in the list
        """

    @overload
    def extend(self, L: VectorString) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _bergamot.VectorString, L: _bergamot.VectorString) -> None

        Extend the list by appending all the items in the given list

        2. extend(self: _bergamot.VectorString, L: Iterable) -> None

        Extend the list by appending all the items in the given list
        """

    @overload
    def extend(self, L: Iterable) -> None:
        """extend(*args, **kwargs)
        Overloaded function.

        1. extend(self: _bergamot.VectorString, L: _bergamot.VectorString) -> None

        Extend the list by appending all the items in the given list

        2. extend(self: _bergamot.VectorString, L: Iterable) -> None

        Extend the list by appending all the items in the given list
        """

    def insert(self, i: int, x: str) -> None:
        """insert(self: _bergamot.VectorString, i: int, x: str) -> None

        Insert an item at a given position.
        """

    @overload
    def pop(self) -> str:
        """pop(*args, **kwargs)
        Overloaded function.

        1. pop(self: _bergamot.VectorString) -> str

        Remove and return the last item

        2. pop(self: _bergamot.VectorString, i: int) -> str

        Remove and return the item at index ``i``
        """

    @overload
    def pop(self, i: int) -> str:
        """pop(*args, **kwargs)
        Overloaded function.

        1. pop(self: _bergamot.VectorString) -> str

        Remove and return the last item

        2. pop(self: _bergamot.VectorString, i: int) -> str

        Remove and return the item at index ``i``
        """

    def remove(self, x: str) -> None:
        """remove(self: _bergamot.VectorString, x: str) -> None

        Remove the first item from the list whose value is x. It is an error if there is no such item.
        """

    def __bool__(self) -> bool:
        """__bool__(self: _bergamot.VectorString) -> bool

        Check whether the list is nonempty
        """

    def __contains__(self, x: str) -> bool:
        """__contains__(self: _bergamot.VectorString, x: str) -> bool

        Return true the container contains ``x``
        """

    @overload
    def __delitem__(self, arg0: int) -> None:
        """__delitem__(*args, **kwargs)
        Overloaded function.

        1. __delitem__(self: _bergamot.VectorString, arg0: int) -> None

        Delete the list elements at index ``i``

        2. __delitem__(self: _bergamot.VectorString, arg0: slice) -> None

        Delete list elements using a slice object
        """

    @overload
    def __delitem__(self, arg0: slice) -> None:
        """__delitem__(*args, **kwargs)
        Overloaded function.

        1. __delitem__(self: _bergamot.VectorString, arg0: int) -> None

        Delete the list elements at index ``i``

        2. __delitem__(self: _bergamot.VectorString, arg0: slice) -> None

        Delete list elements using a slice object
        """

    def __eq__(self, arg0: VectorString) -> bool:
        """__eq__(self: _bergamot.VectorString, arg0: _bergamot.VectorString) -> bool"""

    @overload
    def __getitem__(self, s: slice) -> VectorString:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _bergamot.VectorString, s: slice) -> _bergamot.VectorString

        Retrieve list elements using a slice object

        2. __getitem__(self: _bergamot.VectorString, arg0: int) -> str
        """

    @overload
    def __getitem__(self, arg0: int) -> str:
        """__getitem__(*args, **kwargs)
        Overloaded function.

        1. __getitem__(self: _bergamot.VectorString, s: slice) -> _bergamot.VectorString

        Retrieve list elements using a slice object

        2. __getitem__(self: _bergamot.VectorString, arg0: int) -> str
        """

    def __iter__(self) -> Iterator[str]:
        """__iter__(self: _bergamot.VectorString) -> Iterator[str]"""

    def __len__(self) -> int:
        """__len__(self: _bergamot.VectorString) -> int"""

    def __ne__(self, arg0: VectorString) -> bool:
        """__ne__(self: _bergamot.VectorString, arg0: _bergamot.VectorString) -> bool"""

    @overload
    def __setitem__(self, arg0: int, arg1: str) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _bergamot.VectorString, arg0: int, arg1: str) -> None

        2. __setitem__(self: _bergamot.VectorString, arg0: slice, arg1: _bergamot.VectorString) -> None

        Assign list elements using a slice object
        """

    @overload
    def __setitem__(self, arg0: slice, arg1: VectorString) -> None:
        """__setitem__(*args, **kwargs)
        Overloaded function.

        1. __setitem__(self: _bergamot.VectorString, arg0: int, arg1: str) -> None

        2. __setitem__(self: _bergamot.VectorString, arg0: slice, arg1: _bergamot.VectorString) -> None

        Assign list elements using a slice object
        """
