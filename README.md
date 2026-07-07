# fastapi-beginner-lab

这个项目配合 FastAPI 新手入门系列文章使用。

当前代码配合第 11 篇使用，项目已经接入 SQLite 数据库：

```text
app/
  __init__.py
  main.py           # 启动时自动建表，组装路由
  config.py         # 项目配置（含 DATABASE_URL）
  database.py       # 数据库连接、会话管理
  models.py         # SQLAlchemy 数据库模型
  crud.py           # 数据库操作（增删改查）
  schemas.py        # Pydantic 请求/响应模型
  dependencies.py   # 公共依赖（token 校验、查询参数）
  routers/
    __init__.py
    items.py         # items 相关接口（已接入数据库）
    users.py         # users 相关接口
    health.py        # 系统状态接口
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

启动后打开：

```text
http://127.0.0.1:8000/docs
```

可以试试：

```text
GET /items              # 列表接口，需要 x-token，支持 q 和 limit
GET /items/1            # 存在的商品，返回 200
GET /items/999          # 不存在的商品，返回 404
GET /users/1            # 存在的用户，返回 200
GET /health             # 查看服务状态
POST /items             # 创建商品
```

在 `/docs` 里调用接口时，需要在 `x-token` 请求头里填入 `secret-token`，否则会返回 401。

如果想修改应用名称或环境，可以编辑 `.env`：

```text
APP_NAME=FastAPI Beginner Lab
APP_ENV=dev
DATABASE_URL=sqlite:///./fastapi_beginner_lab.db
```
