from fastapi import FastAPI

from .routers import items, users

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/ping")
def ping():
    return {"message": "pong"}
