from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(".env")
__all__ = ["service_settings", "database_settings"]


class ServiceSettings(BaseSettings):
    class Config:
        env_prefix = "service_"

    title: str = "Stocks API"
    root_path: str = ""


class DatabaseSettings(BaseSettings):
    class Config:
        env_prefix = "database_"

    driver: str = "postgresql+asyncpg"
    sync_driver: str = "postgresql+psycopg2"
    database: str = "database"
    username: str = "username"
    password: str = "password"
    host: str = "localhost"

    echo: bool = False

    def url(self,) -> str:
        return f"{self.driver}://{self.username}:{self.password}@{self.host}/{self.database}"


service_settings = ServiceSettings()
database_settings = DatabaseSettings()
