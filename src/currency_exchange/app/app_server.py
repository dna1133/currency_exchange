from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator

from fastapi import FastAPI
import redis

from currency_exchange.gateways.postgresql.database import Database

from currency_exchange.core.configs import settings

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    db["db"] = Database(url=settings.POSTGRES_URL, ro_url=settings.POSTGRES_URL)
    db["cache_db"] = redis.from_url(settings.REDIS_URL)
    yield
    db.clear()


db = {}

app = FastAPI(title=settings.APPLICATION_TITTLE, lifespan=lifespan)
