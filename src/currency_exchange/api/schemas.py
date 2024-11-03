from decimal import Decimal
from pydantic import UUID4, BaseModel

from currency_exchange.domain.entity.currency import Currency
from currency_exchange.domain.entity.exchange import Exchange


class CurrensySchema(BaseModel):
    name: str
    code: str
    sign: str
    oid: str

    @classmethod
    def from_entity(cls, currency: Currency) -> "CurrensySchema":
        return cls(
            oid=currency.oid,
            name=currency.name,
            code=currency.code,
            sign=currency.sign,
        )


class ExchangeSchema(BaseModel):
    oid: str
    rate: Decimal

    @classmethod
    def from_entity(cls, exchange: Exchange) -> "ExchangeSchema":
        return cls(
            oid=exchange.oid,
            name=exchange.rate,
        )


class ExchangePairArgs:
    def __init__(self, exchange_from: str, exchange_to: str):
        self.exchange_from = exchange_from
        self.exchange_to = exchange_to
