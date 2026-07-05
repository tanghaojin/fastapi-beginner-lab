from datetime import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: bool = False


class ItemCreate(ItemBase):
    pass


class ItemPublic(ItemBase):
    id: int


class ItemInDB(ItemBase):
    id: int
    cost_price: float
    created_at: datetime
