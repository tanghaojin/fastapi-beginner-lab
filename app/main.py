from fastapi import FastAPI, HTTPException
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


fake_items_db = {
    1: {"name": "Hammer", "price": 9.99, "is_offer": False},
    2: {"name": "Screwdriver", "price": 5.50, "is_offer": True},
    3: {"name": "Wrench", "price": 15.0, "is_offer": False},
}

fake_users_db = {
    1: {"name": "Alice"},
    2: {"name": "Bob"},
}

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/ping")
def ping():
    return {"message": "pong"}


@app.get("/items/{item_id}", response_model=ItemPublic)
def read_item(item_id: int):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item = fake_items_db[item_id]
    return {"id": item_id, **item}


@app.post("/items", response_model=ItemPublic)
def create_item(item: ItemCreate):
    item_data = item.model_dump()
    return {
        "id": 1,
        **item_data,
        "internal_note": "Only visible inside the server.",
    }


@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **fake_users_db[user_id]}
