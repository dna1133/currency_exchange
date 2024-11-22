import logging
from fastapi import APIRouter, Depends

from fastapi_cache.decorator import cache

from currency_exchange.gateways.database.models.currencies import Currencies
from currency_exchange.gateways.database.postgresql.database import BaseDB, Database
from currency_exchange.api.responses.currency_responses import (
    get_currencies_responce,
    get_currency_responce,
    post_currency_responce,
)
from currency_exchange.services.base_api_service import BaseService
from currency_exchange.services.currency_api_service import CurrencyService

router = APIRouter(
    prefix="/currensies",
    tags=["currensies"],
)

log = logging.getLogger(__name__)


@router.get("/", responses=get_currencies_responce)
@cache(expire=10)
async def get_all_currencies(
    service: BaseService = Depends(CurrencyService),
):
    return await service.get_all()


@router.get("/{code}", responses=get_currency_responce)
@cache(expire=30)
async def get_currency_by_code(
    code: str, service: BaseService = Depends(CurrencyService)
):
    return await service.find_one(code=code.upper())


@router.post("", responses=post_currency_responce)
async def post_currensies(
    code: str,
    fullname: str,
    sign: str,
    service: BaseService = Depends(CurrencyService),
):
    return await service.add_currency(code.upper(), fullname, sign)
