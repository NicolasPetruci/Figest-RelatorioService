import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port: int = int(os.getenv("PORT", "3004"))
    database_url: str = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/figest")

    class Config:
        env_file = ".env"

settings = Settings()
