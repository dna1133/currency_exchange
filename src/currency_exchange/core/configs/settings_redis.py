from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def REDIS_URL(self):
        return f"{self.REDIS_HOST}:{self.REDIS_PORT}"
