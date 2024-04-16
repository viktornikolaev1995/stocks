from typing import AsyncGenerator
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.base import Session
from db.services import StockService

__all__ = ["get_stock_service"]


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:
        yield session


def get_stock_service(session: AsyncSession = Depends(get_async_session)):
    return StockService(session=session)  # noqa: F405
