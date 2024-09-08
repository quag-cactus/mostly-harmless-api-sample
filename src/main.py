from fastapi import FastAPI, HTTPException
import uvicorn

from asgi_correlation_id import CorrelationIdMiddleware, correlation_id
from loguru import logger
from fastapi_versionizer.versionizer import Versionizer

from src.error import ApiError
from src.routers import quaggy

logger.add("./log/log_info.log", rotation="1MB", retention=3, level="INFO")
logger.add("./log/log_err.log", rotation="1MB", retention=3, level="ERROR")

app = FastAPI()

app.add_middleware(CorrelationIdMiddleware)

app.include_router(quaggy.router)

@app.exception_handler(ApiError)
def api_error_handler(request, err: ApiError):
    raise HTTPException(status_code=err.status_code, detail=f'{err.detail}')

@app.get("/")
async def root():
    return {"message": "Hello World", "request_id": correlation_id.get()}


@app.post("/post")
async def root():
    return {"message": "Hello Posted World", "request_id": correlation_id.get()}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}




versions = Versionizer(
    app=app,
    prefix_format="/v{major}",
    semantic_version_format="{major}",
    latest_prefix="/latest",
    sort_routes=True,
).versionize()

# if __name__ == "__main__":
#    uvicorn.run("main:app", port=8000, reload=True)
