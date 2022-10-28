from fastapi import FastAPI,Body,Form,UploadFile,File,Header,Cookie,Request
from pydantic import BaseModel
from typing import Optional
from enum import Enum


app = FastAPI()

@app.get("/")
async def get_header(user_agent: str = Header(...)):
    return {"user_agent": user_agent}



# @app.get("/")
# async def get_cookie(hello: Optional[str] = Cookie(None)):
#     return {"hello": hello}

@app.get('/req')
async def get_request(request : Request):
    return {'request' : request.url.path}