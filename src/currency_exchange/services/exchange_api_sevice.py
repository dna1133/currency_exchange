from decimal import Decimal
from fastapi import HTTPException
from fastapi import status
from sqlalchemy import and_, insert, select

from currency_exchange.domain.entity.exchange import ExchangeRate, ExchangePair
from currency_exchange.gateways.database.models.exchange_rates import ExchangeRates
from currency_exchange.services.base_api_service import BaseService


class ExchangeService(BaseService):
    _model = ExchangeRates

    @classmethod
    async def get_exchange_rate(cls, exchange_rate: str):
        exchange_pair = ExchangePair(exchange_rate)
        query = select(cls._model).where(
            and_(
                cls._model.base_currency_oid == exchange_pair.exchange_from,
                cls._model.target_currency_oid == exchange_pair.exchange_to,
            )
        )
        async with cls.db.get_read_only_session() as session:
            res = await session.execute(query)
            return res.scalars().all()

    @classmethod
    async def add_exchange_rate(
        cls,
        base_currency_oid: str,
        target_currency_oid: str,
        rate: Decimal,
    ):
        pass
