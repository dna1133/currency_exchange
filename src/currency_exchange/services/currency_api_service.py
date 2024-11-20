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
        async with cls.db.get_read_only_session() as session:
            raw_currency = await session.execute(query)

        if raw_currency.scalars().all():
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
        async with cls.db.get_session() as session:
            new_currensy = await session.execute(query_add)
            await session.commit()
            return new_currensy.scalars().all()
