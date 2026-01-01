from fastapi import APIRouter
from typing import Union, Optional

app2 = APIRouter()


# 对应的路径?参数：http://localhost:8080/jobs?language=Python&school=NEU&experience=0
@app2.get("/jobs")
async def get_jobs(
        language: str,
        school: Union[str, None] = None,
        experience: Optional[str] = None):
    # 基于language、school、experience进行数据库查询，另外给了默认值那么该参数就是可填可不填
    # Union是要求数据应该是某几种类型，但需手动默认值，即school: Union[str, None]仍是必填字段
    # Optional是Union的一个简化，当str数据类型中有可能是None时，则用Optional[str]，相当于Union[str, None]
    return {
        "language": language,
        "school": school,
        "experience": experience,
    }
