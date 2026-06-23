# fastapi-beginner-lab

这个项目配合 FastAPI 新手入门系列文章使用。

第 1 篇只保留一个最小 FastAPI 应用：

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
