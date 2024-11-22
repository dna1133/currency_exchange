from decimal import Decimal
from fastapi import HTTPException
from fastapi import status
from sqlalchemy import and_, insert, select

from currency_exchange.domain.entity.exceptions import ApplicationError
from currency_exchange.domain.entity.exchange import ExchangeRate, ExchangePair
from currency_exchange.gateways.database.models.exchange_rates import ExchangeRates
from currency_exchange.services.base_api_service import BaseService
from currency_exchange.services.currency_api_service import CurrencyService


class ExchangeService(BaseService):
    _model = ExchangeRates
    currency_service = CurrencyService

    @classmethod
    async def get_exchange_rate(cls, exchange_pair_raw: str):
        try:
            exchange_pair = ExchangePair(exchange_pair_raw.upper())
        except ApplicationError as e:
            raise HTTPException(status_code=400, detail=e.message)
        ex_rates_dict = cls._check_pair(
            code_base=exchange_pair.exchange_from, code_target=exchange_pair.exchange_to
        )
        base_currency = ex_rates_dict["base"]
        target_currency = ex_rates_dict["target"]
        query = select(cls._model).where(
            and_(
                cls._model.base_currency_oid == base_currency.oid,
                cls._model.target_currency_oid == target_currency.oid,
            )
        )
        exchange_rate_result = await cls._transaction_one(query)
        output = {
            "id": exchange_rate_result.oid,
            "base_currency": base_currency,
            "target_currency": target_currency,
            "rate": exchange_rate_result.rate,
        }
        return output

    @classmethod
    async def get_all_exchange_rates(cls):
        output = []
        query = select(cls._model)
        exchange_rate_list = await cls._transaction_many(query)
        for rate in exchange_rate_list:
            base_currency = await cls.currency_service.find_one(
                oid=rate.base_currency_oid
            )
            target_currency = await cls.currency_service.find_one(
                oid=rate.target_currency_oid
            )
            output.append(
                {
                    "id": rate.oid,
                    "base_currency": base_currency,
                    "target_currency": target_currency,
                    "rate": rate.rate,
                }
            )
        return output

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
        base_currency = ex_rates_dict["base"]
        target_currency = ex_rates_dict["target"]
        exchange_rate = ExchangeRate(
            exchange_from=base_currency.oid,
            exchange_to=target_currency.oid,
        )
        query = (
            insert(cls._model)
            .values(
                oid=exchange_rate.oid,
                base_currency_oid=exchange_rate.exchange_from,
                target_currency_oid=exchange_rate.exchange_to,
                rate=rate,
            )
            .returning(cls._model)
        )
        new_exchange_rate = await cls._transaction_one(query, mode="rw")
        return new_exchange_rate

    @classmethod
    async def patch_exchange_rate(cls, exchange_pair_raw: str, rate: Decimal):
        try:
            exchange_pair = ExchangePair(exchange_pair_raw.upper())
        except ApplicationError as e:
            raise HTTPException(status_code=400, detail=e.message)
        ex_rates_dict = cls._check_pair(
            code_base=exchange_pair.exchange_from, code_target=exchange_pair.exchange_to
        )
        base_currency = ex_rates_dict["base"]
        target_currency = ex_rates_dict["target"]
        query_patch = select(cls._model).where(
            and_(
                cls._model.base_currency_oid == base_currency.oid,
                cls._model.target_currency_oid == target_currency.oid,
            )
        )
        exchange_rate_result = await cls._transaction_one(
            query_patch, mode="rw", patch_data={"rate": rate}
        )
        return exchange_rate_result

    @classmethod
    async def get_exchange_sum(
        cls,
        base_currency_code: str,
        target_currency_code: str,
        amount: Decimal,
    ):
        currency_pair_dict = cls._check_pair(
            code_base=base_currency_code, code_target=target_currency_code
        )
        base_currency = currency_pair_dict["base"]
        target_currency = currency_pair_dict["target"]
        query = select(cls._model).where(
            and_(
                cls._model.base_currency_oid == base_currency.oid,
                cls._model.target_currency_oid == target_currency.oid,
            )
        )
        exchange_rate = await cls._transaction_one(query)

        converted_amount = exchange_rate.rate * amount
        output = {
            "baseCurrency": base_currency,
            "targetCurrency": target_currency,
            "rate": exchange_rate.rate,
            "amount": amount,
            "convertedAmount": converted_amount,
        }
        return output

    @classmethod
    async def _check_pair(
        cls,
        oid_base: str | None = None,
        oid_target: str | None = None,
        code_base: str | None = None,
        code_target: str | None = None,
    ):
        if code_base and code_target:
            base_currency = await cls.currency_service.find_one(code=code_base)
            target_currency = await cls.currency_service.find_one(code=code_target)
        elif oid_base and oid_target:
            base_currency = await cls.currency_service.find_one(oid=oid_base)
            target_currency = await cls.currency_service.find_one(oid=oid_target)
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong currency"
            )
        if not base_currency or not target_currency:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Can't find currency"
            )
        return {"base": base_currency, "target": target_currency}
