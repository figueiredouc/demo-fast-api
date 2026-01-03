from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = "development"
    database_url: str
    secret_key: str
    jwt_lifetime_minutes: int = 60
    superuser_email: str = "admin@example.com"
    superuser_password: str = "admin123"

    model_config = {"env_file": ".env", "extra": "ignore"}


settings = Settings()

