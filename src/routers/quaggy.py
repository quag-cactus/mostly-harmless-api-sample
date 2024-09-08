import datetime

from fastapi import APIRouter
from fastapi_versionizer.versionizer import api_version
from asgi_correlation_id import correlation_id
from loguru import logger

from src.services import quaggy_manager

router = APIRouter(prefix="/quaggy", tags=["quaggy"], redirect_slashes=False)


@api_version(1)
@router.get("/check_status/{quaggy_id}")
def check_status(quaggy_id):
    logger.info(f"Checking status of quaggy with id: {quaggy_id}")
    s = quaggy_manager.check_quaggy_status(quaggy_id)
    return {"request_id": correlation_id.get(), "status": s}

@api_version(2)
@router.get("/get_schedule_now/{quaggy_id}")
def get_schedule_now(quaggy_id):
    now_time = datetime.datetime.now()
    s = quaggy_manager.get_quaggy_schedule(quaggy_id, now_time)
    return {"request_id": correlation_id.get(), "status": s}
