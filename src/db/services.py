from datetime import date
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import StockCreateSchema
from .models import Stock

__all__ = ["StockService"]


class StockService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_stocks(
        self,
        offset: int,
        limit: int,
        date_from: date,
        date_to: date,
        pk: int | None,
    ):
        filters = set()
        filters.add(Stock.date.between(date_from, date_to))
        if pk is not None:
            filters.add(Stock.id == pk)

        stock_list = await self.session.scalars(
            select(Stock).where(and_(*filters)).order_by("id").offset(offset).limit(limit)
        )
        return stock_list.all()

    async def create_stock(self, stock_schema: StockCreateSchema):
        stock = Stock(**stock_schema.dict())
        self.session.add(stock)
        await self.session.commit()
        await self.session.refresh(stock)
        return stock
