from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_offer = Column(Boolean, default=False)
    cost_price = Column(Float)
    created_at = Column(DateTime)
    created_by = Column(String, default="system")
