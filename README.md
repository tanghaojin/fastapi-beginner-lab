# fastapi-beginner-lab

这个项目配合 FastAPI 新手入门系列文章使用。

当前代码配合第 6 篇使用，包含依赖注入示例：用 `Depends` 复用公共校验逻辑，以及一个统一的查询参数依赖：

```text
app/
  __init__.py
  main.py
  dependencies.py
```

运行方式：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .

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
GET /items              # 列表接口，需要 x-token 请求头，支持 q 和 limit 查询参数
GET /items/1           # 存在的商品，返回 200
GET /items/999         # 不存在的商品，返回 404
GET /users/1           # 存在的用户，返回 200
POST /items             # 创建商品，请求体需要 name、price、is_offer
```

在 `/docs` 里调用接口时，需要在 `x-token` 请求头里填入 `secret-token`，否则会返回 401。
