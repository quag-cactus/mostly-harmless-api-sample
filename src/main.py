import time

from fastapi import FastAPI
import uvicorn

from src.services import quaggy_manager

from asgi_correlation_id import CorrelationIdMiddleware, correlation_id
from loguru import logger

from src.routers import quaggy

logger.add("./log/log_info.log", rotation="1MB", retention=3, level="INFO")
logger.add("./log/log_err.log", rotation="1MB", retention=3, level="ERROR")

app = FastAPI()

app.add_middleware(CorrelationIdMiddleware)

app.include_router(quaggy.router)


@app.get("/")
async def root():
    return {"message": "Hello World", "request_id": correlation_id.get()}


@app.post("/post")
async def root():
    return {"message": "Hello Posted World", "request_id": correlation_id.get()}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}



#if __name__ == "__main__":
#    uvicorn.run("main:app", port=8000, reload=True)
