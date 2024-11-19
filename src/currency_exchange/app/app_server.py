from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from redis.asyncio import Redis

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from currency_exchange.api.routers import exchange
from currency_exchange.api.routers import currency

from currency_exchange.core.configs import settings
from currency_exchange.core.logging.logger_setup import LoggerSetup

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    logger_setup = LoggerSetup()
    log.info("--- APP started")
    redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    log.info("--- APP down")


app = FastAPI(title=settings.APPLICATION_TITTLE, lifespan=lifespan)
app.include_router(exchange.router)
app.include_router(currency.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
