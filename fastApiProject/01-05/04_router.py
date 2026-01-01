from fastapi import FastAPI
import uvicorn

# FastAPI类实例化出的app对象，就是进行路由映射的根本对象
app = FastAPI()


# summary会在fastapi文档中的接口概览界面中显示，而description会在点开的详情栏中显示
# response_description会在文档详情栏中的响应部分的description中显示
@app.get("/get", tags=["这是一个默认的测试接口"],
         summary="this is items测试 summary",
         description="this is items测试的详情内容",
         response_description="这是items响应的介绍")
async def get_test():
    return {"method": "get方法"}


# 添加了tag的会在fastapi文档中分一个类，同tag的会分到同一类
# 所以文档中一个接口可以多次出现
@app.post("/items", tags=["这是一个items的测试接口", "这是一个默认的测试接口"])
async def item_test():
    return {"items": "items数据"}


@app.put("/items", tags=["这是一个items的测试接口"], deprecated=True)
async def put_test():
    return {"method": "put方法"}


@app.delete("/delete", tags=["这是一个默认的测试接口"])
async def delete_test():
    return {"method": "delete方法"}


if __name__ == '__main__':
    uvicorn.run("04_router:apps", host='127.0.0.1', port=8080, reload=True)
