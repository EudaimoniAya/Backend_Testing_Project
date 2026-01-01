from fastapi import APIRouter
from typing import Union, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List

from fastapi import Form

app4 = APIRouter()


# 如果直接在括号中填username: str，那么表示的是查询参数
# 这里填写的是username:str=Form()，表示请求体中的一个form表单的参数
# fastapi在做解析时会从请求体中按照content-type=urlencoded的格式解析出数据交付给username
@app4.post("/register")
async def data(username: str = Form(), password: str = Form()):
    # 真实项目需要在此完成数据库的添加操作
    print(f"Username: {username}, Password: {password}")
    return {
        "username": username
    }
