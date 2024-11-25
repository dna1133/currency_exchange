from contextlib import asynccontextmanager
import logging
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from currency_exchange.api.routers import exchange
from currency_exchange.api.routers import currency

from currency_exchange.core.configs import settings
from currency_exchange.core.conteiner import get_conteiner
from currency_exchange.core.logging.logger_setup import LoggerSetup

log = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator:
    logger_setup = LoggerSetup()
    conteiner = get_conteiner()
    log.info("--- APP started")
    yield
    log.info("--- APP down")


app = FastAPI(title=settings.APPLICATION_TITTLE, lifespan=lifespan)
app.include_router(exchange.router)
app.include_router(currency.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_methods=["*"],
    allow_headers=["*"],
)
