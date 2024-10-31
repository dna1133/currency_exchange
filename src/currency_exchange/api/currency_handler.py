from fastapi import APIRouter, Request
from starlette.responses import PlainTextResponse

from currency_exchange.api.schemas import CurrensySchema


currency_router = APIRouter(
    prefix="",
    tags=["currency"],
)


@currency_router.get("/currencies", response_model=list[CurrensySchema])
async def get_all_exchange_rates():
    return await {}


@currency_router.get("/currency/{currency}", response_model=CurrensySchema)
async def get_currency_by_code(request: Request):
    return await {}


@currency_router.post("/currencies")
async def post_currensies(reqyest: Request):
    return await {}
