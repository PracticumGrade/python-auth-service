from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    user: str = Field(alias='POSTGRES_USER')
    password: str = Field(alias='POSTGRES_PASSWORD')
    host: str = Field(alias='POSTGRES_HOST')
    port: str = Field(alias='POSTGRES_PORT')
    db: str = Field(alias='POSTGRES_DB')


settings = Settings()
