from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import crud, models
from .auth import hash_password
from .config import get_settings
from .database import engine, SessionLocal
from .routers import health, items, users

models.Base.metadata.create_all(bind=engine)

settings = get_settings()

openapi_tags = [
    {
        "name": "items",
        "description": "商品相关接口，用来练习列表、查询和创建。",
    },
    {
        "name": "users",
        "description": "用户相关接口，包含登录和查询。",
    },
    {
        "name": "system",
        "description": "系统状态接口，用来检查服务是否正常。",
    },
]

app = FastAPI(title=settings.app_name, openapi_tags=openapi_tags)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(items.router)
app.include_router(users.router)
app.include_router(health.router)


@app.get("/", tags=["system"], summary="首页")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/ping", tags=["system"], summary="测试服务连通性")
def ping():
    return {"message": "pong"}


def seed_test_user():
    db = SessionLocal()
    user = crud.get_user_by_username(db, "test")
    if user is None:
        crud.create_user(db, "test", hash_password("test123"))
    db.close()


seed_test_user()
