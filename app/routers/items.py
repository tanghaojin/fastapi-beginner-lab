from fastapi import APIRouter, HTTPException, Depends

from ..schemas import ItemCreate, ItemPublic
from ..dependencies import get_token_header, get_common_query

router = APIRouter(prefix="/items", tags=["items"])

fake_items_db = {
    1: {"name": "Hammer", "price": 9.99, "is_offer": False},
    2: {"name": "Screwdriver", "price": 5.50, "is_offer": True},
    3: {"name": "Wrench", "price": 15.0, "is_offer": False},
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
    for item_id, item in fake_items_db.items():
        if q is None or q.lower() in item["name"].lower():
            result.append({"id": item_id, **item})
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
    item = fake_items_db[item_id]
    return {"id": item_id, **item}


@router.post(
    "",
    response_model=ItemPublic,
    summary="创建商品",
    description="接收创建商品需要的字段，服务端会补上 ID 和内部字段。",
)
def create_item(item: ItemCreate, token: str = Depends(get_token_header)):
    item_data = item.model_dump()
    return {
        "id": 1,
        **item_data,
        "internal_note": "Only visible inside the server.",
    }
