from fastapi import APIRouter, Request
from pydantic import BaseModel, EmailStr
from typing import Union

app7 = APIRouter()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app7.post("/create_user", response_model=UserOut)
def create_user(user: UserIn):
    # 存到数据库
    # 这个user对象仍然是原来传进来的包含密码的user对象，
    # 但是在最后返回前会经过response_model=UserOut处理
    return user
