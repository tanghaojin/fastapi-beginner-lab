from fastapi import APIRouter, Depends

from ..config import Settings, get_settings

router = APIRouter(tags=["system"])


@router.get(
    "/health",
    summary="查看服务状态",
    description="返回服务是否可用。",
)
def health_check(settings: Settings = Depends(get_settings)):
    return {
        "status": "ok",
        "app_name": settings.app_name,
        "app_env": settings.app_env,
    }
