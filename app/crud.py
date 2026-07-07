from datetime import datetime, timezone

from sqlalchemy.orm import Session

from . import models, schemas


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items(db: Session, q: str | None = None, limit: int = 10):
    query = db.query(models.Item)
    if q:
        query = query.filter(models.Item.name.ilike(f"%{q}%"))
    return query.limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(
        name=item.name,
        price=item.price,
        is_offer=item.is_offer,
        cost_price=item.price * 0.6,
        created_at=datetime.now(timezone.utc),
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
