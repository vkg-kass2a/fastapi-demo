from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    sentence: str


@app.post("/recall")
async def recall(item: Item):
    return {"message": f"你说了：{item.sentence}"}