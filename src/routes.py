from typing import List
from fastapi import APIRouter, Depends
from db import StockService, get_stock_service
from schemas import StockSchema, StockCreateSchema
from datetime import date


router = APIRouter()


@router.get("", response_model=List[StockSchema])
async def retrieve_stocks(
	offset: int = 0,
	limit: int = 100,
	date_from: date = date.min,
	date_to: date = date.max,
	service: StockService = Depends(get_stock_service),  # noqa: F405
):
	wheels = await service.get_stocks(
		offset=offset,
		limit=limit,
		date_from=date_from,
		date_to=date_to,
		pk=None
	)
	return wheels


@router.post("", response_model=StockSchema)
async def create_stock(
	stock: StockCreateSchema,
	service: StockService = Depends(get_stock_service)  # noqa: F405
):
	return await service.create_stock(stock)
