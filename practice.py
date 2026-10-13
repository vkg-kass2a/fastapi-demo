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


#查 （全部）
@app.get("/books")
async def list_books():
    return books

#增
@app.post("/books")
async def create_book(book: Book):
    global next_id          # 声明要改全局变量
    book.id = next_id       # 分配当前 id
    next_id += 1            # 计数器 +1
    books.append(book)
    return book

#查 （单个）
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for b in books:
        if b.id == book_id:
            return b
    return {"message": "Book not found"}


#改
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