from decimal import Decimal
import logging
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi_cache.decorator import cache

from currency_exchange.api.ischemas import ExchangePairArgs
from currency_exchange.api.responses.exchange_resposes import (
    get_all_exchange_rates_responce,
    get_exchange_rate_responce,
    post_exchange_rate_responce,
    patch_exchange_rate_responce,
    get_exchange_sum_responce,
)
from currency_exchange.domain.entity.exceptions import ApplicationError
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
    return await service.get_all_exchange_rates()


@router.get("/{exchange_rate}", responses=get_exchange_rate_responce)
@cache(expire=30)
async def get_exchange_rate(
    exchange_rate: str,
    service: BaseService = Depends(ExchangeService),
):
    return await service.get_exchange_rate(exchange_rate)


@router.post("/", responses=post_exchange_rate_responce)
@cache(expire=30)
async def post_exchange_rate(
    base_currency_code: str,
    target_currency_code: str,
    rate: Decimal,
    service: BaseService = Depends(ExchangeService),
):
    return await service.add_exchange_rate(
        base_currency_code, target_currency_code, rate
    )


@router.patch("/{exchange_rate}", responses=patch_exchange_rate_responce)
@cache(expire=30)
async def patch_exchange_rate(
    exchange_rate: str, rate: Decimal, service: BaseService = Depends(ExchangeService)
):
    return await service.patch_exchange_rate(exchange_pair_raw=exchange_rate, rate=rate)


@router.get("/exchange", responses=get_exchange_sum_responce)
@cache(expire=30)
async def get_exchange_sum(
    ext: ExchangePairArgs = Depends(), service: BaseService = Depends(ExchangeService)
):
    return await service.get_exchange_sum(
        ext.exchange_from, ext.exchange_to, ext.amount
    )
