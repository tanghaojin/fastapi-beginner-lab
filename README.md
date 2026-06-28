# fastapi-beginner-lab

这个项目配合 FastAPI 新手入门系列文章使用。

当前代码配合第 3 篇使用，包含一个最小 FastAPI 应用、一个接收 URL 参数的接口，以及一个接收 JSON 请求体的接口：

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
http://127.0.0.1:8000/items/3?q=book&short=true
```

也可以在 `/docs` 里调用 `POST /items`，请求体示例：

```json
{
  "name": "Notebook",
  "price": 12.5,
  "is_offer": true
}
```
