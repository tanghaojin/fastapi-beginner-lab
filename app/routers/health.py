from fastapi import APIRouter

router = APIRouter(tags=["system"])


@router.get(
    "/health",
    summary="查看服务状态",
    description="返回服务是否可用。",
)
def health_check():
    return {"status": "ok"}
