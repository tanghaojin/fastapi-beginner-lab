from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

from .dependencies import get_token_header, get_common_query


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


@app.get("/items", response_model=list[ItemPublic])
def list_items(queries: dict = Depends(get_common_query), token: str = Depends(get_token_header)):
    q = queries["q"]
    limit = queries["limit"]
    result = []
    for item_id, item in fake_items_db.items():
        if q is None or q.lower() in item["name"].lower():
            result.append({"id": item_id, **item})
    return result[:limit]


@app.get("/items/{item_id}", response_model=ItemPublic)
def read_item(item_id: int, token: str = Depends(get_token_header)):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    item = fake_items_db[item_id]
    return {"id": item_id, **item}


@app.post("/items", response_model=ItemPublic)
def create_item(item: ItemCreate, token: str = Depends(get_token_header)):
    item_data = item.model_dump()
    return {
        "id": 1,
        **item_data,
        "internal_note": "Only visible inside the server.",
    }


@app.get("/users/{user_id}")
def read_user(user_id: int, token: str = Depends(get_token_header)):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **fake_users_db[user_id]}
