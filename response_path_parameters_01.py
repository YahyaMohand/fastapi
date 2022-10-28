from turtle import title
from fastapi import FastAPI,Body,status,Response
from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Post(BaseModel) :
    title : str
    nb_views : int


class PublicModel(BaseModel):
    title : str
app = FastAPI()

# @app.post('/post', status_code=status.HTTP_201_CREATED)
# async def state(post : Post):
#     return post


# Dummy database
posts = {
1: Post(title="Hello", nb_views=100),
}
# @app.get('/post/{id}' , response_model = PublicModel)
# async def get_id(id : int):
#     return posts[id]


@app.put('/posts/{id}')
async def update_post(id : int , post : Post, response : Response):
    if id not in posts:
        response.status_code = status.HTTP_404_CREATED
    posts[id] = post
    return posts[id]