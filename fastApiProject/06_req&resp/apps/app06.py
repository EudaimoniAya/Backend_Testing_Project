from fastapi import APIRouter, Request

app6 = APIRouter()


@app6.post("/items")
async def items(request: Request):
    print("url:", request.url)
    print("客户端IP地址:", request.client.host)
    print("客户端浏览器信息:", request.headers.get("user-agent"))
    print("cookies:", request.cookies)
    return {
        "url:": request.url,
        "客户端IP地址:": request.client.host,
        "客户端浏览器信息:": request.headers.get("user-agent")
    }