from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi

from asgi_correlation_id import CorrelationIdMiddleware, correlation_id
from fastapi_versionizer.versionizer import Versionizer

from src.log_initializer import init_log
from version import __version__
from src.error import ApiError
from src.routers import quaggy


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Custom title",
        version=__version__,
        summary="This is a very custom OpenAPI schema",
        description="Here's a longer description of the custom **OpenAPI** schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


init_log()

app = FastAPI()

app.add_middleware(CorrelationIdMiddleware)

app.include_router(quaggy.router)


@app.exception_handler(ApiError)
def api_error_handler(request, err: ApiError):
    raise HTTPException(status_code=err.status_code, detail=f"{err.detail}")


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

app.openapi = custom_openapi

# if __name__ == "__main__":
#    uvicorn.run("main:app", port=8000, reload=True)
