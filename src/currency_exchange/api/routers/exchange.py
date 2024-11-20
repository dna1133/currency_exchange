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
from currency_exchange.services.base_api_service import BaseService
from currency_exchange.services.exchange_api_sevice import ExchangeService


router = APIRouter(
    prefix="/exchange_rates",
    tags=["exchangeRates"],
)

log = logging.getLogger(__name__)


@router.get("/", responses=get_all_exchange_rates_responce)
@cache(expire=30)
async def get_all_exchange_rates(
    service: BaseService = Depends(ExchangeService),
):
    return await service.get_all()


@router.get("/{exchange_rate}", responses=get_exchange_rate_responce)
@cache(expire=30)
async def get_exchange_rate():
    return await {}


@router.post("/", responses=post_exchange_rate_responce)
@cache(expire=30)
async def post_exchange_rate():
    return await {}


@router.patch("/", responses=patch_exchange_rate_responce)
@cache(expire=30)
async def patch_exchange_rate():
    return await {}


@router.get("/exchange", responses=get_exchange_sum_responce)
@cache(expire=30)
async def get_exchange_sum(exch: ExchangePairArgs = Depends()):
    return {"exchange_from": exch.exchange_from, "exchange_to": exch.exchange_to}
