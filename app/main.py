import uvicorn
from fastapi import FastAPI
from .versions.v1 import v1

app = FastAPI()

app.include_router(v1.router)


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
