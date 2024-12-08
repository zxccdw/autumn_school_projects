import multiprocessing as mp

from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    pg_database: str = "db_misis"
    pg_host: str = "localhost"
    pg_port: int = 5432
    pg_username: str = "db_misis"
    pg_password: str = "db_misis" # ???

    uvicorn_host: str = "0.0.0.0"
    uvicorn_port: int = 8000
    uvicorn_workers: int = 1 # mp.cpu_count() * 2
    uvicorn_log_level: str = "WARNING"


app_settings = AppSettings()
