# fastapi-beginner-lab

这个项目配合 FastAPI 新手入门系列文章使用。

当前代码配合第 14 篇使用，项目已加入 OAuth2 + JWT 认证和本地 CORS 配置：

```text
app/
  __init__.py
  main.py           # 启动时建表、播种测试用户、组装路由和 CORS
  config.py         # 项目配置（含 DATABASE_URL、SECRET_KEY）
  database.py       # 数据库连接、会话管理
  models.py         # SQLAlchemy 数据库模型（Item、User）
  crud.py           # 数据库操作（items、users）
  schemas.py        # Pydantic 请求/响应模型
  auth.py           # 认证逻辑（密码哈希、JWT、当前用户）
  dependencies.py   # 公共查询参数依赖
  routers/
    __init__.py
    items.py         # items 接口（需 Bearer token）
    users.py         # 登录和用户查询接口
    health.py        # 系统状态接口
tests/
  __init__.py
  conftest.py       # 测试夹具、测试数据库配置
  test_health.py    # 健康检查相关测试
  test_items.py     # 商品接口测试
```

运行方式：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
Copy-Item .env.example .env

$env:PYTHONIOENCODING = "utf-8"
$env:PYTHONUTF8 = "1"
fastapi dev app/main.py
```

运行测试：

```powershell
pytest
```

启动后打开：

```text
http://127.0.0.1:8000/docs
```

可以试试：

```text
POST /users/token       # 用 test / test123 登录，获取 token
GET  /items             # 列表接口，支持 q 和 limit
GET  /items/1           # 存在的商品，返回 200
GET  /items/999         # 不存在的商品，返回 404
POST /items             # 创建商品
GET  /users/1           # 查看用户信息
GET  /health            # 查看服务状态
```

在 `/docs` 里访问受保护接口前，先点右上角 **Authorize**，填入 `POST /users/token` 返回的 access_token。

本地前端默认允许从 `http://localhost:5173` 请求接口。项目使用显式的 CORS 来源、方法和请求头配置，支持携带 Bearer token 的 `GET` 和 `POST` 请求。

测试账号：用户名 `test`，密码 `test123`。

如果想修改应用名称或环境，可以编辑 `.env`：

```text
APP_NAME=FastAPI Beginner Lab
APP_ENV=dev
DATABASE_URL=sqlite:///./fastapi_beginner_lab.db
```
