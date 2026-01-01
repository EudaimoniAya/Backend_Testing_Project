import os.path

from fastapi import APIRouter, UploadFile
from typing import Union, Optional
from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import List

from fastapi import Form, File

app5 = APIRouter()


@app5.post("/file")
async def get_file(file: bytes = File()):
    print("file", file)
    return {
        "file": "file"
    }


# 上传多个文件
@app5.post("/files")
async def get_files(files: List[bytes] = File()):
    for file in files:
        print(len(file))
    return {
        "files": len(files)
    }


@app5.post("/uploadFile")
async def upload_file(file: UploadFile):
    print("file", file)
    upload_dir = "imgs"
    os.makedirs(upload_dir, exist_ok=True)

    path = os.path.join(upload_dir, file.filename)
    # 文件保存
    with open(path, "wb") as f:
        for line in file.file:
            f.write(line)

    return {
        "file": file.filename
    }


@app5.post("/uploadFiles")
async def upload_files(files: List[UploadFile]):
    print("files", files)

    upload_dir = "uploadFiles"
    os.makedirs(upload_dir, exist_ok=True)

    for file in files:
        # print("file.filename:", file.filename)
        path = os.path.join(upload_dir, file.filename)
        # 文件保存
        with open(path, "wb") as f:
            for line in file.file:
                f.write(line)

    return {
        "names": [file.filename for file in files]
    }
