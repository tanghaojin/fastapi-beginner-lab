from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q is not None:
        item["q"] = q
    if not short:
        item["description"] = "This is a sample item used in the FastAPI beginner series."
    return item
