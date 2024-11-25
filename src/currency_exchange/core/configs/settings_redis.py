from pydantic import RedisDsn
from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DSN: RedisDsn = "redis://"

    @property
    def REDIS_URL(self):
        return f"{self.REDIS_HOST}:{self.REDIS_PORT}"
