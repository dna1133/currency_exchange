from decimal import Decimal
from fastapi import HTTPException
from fastapi import status
from sqlalchemy import and_, insert, select

from currency_exchange.domain.entity.exchange import ExchangeRate, ExchangePair
from currency_exchange.gateways.database.models.exchange_rates import ExchangeRates
from currency_exchange.services.base_api_service import BaseService
from currency_exchange.services.currency_api_service import CurrencyService


class ExchangeService(BaseService):
    _model = ExchangeRates
    currency_service = CurrencyService

    @classmethod
    async def get_exchange_rate(cls, exchange_pair_raw: str):
        exchange_pair = ExchangePair(exchange_pair_raw)

        base_currency = await cls.currency_service.get_by_code(
            exchange_pair.exchange_from
        )
        target_currency = await cls.currency_service.get_by_code(
            exchange_pair.exchange_to
        )
        if not base_currency or not target_currency:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Can't find currency"
            )
        query = select(cls._model).where(
            and_(
                cls._model.base_currency_oid == base_currency.oid,
                cls._model.target_currency_oid == target_currency.oid,
            )
        )
        async with cls.db.get_read_only_session() as session:
            exchange_rate = await session.execute(query)
        exchange_rate_result = exchange_rate.scalars().one_or_none()
        if not exchange_rate_result:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Can't find currency"
            )
        return {
            "id": exchange_rate_result.oid,
            "base_currency": base_currency,
            "target_currency": target_currency,
            "rate": exchange_rate_result.rate,
        }

    @classmethod
    async def get_all_exchange_rates(cls):
        res = []
        query = select(cls._model)
        async with cls.db.get_read_only_session() as session:
            exchange_rates = await session.execute(query)
        exchange_rate_list = exchange_rates.scalars().all()
        for rate in exchange_rate_list:
            base_currency = await cls.currency_service.get_by_oid(
                rate.base_currency_oid
            )
            target_currency = await cls.currency_service.get_by_oid(
                rate.target_currency_oid
            )
            res.append(
                {
                    "id": rate.oid,
                    "base_currency": base_currency,
                    "target_currency": target_currency,
                    "rate": rate.rate,
                }
            )
        return res

    @classmethod
    async def add_exchange_rate(
        cls,
        base_currency_code: str,
        target_currency_code: str,
        rate: Decimal,
    ):
        ex_rates_dict = cls._check_pair(
            code_base=base_currency_code, code_target=target_currency_code
        )
        # base_currency = await cls.currency_service.get_by_code(base_currency_code)
        # target_currency = await cls.currency_service.get_by_code(target_currency_code)
        # # bc = base_currency.scalars().all()
        # # dc = target_currency.scalars().all()
        # if not base_currency or not target_currency:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST, detail="Can't find currency"
        #     )
        base_currency = ex_rates_dict["base"]
        target_currency = ex_rates_dict["target"]
        exchange_rate = ExchangeRate(
            exchange_from=base_currency.oid,
            exchange_to=target_currency.oid,
        )
        query_add = (
            insert(cls._model)
            .values(
                oid=exchange_rate.oid,
                base_currency_oid=exchange_rate.exchange_from,
                target_currency_oid=exchange_rate.exchange_to,
                rate=rate,
            )
            .returning(cls._model)
        )
        async with cls.db.get_session() as session:
            new_exchange_rate = await session.execute(query_add)
            await session.commit()
            return new_exchange_rate.scalars().one_or_none()

    @classmethod
    async def patch_exchange_rate(cls, rate: Decimal): ...

    @classmethod
    async def _check_pair(
        cls,
        oid_base: str | None = None,
        oid_target: str | None = None,
        code_base: str | None = None,
        code_target: str | None = None,
    ):
        if code_base and code_target:
            base_currency = await cls.currency_service.get_by_code(code_base)
            target_currency = await cls.currency_service.get_by_code(code_target)
        elif oid_base and oid_target:
            base_currency = await cls.currency_service.get_by_oid(oid_base)
            target_currency = await cls.currency_service.get_by_oid(oid_target)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong currency"
            )
        if not base_currency or not target_currency:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Can't find currency"
            )
        return {"base": base_currency, "target": target_currency}
