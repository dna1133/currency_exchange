from dataclasses import dataclass
from decimal import Decimal, getcontext

from currency_exchange.core.configs import settings

from currency_exchange.domain.entity.base import BaseEntity
from currency_exchange.domain.entity.exceptions import ApplicationError


@dataclass
class ExchangeRate(BaseEntity):
    exchange_from: str
    exchange_to: str
    _rate: Decimal | None = None

    getcontext().prec = 6

    @property
    def rate(self) -> Decimal:
        return self._rate

    @rate.setter
    def rate(self, rate) -> Decimal:
        self._rate = rate


class ExchangePair:
    def __init__(self, codes: str) -> None:
        if len(codes) != (settings.EXCHANGE_RATE_LEN * 2):
            raise ApplicationError("Wrong echange pair!")
        self.exchange_from = codes[: settings.EXCHANGE_RATE_LEN]
        self.exchange_to = codes[settings.EXCHANGE_RATE_LEN :]
