from enum import Enum

from pydantic_settings import BaseSettings


class Environment(str, Enum):
    DEV = "dev"
    PROD = "prod"
    TEST = "test"


class CommonSettings(BaseSettings):
    SERVICE_NAME: str = "currency_exchange"
    LOGGING_LEVEL: str
    ENVIRONMENT: Environment = Environment.DEV
