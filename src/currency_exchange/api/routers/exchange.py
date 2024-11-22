from decimal import Decimal
import logging
from typing import Annotated
from fastapi import APIRouter, Depends

from currency_exchange.api.ischemas import exchange_params
from currency_exchange.api.responses.exchange_resposes import (
    get_all_exchange_rates_responce,
    get_exchange_rate_responce,
    post_exchange_rate_responce,
    patch_exchange_rate_responce,
    get_exchange_sum_responce,
)
from currency_exchange.services.api_services.base_api_service import BaseService
from currency_exchange.services.api_services.exchange_api_sevice import ExchangeService
from currency_exchange.services.cache_services.redis_service import CacheService


router = APIRouter(
    prefix="/exchange_rates",
    tags=["exchangeRates"],
)

log = logging.getLogger(__name__)

cache = CacheService()


@router.get("/", responses=get_all_exchange_rates_responce)
@cache.cached(expire=30)
async def get_all_exchange_rates(
    service: BaseService = Depends(ExchangeService),
):
    result = await service.get_all_exchange_rates()
    return result


@router.post("/", responses=post_exchange_rate_responce)
async def post_exchange_rate(
    base_currency_code: str,
    target_currency_code: str,
    rate: Decimal,
    service: BaseService = Depends(ExchangeService),
):
    result = await service.add_exchange_rate(
        base_currency_code.upper(), target_currency_code.upper(), rate
    )
    return result


@router.patch("/{exchange_rate}", responses=patch_exchange_rate_responce)
async def patch_exchange_rate(
    exchange_rate: str, rate: Decimal, service: BaseService = Depends(ExchangeService)
):
    result = await service.patch_exchange_rate(
        exchange_pair_raw=exchange_rate.upper(), rate=rate
    )
    return result


@router.get("/exchange", responses=get_exchange_sum_responce)
async def get_exchange_sum(
    ext: Annotated[dict, Depends(exchange_params)],
    service: BaseService = Depends(ExchangeService),
):

    result = await service.get_exchange_sum(
        ext["exchange_from"].upper(), ext["exchange_to"].upper(), ext["amount"]
    )
    return result


@router.get("/{ex_rate}", responses=get_exchange_rate_responce)
@cache.cached(expire=30)
async def get_exchange_rate(
    ex_rate: str,
    service: BaseService = Depends(ExchangeService),
):
    result = await service.get_exchange_rate(ex_rate.upper())
    return result
