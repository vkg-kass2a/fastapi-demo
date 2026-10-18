from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 内存数据库
todos = []
next_id = 1


class Todo(BaseModel):
    id: int | None = None
    title: str = Field(min_length=1, max_length=100)
    done: bool = False


# 增
@app.post("/todos")
async def create_todo(todo: Todo):
    global next_id
    todo.id = next_id
    next_id += 1
    todos.append(todo)
    return todo


# 查全部 (包含筛选细节)
@app.get("/todos")
async def list_todos(done: bool | None = None):
    # 如果 done 是 None（即客户端没传这个参数），直接返回全部
    if done is None:
        return todos
    
    # 如果传了，就根据 done 的值进行过滤
    return [t for t in todos if t.done == done]


# 查单个
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for t in todos:
        if t.id == todo_id:
            return t
    return {"message": "Todo not found"}


# 改
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todo.id = todo_id  # 保持原本的 id 不变
            todos[i] = todo
            return todo
    return {"message": "Todo not found"}


# 删
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            deleted = todos.pop(i)
            return {"message": f"Todo {todo_id} deleted", "deleted": deleted}
    return {"message": "Todo not found"}