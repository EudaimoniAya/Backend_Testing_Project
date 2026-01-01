import uvicorn
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# @app.middleware('http')
# async def CORSMiddleware(request: Request, call_next):
#     # 不需要请求处理
#     response = await call_next(request)
#     # 响应代码块
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response


@app.get("/user")
def get_user():
    print("user: aya")
    return {"user": "current user"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True, workers=1)
