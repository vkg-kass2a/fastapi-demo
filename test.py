from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int


@app.get("/ping")
async def ping():
    return {"msg": "pong"}


@app.post("/user")
async def create_user(user: User):
    return {"message": f"你好 {user.name}, 你 {user.age}岁"}

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/search")
async def get_search(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit":limit }
