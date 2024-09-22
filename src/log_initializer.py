from loguru import logger
import sys

import asgi_correlation_id

from uvicorn.config import LOGGING_CONFIG


LOGGER_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message}</level>"
)


def init_log():

    logger.configure(extra={"request_id": ""})  # Default values
    logger.remove()
    logger.add(sys.stderr, format=LOGGER_FORMAT)
