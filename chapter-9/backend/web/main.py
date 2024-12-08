from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from web.router.router import router


def create_app() -> FastAPI:
    fastapi_app = FastAPI()

    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    fastapi_app.include_router(router)
    return fastapi_app
