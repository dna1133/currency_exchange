from dataclasses import dataclass
from decimal import Decimal, getcontext

from currency_exchange.domain.entity.base import BaseEntity


@dataclass
class ExchangeRate(BaseEntity):
    _rate: Decimal | None = None

    getcontext().prec = 6

    @property
    def rate(self) -> Decimal:
        return self._rate

    @rate.setter
    def rate(self, base_curr: Decimal, target_curr: Decimal) -> Decimal:
        self._rate = base_curr / target_curr
