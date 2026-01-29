from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    API_V1_PREFIX: str = "/api/v1"
    APP_NAME: str = "ApexStore API"
    ENV: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
