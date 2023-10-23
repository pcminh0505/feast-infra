from typing import List
from pydantic import BaseModel

from projects import Project


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    username: str


class User(UserBase):
    id: int
    Projects: List[Project] = []

    class Config:
        orm_mode = True
