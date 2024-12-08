from fastapi import APIRouter, Path, HTTPException, status, Query, Body, dependencies, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from typing import List, Optional, Dict, Any

from datetime import datetime, timedelta
import time
from db.manager import DBManager
from shared.base import logger


router = APIRouter(prefix="")
db = DBManager(logger)
# db._recreate_tables()

@router.get("/ping", tags=["tests"])
async def get_server_status() -> str:
    return "pong"