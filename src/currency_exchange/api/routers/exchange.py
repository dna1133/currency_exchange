import logging
from fastapi import APIRouter, Depends, Request
from fastapi_cache.decorator import cache

from currency_exchange.api.ischemas import ExchangePairArgs
from currency_exchange.api.responses.exchange_resposes import (
    get_all_exchange_rates_responce,
    get_exchange_rate_responce,
    post_exchange_rate_responce,
    patch_exchange_rate_responce,
    get_exchange_sum_responce,
)


router = APIRouter(
    prefix="/exchange_rates",
    tags=["exchangeRates"],
)

log = logging.getLogger(__name__)


@router.get("/", responses=get_all_exchange_rates_responce)
@cache(expire=30)
async def get_all_exchange_rates(request: Request):
    return await {}


@router.get("/{exchange_rate}", responses=get_exchange_rate_responce)
@cache(expire=30)
async def get_exchange_rate(request: Request):
    return await {}


@router.post("/", responses=post_exchange_rate_responce)
@cache(expire=30)
async def post_exchange_rate(request: Request):
    return await {}


@router.patch("/", responses=patch_exchange_rate_responce)
@cache(expire=30)
async def patch_exchange_rate(request: Request):
    return await {}


@router.get("/exchange", responses=get_exchange_sum_responce)
@cache(expire=30)
async def get_exchange_sum(exch: ExchangePairArgs = Depends(), request=Request):
    return {"exchange_from": exch.exchange_from, "exchange_to": exch.exchange_to}
