from decimal import Decimal
from datetime import date

from schemas.base import BaseSchema


__all__ = ["StockSchema", "StockCreateSchema"]


class StockId(BaseSchema):
	id: int


class StockBase(BaseSchema):
	name: str
	last: Decimal
	high: Decimal
	low: Decimal
	change: Decimal
	change_pct: str
	volume: str
	country: str
	currency: str
	date: date
	url: str


class StockSchema(StockBase, StockId):
	pass


class StockCreateSchema(StockBase):
	pass
