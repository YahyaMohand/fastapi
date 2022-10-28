from fastapi import FastAPI,Query
from enum import Enum
app = FastAPI()

class ModelType(str,Enum):
	conv = "CNN"
	bid = "LSTM"
	gan = "GAN"

@app.get('/users/')
async def hello(page : int = Query(1,gt=0), size : int = 
Query(10,le=100)):
	return {'page': page, 'size':size}
