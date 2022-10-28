from fastapi import FastAPI,Body,Form,UploadFile,File
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class User(BaseModel):
        name : str
        age : int

class Company(BaseModel):
        name : str

# @app.post('/users/')
# async def create_user(user:User, company:Company):
#         return {'user':user, 'company':company}

# @app.post('/users')
# async def create_user(user:User , prior : int = Body(...,ge=9)):
#         return {'user': user , 'prior':prior}

@app.get('/')
async def hello_world():
        return 'Hello_World'

@app.post('/users')
async def create_user(name: str = Form(...) , age : int = Form(...)):
        return {'name' : name, 'age' : age}


@app.post('/upload')
async def upload(files : list[UploadFile] = File(...)):
        return [ 
                {'file_name' : file.filename , "content_type": file.content_type}
                for file in files
        ]