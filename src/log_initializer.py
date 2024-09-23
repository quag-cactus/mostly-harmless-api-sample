import logging
import sys
import pathlib

from loguru import logger
from asgi_correlation_id import correlation_id


LOGGER_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> "
    "[{correlation_id}] <level>{message}</level>"
)

ACCESS_LOGGER_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <level>{message}</level>"
)


def uvicorn_filter(record):
    # ロガー名に"uvicorn"が含まれていればTrueを返す
    return record["extra"].get("from_uvicorn_log", False)


def correlation_id_filter(record):
    request_id = correlation_id.get()
    record["correlation_id"] = request_id[:8] if not request_id is None else "-"
    return True


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record: logging.LogRecord):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).bind(
            from_uvicorn_log=True
        ).log(level, record.getMessage())


def init_log(log_dir: pathlib = pathlib.Path("./log")):

    uvicorn_loggers = (
        logging.getLogger(name)
        for name in logging.root.manager.loggerDict
        if name.startswith("uvicorn")
    )

    for uvicorn_logger in uvicorn_loggers:
        uvicorn_logger.handlers = []
        intercept_handler = InterceptHandler()
        uvicorn_logger.handlers = [intercept_handler]
        uvicorn_logger.propagate = False
        # logging.getLogger("uvicorn").handlers = [intercept_handler]

    logger.remove()
    logger.add(
        sys.stdout, format=LOGGER_FORMAT, level="DEBUG", filter=correlation_id_filter
    )
    logger.add(
        log_dir / "info.log",
        format=LOGGER_FORMAT,
        rotation="1 MB",
        retention=3,
        level="INFO",
        filter=correlation_id_filter,
    )
    logger.add(
        log_dir / "access.log",
        format=ACCESS_LOGGER_FORMAT,
        rotation="1 MB",
        retention=3,
        level="INFO",
        filter=lambda r: r["extra"].get("from_uvicorn_log", False),
    )
    logger.add(
        log_dir / "error.log",
        format=LOGGER_FORMAT,
        rotation="1 MB",
        retention=3,
        level="ERROR",
        filter=correlation_id_filter,
    )

    return
