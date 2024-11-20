import logging
from fastapi import APIRouter, Request, Depends, status
from sqlalchemy import select

from fastapi_cache.decorator import cache

from currency_exchange.core.conteiner import get_conteiner
from currency_exchange.gateways.database.models.currencies import Currencies
from currency_exchange.gateways.database.postgresql.database import BaseDB, Database
from currency_exchange.api.responses.currency_responses import (
    get_currencies_responce,
    get_currency_responce,
    post_currency_responce,
)

router = APIRouter(
    prefix="/currensies",
    tags=["currensies"],
)

log = logging.getLogger(__name__)


@router.get("/", responses=get_currencies_responce)
@cache(expire=10)
async def get_all_currencies(
    conteiner=Depends(get_conteiner),
):
    db: BaseDB = conteiner.resolve(BaseDB)
    query = select(Currencies)
    async with db.get_session() as session:
        res = await session.execute(query)
        return res.scalars().all()


@router.get("/{currency}", responses=get_currency_responce)
@cache(expire=30)
async def get_currency_by_code(request: Request): ...


@router.post("/", responses=post_currency_responce)
@cache(expire=30)
async def post_currensies(reqyest: Request): ...


# @router.get("/test")
# async def get_test():
#     return {"status": "test success"}
