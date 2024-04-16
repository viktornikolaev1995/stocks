from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config import database_settings

__all__ = [
    "Session",
    "Base",
]

engine = create_async_engine(
    database_settings.url(),
    future=True,
    pool_size=20,
    pool_pre_ping=True,
    pool_use_lifo=True,
    echo=database_settings.echo,
)
Session = sessionmaker(
    future=True,
    class_=AsyncSession,
    bind=engine,
    expire_on_commit=False,
)
Base = declarative_base()
