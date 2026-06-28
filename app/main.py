from fastapi import FastAPI
from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    price: float
    is_offer: bool = False


class ItemPublic(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool = False

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


@app.post("/items", response_model=ItemPublic)
def create_item(item: ItemCreate):
    item_data = item.model_dump()
    return {
        "id": 1,
        **item_data,
        "internal_note": "Only visible inside the server.",
    }
