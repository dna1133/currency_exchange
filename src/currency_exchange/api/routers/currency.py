import logging
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from currency_exchange.api.responses.currency_responses import (
    get_currencies_responce,
    get_currency_responce,
    post_currency_responce,
)
from currency_exchange.api.schemas.currency_schemas import CurrencySchema
from currency_exchange.services.api_services.base_api_service import BaseService
from currency_exchange.services.api_services.currency_api_service import CurrencyService
from currency_exchange.services.cache_services.redis_service import CacheService

router = APIRouter(
    prefix="/currenсies",
    tags=["currenсies"],
)

log = logging.getLogger(__name__)
cache = CacheService()


@router.get("/", responses=get_currencies_responce)
@cache.cached(expire=30)
async def get_all_currencies(
    service: BaseService = Depends(CurrencyService),
):
    result = await service.get_all()
    return result


@router.get("/{code}", responses=get_currency_responce)
@cache.cached()
async def get_currency_by_code(
    code: str, service: BaseService = Depends(CurrencyService)
):
    result = await service.find_one(code=code.upper())
    return result


@router.post("", responses=post_currency_responce)
async def post_currensies(
    code: str,
    fullname: str,
    sign: str,
    service: BaseService = Depends(CurrencyService),
):
    result = await service.add_currency(code.upper(), fullname, sign)
    return result
