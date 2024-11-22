from functools import lru_cache
import punq
from redis.asyncio import Redis

from currency_exchange.gateways.database.postgresql.database import BaseDB, Database

from currency_exchange.core.configs import settings


@lru_cache(1)
def get_conteiner():
    return _init_conteiner()


def _init_conteiner():
    container = punq.Container()

    db = Database(url=settings.POSTGRES_URL, ro_url=settings.POSTGRES_URL)
    container.register(BaseDB, Database, scope=punq.Scope.singleton, instance=db)

    redis = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    container.register(Redis, instance=redis, scope=punq.Scope.singleton)

    return container
