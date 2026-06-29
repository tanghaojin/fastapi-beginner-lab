from fastapi import Header, HTTPException, Query
from typing import Annotated


def get_token_header(x_token: str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return x_token


def get_common_query(
    q: str | None = Query(None, description="搜索关键词"),
    limit: int = Query(10, ge=1, le=100, description="返回数量上限"),
):
    return {"q": q, "limit": limit}
