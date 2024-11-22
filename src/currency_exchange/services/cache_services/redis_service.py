from dataclasses import dataclass
from decimal import Decimal
from functools import wraps
import json
from typing import Any, Callable

from redis.asyncio import Redis

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import class_mapper

from currency_exchange.core.conteiner import get_conteiner
from currency_exchange.domain.entity.base import BaseEntity
from currency_exchange.services.cache_services.base_cache_servise import (
    BaseCacheService,
)


@dataclass
class CacheService(BaseCacheService):
    conteiner = get_conteiner()
    redis = conteiner.resolve(Redis)

    def cached(self, expire: int = 60):
        def decorator(func: Callable):
            @wraps(func)
            async def wrapper(*args, **kwargs) -> Any:

                cache_key = f"{func.__name__}:{args}:{kwargs}"
                cached_result = await self.redis.get(cache_key)
                if cached_result:
                    return json.loads(cached_result)
                result = await func(*args, **kwargs)
                if isinstance(result, BaseEntity):
                    result = result.to_dict()
                elif isinstance(result, list):
                    result = [self._sqlalchemy_to_dict(obj) for obj in result]
                elif isinstance(result, object):
                    result = self._sqlalchemy_to_dict(result)
                elif isinstance(result, dict):
                    result = self._sqlalchemy_to_dict(result)
                await self.redis.set(cache_key, json.dumps(result), ex=expire)
                return result

            return wrapper

        return decorator

    def _sqlalchemy_to_dict(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            result = {
                c.key: getattr(obj, c.key) for c in class_mapper(obj.__class__).columns
            }
            result = self._sqlalchemy_to_dict(result)
            return result
        elif isinstance(obj, dict):
            return {k: self._sqlalchemy_to_dict(v) for k, v in obj.items()}
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            return obj
