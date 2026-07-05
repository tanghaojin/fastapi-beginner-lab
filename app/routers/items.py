from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, Depends

from ..schemas import ItemCreate, ItemInDB, ItemPublic
from ..dependencies import get_token_header, get_common_query

router = APIRouter(prefix="/items", tags=["items"])

fake_items_db = {
    1: ItemInDB(
        id=1,
        name="Hammer",
        price=9.99,
        is_offer=False,
        cost_price=4.0,
        created_at=datetime(2026, 1, 1, tzinfo=timezone.utc),
    ),
    2: ItemInDB(
        id=2,
        name="Screwdriver",
        price=5.50,
        is_offer=True,
        cost_price=2.0,
        created_at=datetime(2026, 1, 2, tzinfo=timezone.utc),
    ),
    3: ItemInDB(
        id=3,
        name="Wrench",
        price=15.0,
        is_offer=False,
        cost_price=7.0,
        created_at=datetime(2026, 1, 3, tzinfo=timezone.utc),
    ),
}


@router.get(
    "",
    response_model=list[ItemPublic],
    summary="获取商品列表",
    description="支持用 q 做简单名称搜索，也可以用 limit 控制返回数量。",
)
def list_items(queries: dict = Depends(get_common_query), token: str = Depends(get_token_header)):
    q = queries["q"]
    limit = queries["limit"]
    result = []
    for item in fake_items_db.values():
        if q is None or q.lower() in item.name.lower():
            result.append(item)
    return result[:limit]


@router.get(
    "/{item_id}",
    response_model=ItemPublic,
    summary="获取单个商品",
    description="根据商品 ID 查询商品。商品不存在时返回 404。",
)
def read_item(item_id: int, token: str = Depends(get_token_header)):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]


@router.post(
    "",
    response_model=ItemPublic,
    summary="创建商品",
    description="接收创建商品需要的字段，服务端会补上 ID 和内部字段。",
)
def create_item(item: ItemCreate, token: str = Depends(get_token_header)):
    new_item = ItemInDB(
        id=max(fake_items_db) + 1,
        **item.model_dump(),
        cost_price=item.price * 0.6,
        created_at=datetime.now(timezone.utc),
    )
    fake_items_db[new_item.id] = new_item
    return new_item
