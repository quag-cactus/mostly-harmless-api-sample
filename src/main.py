from fastapi import FastAPI
import uvicorn

from services import quaggy_manager

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/quaggy/check_status/{quaggy_id}")
def check_status(quaggy_id):
    s = quaggy_manager.check_quaggy()
    return {"status": s}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
