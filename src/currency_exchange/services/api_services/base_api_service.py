from fastapi import HTTPException, status
from sqlalchemy import select
from currency_exchange.core.conteiner import get_conteiner
from currency_exchange.gateways.database.postgresql.database import BaseDB


class BaseService:
    conteiner = get_conteiner()
    db: BaseDB = conteiner.resolve(BaseDB)
    _model = None
    session_dict = {"r": db.get_read_only_session, "rw": db.get_session}

    @classmethod
    async def find_one(cls, **filter_by):
        query = select(cls._model).filter_by(**filter_by)
        resalt = await cls._transaction_one(query)
        return resalt

    @classmethod
    async def find_many(cls, **filter_by):
        query = select(cls._model).filter_by(**filter_by)
        resalt = await cls._transaction_many(query)
        return resalt

    @classmethod
    async def get_all(cls):
        query = select(cls._model)
        resalt = await cls._transaction_many(query)
        return resalt

    @classmethod
    async def _transaction_one(
        cls, query, mode: str = "r", patch_data: dict | None = None
    ):
        async with cls.session_dict[mode]() as session:
            _result = await session.execute(query)
            result = _result.scalars().one_or_none()
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
            if mode == "rw":
                if patch_data:
                    for key, value in patch_data.items():
                        if key == "oid":
                            continue
                        else:
                            setattr(result, key, value)
                await session.commit()
            return result

    @classmethod
    async def _transaction_many(
        cls, query, mode: str = "r", patch_data: dict | None = None
    ):
        async with cls.session_dict[mode]() as session:
            _result = await session.execute(query)
            result = _result.scalars().all()
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                )
            if mode == "rw":
                if patch_data:
                    for key, value in patch_data.items():
                        if key == "oid":
                            continue
                        else:
                            setattr(result, key, value)
                await session.commit()
            return result
