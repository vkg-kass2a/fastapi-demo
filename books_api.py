from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


# 内存数据库
books = []
next_id = 1


class Book(BaseModel):
    id: int | None = None
    title: str = Field(min_length=1, max_length=50)
    author: str
    price: float = Field(gt=0)



# 增
@app.post("/books")
async def create_book(book: Book):
    global next_id
    book.id = next_id
    next_id += 1
    books.append(book)
    return book



# 查全部
@app.get("/books")
async def list_books():
    return books


# 查单个
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for b in books:
        if b.id == book_id:
            return b
    return {"message": "Book not found"}


# 改
@app.put("/books/{book_id}")
async def update_book(book_id: int, book: Book):
    for i, b in enumerate(books):
        if b.id == book_id:
            book.id = book_id
            books[i] = book
            return book
    return {"message": "Book not found"}


# 删
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i, b in enumerate(books):
        if b.id == book_id:
            deleted = books.pop(i)
            return {"message": f"Book {book_id} deleted", "deleted": deleted}
    return {"message": "Book not found"}
