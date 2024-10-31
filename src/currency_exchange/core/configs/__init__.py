from pydantic_settings import SettingsConfigDict

from currency_exchange.core.configs.settings_app import AppSettings
from currency_exchange.core.configs.settings_common import CommonSettings
from currency_exchange.core.configs.settings_database import DBSettings
from currency_exchange.core.configs.settings_redis import RedisSettings


class Settings(
    CommonSettings,
    DBSettings,
    AppSettings,
    RedisSettings,
):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)


settings = Settings()
