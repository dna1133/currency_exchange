from fastapi import HTTPException
from fastapi import status
from sqlalchemy import and_, insert, select

from currency_exchange.domain.entity.currency import Currency
from currency_exchange.gateways.database.models.currencies import Currencies
from currency_exchange.services.base_api_service import BaseService


class CurrencyService(BaseService):
    _model = Currencies

    @classmethod
    async def add_currency(cls, code: str, fullname: str, sign: str):
        query = select(cls._model).where(
            and_(cls._model.code == code, cls._model.fullname == fullname)
        )
        _currency = await cls._transaction_one(query)
        if _currency:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Allready exists"
            )

        currency = Currency(name=fullname, code=code, sign=sign)
        query_add = (
            insert(cls._model)
            .values(
                oid=currency.oid,
                fullname=currency.name,
                code=currency.code,
                sign=currency.sign,
            )
            .returning(cls._model)
        )
        new_currensy = await cls._transaction_one(query_add, mode="rw")
        return new_currensy
