from typing import Dict,Optional, Tuple
from fastapi import FastAPI, Depends,HTTPException, status,Query
from pydantic import BaseModel


app = FastAPI()

class Pagenation:
    def __init__(self, maximun_limit : int = 100 ) -> None:
        self.maximum_limit = maximun_limit

    async def __call__(self, skip: int = Query(0 , ge=0), limit: int = Query(10, ge=0)) -> Tuple[int,int]:
        capped_limit = min(self.maximum_limit,limit)
        return(skip, capped_limit)

pagination = Pagenation(maximun_limit=90)
@app.get('/item')
async def page(p : Tuple[int,int] = Depends(pagination)):
    skip , limit = p
    return {"skip" : skip, "limit" : limit}
    
        