from typing import Annotated

from fastapi import FastAPI, Depends

app = FastAPI()


class Logger:
    def log(self, message: str):
        print(f"Logging message: {message}")


# 依赖注入
def get_logger():
    return Logger()


logger_dependency = Annotated[Logger, Depends(get_logger)]


@app.get("/log/{message}")
def log_message(message: str, logger: logger_dependency):
    # 这里的Depends表示需要一个依赖项来运行这个应用
    logger.log(message)
    return message


# 反例
@app.get("/log/{message}")
def log_message(message: str):
    logger = Logger()
    logger.log(message)
    return message
