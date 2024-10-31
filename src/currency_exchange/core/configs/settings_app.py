from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    APPLICATION_TITTLE: str = "Currency Exchange"

    APPLICATION_HOST: str
    APPLICATION_PORT: int
    APPLICATION_WORKERS: int
