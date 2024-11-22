from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class ExchangePairArgs:
    def __init__(
        self, exchange_from: str, exchange_to: str, amount: Decimal | None = None
    ):
        self.exchange_from = exchange_from
        self.exchange_to = exchange_to
        self.amount = amount if amount else 1


class ErrorSchema(BaseModel):
    detail: str


async def exchange_params(
    exchange_from: str,
    exchange_to: str,
    amount: Decimal,
):
    return {
        "exchange_from": exchange_from,
        "exchange_to": exchange_to,
        "amount": amount,
    }
