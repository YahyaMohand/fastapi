from fastapi import FastAPI,Body,status,Response,HTTPException,File
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Post(BaseModel) :
    title : str
    nb_views : int


class PublicModel(BaseModel):
    title : str
app = FastAPI()

@app.post('/password')
async def check_password(password : str = File(...) , confirm_pass : str = File(...)):
    if password != confirm_pass:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Passwords don't match.",
        )
    return {'password matched'}