from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_FILE = Path(__file__).parents[2].joinpath(".env")


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_FILE, env_file_encoding="utf-8", extra="ignore"
    )


class Config(BaseConfig):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: SecretStr
    TRON_API_KEY: SecretStr

config = Config()


def get_db_url():
    return (f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASSWORD.get_secret_value()}@"
            f"{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}")
