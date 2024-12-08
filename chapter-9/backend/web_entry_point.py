from logging import _nameToLevel

import uvicorn

from web.main import create_app
from shared.base import logger
from shared.settings import app_settings
from os import getenv

uvicorn_app = create_app()

if __name__ == "__main__":
    DOCKER_MODE = getenv("DOCKER_MODE")
    if getenv("DOCKER_MODE") == "true":
        DOCKER_MODE = True
        logger.warning("Docker mode enabled")
    else:
        logger.warning("Docker mode disabled")
    
    logger.info(
        "starting server on {}:{} with {} workers",
        app_settings.uvicorn_host,
        app_settings.uvicorn_port,
        app_settings.uvicorn_workers,
    )
    uvicorn.run(
        "web_entry_point:uvicorn_app",
        host=app_settings.uvicorn_host,
        port=app_settings.uvicorn_port,
        workers=app_settings.uvicorn_workers,
        log_level=_nameToLevel[app_settings.uvicorn_log_level],
    )
