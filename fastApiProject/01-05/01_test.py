from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, PositiveInt


# Pydantic的BaseModel一旦被继承，可以完成数据验证
# 当实例化一个对象时，如果传进来的参数不匹配，会尝试做一个转换
class User(BaseModel):
    id: int     # id 需要是一个int，是一个必需字段
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []

# 可以理解为前后端分离时，前端传给后端的数据
external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

user = User(**external_data)

print(user.id)
#> 123
print(repr(user.signup_ts))

print(user.friends)
"""
{
    'id': 123,
    'name': 'John Doe',
    'signup_ts': datetime.datetime(2019, 6, 1, 12, 22),
    'tastes': {'wine': 9, 'cheese': 7, 'cabbage': 1},
}
"""
print(user)
print(user.model_dump())
print(user.model_dump_json())

