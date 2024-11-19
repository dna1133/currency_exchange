from decimal import Decimal
from pydantic import BaseModel

from currency_exchange.api.schemas.currency_schemas import CurrencySchema


class ExchangeSchema(BaseModel):
    oid: str
    baseCurrency: CurrencySchema
    targetCurrency: CurrencySchema
    rate: Decimal


class ExchangePairAmountSchema(BaseModel):
    baseCurrency: CurrencySchema
    targetCurrency: CurrencySchema
    rate: Decimal
    amount: Decimal
    convertedAmount: Decimal
