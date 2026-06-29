from fastapi import APIRouter, HTTPException, Depends

from ..dependencies import get_token_header

router = APIRouter()

fake_users_db = {
    1: {"name": "Alice"},
    2: {"name": "Bob"},
}


@router.get("/users/{user_id}")
def read_user(user_id: int, token: str = Depends(get_token_header)):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **fake_users_db[user_id]}
