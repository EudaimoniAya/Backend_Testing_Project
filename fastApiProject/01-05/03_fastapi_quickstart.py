from fastapi import FastAPI
import uvicorn

# FastAPI类实例化出的app对象，就是进行路由映射的根本对象
app = FastAPI()


@app.get("/")
async def home():
    return {"user_id": 1001}


@app.get("/shop")  # 路径操作装饰器
async def shop():  # 路径操作函数
    return {"shop": "商品信息"}


# 如果不想在终端用命令：uvicorn 03_fastapi_quickstart:apps --reload 那么可以用如下方法
if __name__ == '__main__':
    uvicorn.run("03_fastapi_quickstart:apps",
                host='127.0.0.1',
                port=8080,
                reload=True)
