from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import get_db
from ..dependencies import get_token_header, get_common_query

router = APIRouter(prefix="/items", tags=["items"])


@router.get(
    "",
    response_model=list[schemas.ItemPublic],
    summary="获取商品列表",
    description="支持用 q 做简单名称搜索，也可以用 limit 控制返回数量。",
)
def list_items(
    queries: dict = Depends(get_common_query),
    token: str = Depends(get_token_header),
    db: Session = Depends(get_db),
):
    q = queries["q"]
    limit = queries["limit"]
    return crud.get_items(db, q=q, limit=limit)


@router.get(
    "/{item_id}",
    response_model=schemas.ItemPublic,
    summary="获取单个商品",
    description="根据商品 ID 查询商品。商品不存在时返回 404。",
)
def read_item(
    item_id: int,
    token: str = Depends(get_token_header),
    db: Session = Depends(get_db),
):
    item = crud.get_item(db, item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post(
    "",
    response_model=schemas.ItemPublic,
    summary="创建商品",
    description="接收创建商品需要的字段，服务端会补上 ID 和内部字段。",
)
def create_item(
    item: schemas.ItemCreate,
    token: str = Depends(get_token_header),
    db: Session = Depends(get_db),
):
    return crud.create_item(db, item)
