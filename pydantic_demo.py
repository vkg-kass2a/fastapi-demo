from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


class Address(BaseModel):
    city: str
    district: str


class User(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    age: int = Field(ge=18, le=65)
    email: str | None = None
    address: Address
    skills: list[str] = []


@app.post("/profile")
async def create_profile(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "city": user.address.city,
        "skills": user.skills,
    }
