from fastapi import APIRouter, Request, Depends
from sqlalchemy import select
from starlette.responses import PlainTextResponse

from fastapi_cache.decorator import cache

from currency_exchange.api.schemas import CurrensySchema

from currency_exchange.gateways.database.postgresql.database import assync_session_maker
from currency_exchange.gateways.database.models.currencies import Currencies

router = APIRouter(
    prefix="",
    tags=["currency"],
)


@router.get("/currencies")
@cache(expire=30)
async def get_all_currencies():
    async with assync_session_maker() as session:
        query = select(Currencies)
        res = await session.execute(query)
        return res.scalars().all()


@router.get("/currency/{currency}", response_model=CurrensySchema)
@cache(expire=30)
async def get_currency_by_code(request: Request): ...


@router.post("/currencies")
@cache(expire=30)
async def post_currensies(reqyest: Request): ...
