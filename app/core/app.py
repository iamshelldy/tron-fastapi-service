from fastapi import FastAPI

from app.services.tron.router import router as tron_router


def get_app() -> FastAPI:
    app = FastAPI(title="Tron FastAPI Service")

    app.include_router(tron_router)

    return app
