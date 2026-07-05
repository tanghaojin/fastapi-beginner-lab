from fastapi import APIRouter, HTTPException, Depends

from ..dependencies import get_token_header

router = APIRouter(prefix="/users", tags=["users"])

fake_users_db = {
    1: {"name": "Alice"},
    2: {"name": "Bob"},
}


@router.get(
    "/{user_id}",
    summary="获取用户信息",
    description="根据用户 ID 查询用户。用户不存在时返回 404。",
)
def read_user(user_id: int, token: str = Depends(get_token_header)):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **fake_users_db[user_id]}
