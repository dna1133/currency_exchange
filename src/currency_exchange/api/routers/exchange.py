from fastapi import APIRouter, Depends, Request, status
from fastapi_cache.decorator import cache

from currency_exchange.api.schemas import ExchangePairArgs, ExchangeSchema


router = APIRouter(
    prefix="",
    tags=["exchangeRate"],
)


@router.get("/exchangeRates", response_model=list[ExchangeSchema])
@cache(expire=30)
async def get_all_exchange_rates(request: Request):
    return await {}


@router.get("/exchangeRate/{exchange_rate}", response_model=ExchangeSchema)
@cache(expire=30)
async def get_exchange_rate(request: Request):
    return await {}


@router.post("/exchangeRate")
@cache(expire=30)
async def post_exchange_rate(request: Request):
    return await {}


@router.patch("/exchangeRate")
@cache(expire=30)
async def patch_exchange_rate(request: Request):
    return await {}


@router.get(
    "/exchange",
    responses={
        status.HTTP_200_OK: {"model": ""},
        status.HTTP_400_BAD_REQUEST: {"model": ""},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ""},
    },
)
@cache(expire=30)
async def get_exchange_pair(exch: ExchangePairArgs = Depends()):
    return {"exchange_from": exch.exchange_from, "exchange_to": exch.exchange_to}
