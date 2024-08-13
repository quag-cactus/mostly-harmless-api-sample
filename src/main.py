import time

from fastapi import FastAPI
import uvicorn

from services import quaggy_manager

from asgi_correlation_id import CorrelationIdMiddleware, correlation_id
from loguru import logger

logger.add("./log/log_info.log", rotation="1MB", retention=3, level="INFO")
logger.add("./log/log_err.log", rotation="1MB", retention=3, level="ERROR")

app = FastAPI()

app.add_middleware(CorrelationIdMiddleware)


@app.get("/")
async def root():
    return {"message": "Hello World", "request_id": correlation_id.get()}


@app.post("/post")
async def root():
    return {"message": "Hello Posted World", "request_id": correlation_id.get()}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/quaggy/check_status/{quaggy_id}")
def check_status(quaggy_id):
    logger.info(f"Checking status of quaggy with id: {quaggy_id}")
    s = quaggy_manager.check_quaggy_status(quaggy_id)
    return {"request_id": correlation_id.get(), "status": s}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
