# web应用程序：遵循http协议
import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 8080))
sock.listen(5)

while 1:
    # 阻塞等待客户端连接，conn指连接到客户端的套接字，addr指连接到客户端的远程地址
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("客户端发送的请求信息:\n", data)
    """
    客户端发送的请求信息:
    b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\nsec-ch-ua: "Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br, zstd\r\nAccept-Language: zh-CN,zh;q=0.9\r\nCookie: ajs_anonymous_id=85a2e559-2c31-4ae7-8cdd-941f4ad4f7c1; username-localhost-8888="2|1:0|10:1763534436|23:username-localhost-8888|204:eyJ1c2VybmFtZSI6ICI0NTg0MDMwMmM4NGU0NjRkOWQyMmM4Zjc1MzFkODljZiIsICJuYW1lIjogIkFub255bW91cyBQcmF4aWRpa2UiLCAiZGlzcGxheV9uYW1lIjogIkFub255bW91cyBQcmF4aWRpa2UiLCAiaW5pdGlhbHMiOiAiQVAiLCAiY29sb3IiOiBudWxsfQ==|a094ca0e06fd035438'
    => 地址栏输入url是一种GET请求
    """

    # conn.send(b"hello world")   # 不按http响应协议的格式发送，会导致客户端访问时出现响应无效的错误
    # conn.send(b"HTTP/1.1 200 ok\r\nserver:aya\r\n\r\nhello world")  # 不包含content-type，返回的是空网页

    # 法一：
    body = b"hello world"
    conn.send(b"HTTP/1.1 200 OK\r\n"
              b"Server: aya\r\n"
              b"Content-Type: text/html; charset=utf-8\r\n"
              b"Content-Length: " + str(len(body)).encode() + b"\r\n"   # 如果不包含Content-Length那么只会显示空白网页
              b"\r\n" + body)
    # 法二：
    # body = "hello world (from socket server!)"
    # response = (f"HTTP/1.1 200 OK\r\n"
    #             f"Server: aya\r\n"
    #             f"Content-Type: text/html; charset=utf-8\r\n"
    #             f"Content-Length: {len(body)}\r\n"
    #             f"\r\n"
    #             f"{body}")
    #
    # conn.send(response.encode('utf-8'))
    conn.close()

