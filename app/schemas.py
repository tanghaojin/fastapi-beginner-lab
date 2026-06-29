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
