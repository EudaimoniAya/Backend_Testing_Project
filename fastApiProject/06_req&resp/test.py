# 假设这是FastAPI的简化版File类
class File:
    def __init__(self, default=..., description=None):
        self.default = default
        self.description = description

# 模拟一个端点函数
async def upload_file(file: bytes = File()):
    # 在函数内部，我们期望file是bytes类型，而不是File实例
    return len(file)

# 模拟FastAPI分析函数签名
import inspect

def analyze_function(func):
    sig = inspect.signature(func)
    for param in sig.parameters.values():
        # 获取默认值
        default = param.default
        # 检查默认值是否是File实例
        if isinstance(default, File):
            print(f"参数 {param.name} 是一个文件参数，类型注解为 {param.annotation}")
            # 在这里，FastAPI会记录：这个参数需要从请求中提取文件
            # 并且类型是bytes（因为类型注解是bytes）
        else:
            print(f"参数 {param.name} 是一个普通参数，默认值为 {default}")

# 模拟请求处理
async def handle_request(func, request):
    # 假设request中有文件数据
    # 根据之前分析的结果，我们知道upload_file函数的file参数需要从request中提取文件
    # 所以我们会提取文件数据，然后调用func，传入提取的数据
    file_data = await extract_file_from_request(request, "file")
    return await func(file_data)

async def extract_file_from_request(request, param_name):
    # 模拟从请求中提取文件数据，返回bytes
    return b"fake file content"

# 分析函数
analyze_function(upload_file)

# 模拟处理请求
async def main():
    class Request:
        pass
    request = Request()
    result = await handle_request(upload_file, request)
    print(f"函数执行结果: {result}")

import asyncio
asyncio.run(main())