import asyncio
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Book(BaseModel):
    id: int | None = None   # id 可选，创建时自动分配
    title: str
    author: str
    price: float

books = []  #内存数据库
next_id = 1     # id 计数器，从这里开始

# ===== Pydantic 数据模型 =====
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None


# ===== 同步函数 =====
@app.get("/sync")
def sync_demo():
    import time
    time.sleep(2)
    return {"message": "同步完成，等了2秒"}


# ===== 异步函数 =====
@app.get("/async")
async def async_demo():
    await asyncio.sleep(2)
    return {"message": "异步完成，等了2秒"}


# ===== POST + 数据校验 =====
@app.post("/items")
async def create_item(item: Item):
    price_with_tax = item.price * 1.13
    return {
        "name": item.name,
        "price": item.price,
        "price_with_tax": round(price_with_tax, 2),
        "description": item.description
    }

# ===== 路径参数 path parameter =====
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    """URL 里直接放 ID：/users/42 就能拿到 42"""
    return {"user_id": user_id, "user_id_type": type(user_id).__name__}


# ===== 查询参数 query parameter =====
@app.get("/search")
async def search(keyword: str, limit: int = 10):
    """URL 问号后面传：/search?keyword=键盘&limit=5"""
    return {"keyword": keyword, "limit": limit}


# ===== 两者结合 =====
@app.get("/users/{user_id}/orders")
async def get_user_orders(user_id: int, status: str = "all"):
    """路径参数 + 查询参数一起用"""
    return {"user_id": user_id, "status": status}


# 增
@app.post("/books")
async def create_book(book: Book):
    global next_id          # 声明要改全局变量
    book.id = next_id       # 分配当前 id
    next_id += 1            # 计数器 +1
    books.append(book)
    return book

# 查（列出全部）
@app.get("/books")
async def list_books():
    return books


# 查（单个）
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for b in books:
        if b.id == book_id:
            return b
    return {"message": "Book not found"}


# 改
@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    for i, b in enumerate(books):   # enumerate 同时拿到"下标 i"和"书 b"
        if b.id == book_id:
            book.id = book_id        # 保持原 id 不变
            books[i] = book          # 用新书替换旧书
            return book
    return {"message": "Book not found"}


# 删
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b.id == book_id:
            deleted = books.pop(i)   # pop 按位置删除，并返回被删的书
            return {"message": f"Book {book_id} deleted", "deleted": deleted}
    return {"message": "Book not found"}