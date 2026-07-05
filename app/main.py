from fastapi import FastAPI

from .routers import health, items, users

openapi_tags = [
    {
        "name": "items",
        "description": "商品相关接口，用来练习列表、查询和创建。",
    },
    {
        "name": "users",
        "description": "用户相关接口，目前只保留最小查询示例。",
    },
    {
        "name": "system",
        "description": "系统状态接口，用来检查服务是否正常。",
    },
]

app = FastAPI(title="FastAPI Beginner Lab", openapi_tags=openapi_tags)

app.include_router(items.router)
app.include_router(users.router)
app.include_router(health.router)


@app.get("/", tags=["system"], summary="首页")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/ping", tags=["system"], summary="测试服务连通性")
def ping():
    return {"message": "pong"}
