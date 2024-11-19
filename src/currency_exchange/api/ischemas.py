from typing import Optional
from pydantic import BaseModel


class ExchangePairArgs:
    def __init__(self, exchange_from: str, exchange_to: str, amount: int | None = None):
        self.exchange_from = exchange_from
        self.exchange_to = exchange_to
        self.amount = amount if amount else 1


class ErrorSchema(BaseModel):
    detail: str
