from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator

from fastapi import FastAPI
from redis.asyncio import Redis

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from currency_exchange.api.routers import exchange
from currency_exchange.api.routers import currency

from currency_exchange.core.configs import settings

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


db = {}

app = FastAPI(title=settings.APPLICATION_TITTLE, lifespan=lifespan)
app.include_router(exchange.router)
app.include_router(currency.router)
