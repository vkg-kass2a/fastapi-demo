# fastapi-demo

FastAPI 基础练习 —— 路由、Pydantic 模型、路径/查询参数、CRUD 接口。

## 文件说明

| 文件 | 内容 |
|------|------|
| `main.py` | 综合练习：异步/同步对比、Pydantic 校验、路径参数、查询参数、图书管理 CRUD |
| `test.py` | 核心概念练习：路径参数、查询参数、请求体 |
| `practice.py` | 图书管理 CRUD 练习 |
| `recall.py` | 记忆恢复练习 |

## 涉及的知识点

- **FastAPI** —— 路由注册（装饰器）、异步路由、自动生成接口文档（`/docs`）
- **Pydantic** —— 数据模型定义、类型自动校验
- **三种参数传递方式**
  - 路径参数：`/users/{user_id}`
  - 查询参数：`/search?keyword=x&limit=10`
  - 请求体：POST 的 JSON body
- **CRUD** —— POST 增 / GET 查 / PUT 改 / DELETE 删
- **异步编程** —— `async` / `await`

## 怎么跑起来

需要 Python 3.10+。

```bash
# 创建并激活虚拟环境
python3 -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install fastapi uvicorn

# 启动服务
uvicorn main:app --reload
```

浏览器打开 http://localhost:8000/docs 查看交互式接口文档。

## 环境

WSL + Ubuntu 24.04 · Python 3.12 · FastAPI + Uvicorn
