from abc import ABC
from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class BaseCurrency(ABC):
    name: str
    code: str
    sign: str
    oid: str = field(default_factory=uuid4())


@dataclass
class Currency(BaseCurrency): ...
