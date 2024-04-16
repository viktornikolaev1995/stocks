from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from config.settings import service_settings
from routes import router as stock_router


router = APIRouter()
router.include_router(stock_router, prefix="/stocks", tags=["stock-list"])


def create_app() -> FastAPI:
    app = FastAPI(
        title=service_settings.title,
        root_path=service_settings.root_path,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router)
    return app
