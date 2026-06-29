# fastapi-beginner-lab

这个项目配合 FastAPI 新手入门系列文章使用。

当前代码配合第 5 篇使用，包含一个最小 FastAPI 应用、内存数据表、带响应模型的创建接口，以及用 HTTPException 处理资源不存在的查询接口：

```text
app/
  main.py
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
http://127.0.0.1:8000/items/1       # 存在的商品，返回 200
http://127.0.0.1:8000/items/999     # 不存在的商品，返回 404
http://127.0.0.1:8000/users/1       # 存在的用户，返回 200
http://127.0.0.1:8000/users/999     # 不存在的用户，返回 404
```

也可以在 `/docs` 里调用 `POST /items`，请求体示例：

```json
{
  "name": "Notebook",
  "price": 12.5,
  "is_offer": true
}
```

响应里会出现 `id`，但不会出现服务端内部字段 `internal_note`。
