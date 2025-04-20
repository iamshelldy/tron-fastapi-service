from fastapi import FastAPI

from app.core.logger import init_logger
from app.services.tron.router import router as tron_router


def get_app() -> FastAPI:
    init_logger()

    app = FastAPI(title="Tron FastAPI Service")
    app.include_router(tron_router)

    return app
