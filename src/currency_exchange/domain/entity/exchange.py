from dataclasses import dataclass, field
from decimal import Decimal, getcontext
from uuid import uuid4


@dataclass
class Exchange:
    _rate: Decimal
    oid: str = field(default_factory=uuid4)
    getcontext().prec = 6

    @property
    def rate(self) -> Decimal:
        return self._rate

    @rate.setter
    def rate(self, base_curr: Decimal, target_curr: Decimal) -> Decimal:
        self._rate = base_curr / target_curr
