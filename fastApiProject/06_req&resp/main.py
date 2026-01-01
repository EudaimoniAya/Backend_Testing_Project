from fastapi import FastAPI
from apps.app01 import app1
from apps.app02 import app2
from apps.app03 import app3
from apps.app04 import app4
from apps.app05 import app5
from apps.app06 import app6
from apps.app07 import app7
import uvicorn

app = FastAPI()

app.include_router(app1, tags=["01 路径参数"])
app.include_router(app2, tags=["02 查询（请求）参数"])
app.include_router(app3, tags=["03 请求体数据"])
app.include_router(app4, tags=["04 form表单数据"])
app.include_router(app5, tags=["05 文件上传"])
app.include_router(app6, tags=["06 Request对象"])
app.include_router(app7, tags=["07 响应参数"])


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)