
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Nexus AI"
    APP_ENV: str = "development"
    DEBUG: bool = True

    DATABASE_URL: str = ""

    OPENAI_API_KEY: str | None = None

    JWT_SECRET_KEY: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
