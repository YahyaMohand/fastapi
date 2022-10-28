from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader

API_TOKEN = "123123"

app = FastAPI()
api_key_header = APIKeyHeader(name="Token")


@app.get("/protected-route")
async def protected_route(token : str = Depends(api_key_header)):
    if token != API_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return {"hello" : "world"}


    