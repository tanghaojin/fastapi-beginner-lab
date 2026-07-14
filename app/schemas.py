from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    price: float
    is_offer: bool = False


class ItemCreate(ItemBase):
    pass


class ItemPublic(ItemBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ItemInDB(ItemBase):
    id: int
    cost_price: float
    created_at: datetime
    created_by: str
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class NotificationCreate(BaseModel):
    message: str
