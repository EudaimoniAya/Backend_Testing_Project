import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import Response
import time
app = FastAPI()


@app.middleware('http')
async def m2(request: Request, call_next):
    # 请求代码块
    print("m2 request")
    response = await call_next(request)
    # 响应代码块
    response.headers['author'] = 'eudaimoniAya'
    print("m2 response")
    return response


@app.middleware('http')
async def m1(request: Request, call_next):
    # 请求代码块
    print("m1 request")
    # if request.client.host in ["127.0.0.1",]:   # 黑名单
    #     return Response(content="visit forbidden")

    # if request.url.path in ["/user"]:
    #     return Response(content="visit forbidden")

    start_time = time.time()

    response = await call_next(request)
    # 响应代码块
    print("m1 response")
    end_time = time.time()
    response.headers['time_process'] = str(end_time - start_time)
    print("m1 time cost: {}".format(end_time - start_time))
    return response


@app.get("/user")
async def get_user():
    print("get_user函数执行")
    return {
        "user": "current user"
    }

@app.get("/item/{item _id}")
def get_item(item_id: int):
    print("get_item函数执行")
    return {
        "item_id": item_id
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True, workers=1)
