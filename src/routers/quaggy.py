from fastapi import APIRouter
from fastapi_versionizer.versionizer import api_version
from asgi_correlation_id import correlation_id
from loguru import logger

from src.services import quaggy_manager

router = APIRouter(prefix="/quaggy", tags=["quaggy"])


@api_version(1)
@router.get("/check_status/{quaggy_id}")
def check_status(quaggy_id):
    logger.info(f"Checking status of quaggy with id: {quaggy_id}")
    s = quaggy_manager.check_quaggy_status(quaggy_id)
    return {"request_id": correlation_id.get(), "status": s}
