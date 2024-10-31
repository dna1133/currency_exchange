from fastapi import APIRouter, Depends, Request

from currency_exchange.api.schemas import ExchangePairArgs, ExchangeSchema


exchange_router = APIRouter(
    prefix="",
    tags=["exchangeRate"],
)


@exchange_router.get("/exchangeRates", response_model=list[ExchangeSchema])
async def get_all_exchange_rates(request: Request):
    return await {}


@exchange_router.get("/exchangeRate/{exchange_rate}", response_model=ExchangeSchema)
async def get_exchange_rate(request: Request):
    return await {}


@exchange_router.post("/exchangeRate")
async def post_exchange_rate(request: Request):
    return await {}


@exchange_router.patch("/exchangeRate")
async def patch_exchange_rate(request: Request):
    return await {}


@exchange_router.get("/")
async def get_exchange_pair(exch: ExchangePairArgs = Depends()):
    return {"exchange_from": exch.exch_from, "exchange_to": exch.exch_to}
