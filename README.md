# fastapi-demo

> 2026 年转行 AI 应用开发的学习记录 · 从 FastAPI 开始

## 这是什么

这是我转行 AI 应用开发过程中的练习仓库，记录从 Python 基础、FastAPI 服务开发开始的每一步。

代码全部**手工敲写、刻意不使用 AI 自动补全**——目的是把基本功练扎实，而不是看起来会写。

## 文件说明

| 文件 | 内容 |
|------|------|
| `main.py` | FastAPI 综合练习：异步/同步对比、Pydantic 校验、路径参数、查询参数、图书管理 CRUD |
| `practice.py` | 独立默写的图书管理 CRUD（不参考任何笔记完成） |
| `recall.py` | 中断学习后的记忆恢复练习 |
| `test.py` | 核心概念练习：路径参数、查询参数、请求体 |

## 涉及的知识点

- **FastAPI** —— 路由注册（装饰器）、异步路由、自动生成交互式接口文档（`/docs`）
- **Pydantic** —— 数据模型定义、类型自动校验
- **三种参数传递方式**
  - 路径参数：`/users/{user_id}`
  - 查询参数：`/search?keyword=x&limit=10`
  - 请求体：POST 的 JSON body
- **CRUD** —— POST 增 / GET 查 / PUT 改 / DELETE 删
- **异步编程** —— `async` / `await`，以及与同步方式在 I/O 密集场景下的区别
- **Git** —— add / commit / push / .gitignore 完整工作流

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

# 浏览器打开 http://localhost:8000/docs 查看交互式接口文档
```

## 开发环境

- WSL2 + Ubuntu 24.04
- Python 3.12
- FastAPI + Uvicorn

## 后续计划

这个仓库会随学习进度持续更新：

```
FastAPI 基础  ← 当前
    ↓
LangChain / LangGraph
    ↓
RAG 检索增强
    ↓
多 Agent 系统
```
