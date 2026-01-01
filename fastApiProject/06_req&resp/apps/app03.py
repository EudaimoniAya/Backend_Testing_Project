from fastapi import APIRouter
from typing import Union, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List

app3 = APIRouter()


class Addr(BaseModel):
    province: str = "四川"
    city: str = "成都"


# 请求体才有该模型，路径参数和查询参数和数据模型类没关系
class User(BaseModel):
    # name: str = Field(pattern="^a")
    name: str
    age: int = Field(default=10, gt=0, lt=100)
    birthday: Union[date, None] = None
    friends: List[int] = []
    description: Optional[str] = None
    addr: Optional[Addr] = None

    @field_validator('name')
    def name_must_alpha(cls, value):
        assert value.isalpha(), "name must be alphanumeric"
        return value


@app3.post("/user")
async def data(user: User):
    print(user.model_dump(), type(user))
    return user
