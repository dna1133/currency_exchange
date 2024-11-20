from abc import ABC
from dataclasses import dataclass

from currency_exchange.domain.entity.base import BaseEntity


@dataclass
class BaseCurrency(BaseEntity):
    name: str
    code: str
    sign: str


@dataclass
class Currency(BaseCurrency): ...
