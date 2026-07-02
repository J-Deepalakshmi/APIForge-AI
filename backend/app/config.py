from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str

    HOST: str
    PORT: int

    DATABASE_URL: str

    GOOGLE_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()