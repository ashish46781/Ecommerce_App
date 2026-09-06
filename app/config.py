from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "E-Commerce API"
    debug: bool = False
    database_host: str = "127.0.0.1"
    database_port: int = 5432
    database_name: str = "ecommerce"
    database_user: str = "ecommerce_app"
    database_password: SecretStr

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
