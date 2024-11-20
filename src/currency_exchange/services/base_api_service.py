from sqlalchemy import select
from currency_exchange.core.conteiner import get_conteiner
from currency_exchange.gateways.database.postgresql.database import BaseDB


class BaseService:
    conteiner = get_conteiner()
    db: BaseDB = conteiner.resolve(BaseDB)
    _model = None

    @classmethod
    async def get_by_code(cls, code: str):
        query = select(cls._model).where(cls._model.code == code)
        async with cls.db.get_read_only_session() as session:
            res = await session.execute(query)
            return res.scalars().one_or_none()

    @classmethod
    async def get_by_oid(cls, oid: str):
        query = select(cls._model).where(cls._model.oid == oid)
        async with cls.db.get_read_only_session() as session:
            res = await session.execute(query)
            return res.scalars().one_or_none()

    @classmethod
    async def get_all(cls):
        query = select(cls._model)
        async with cls.db.get_read_only_session() as session:
            res = await session.execute(query)
            return res.scalars().all()
