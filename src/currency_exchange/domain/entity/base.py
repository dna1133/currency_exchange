from abc import ABC
from dataclasses import asdict, dataclass, field
from uuid import uuid4


@dataclass
class BaseEntity(ABC):
    oid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)

    def to_dict(self):
        return asdict(self)
