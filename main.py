from fastapi import FastAPI, Path
from enum import Enum

class modelType(str,Enum):
	alexnet = 'alexnet'
	resnet = 'resnet'
	lenet = 'lenet'
	
app = FastAPI()

@app.get('/users/{type}/')
async def hello(type:modelType):
	if type == modelType.alexnet:
		return {"type": type, "message": "Deep Learning FTW!"}
	if type == modelType.resnet:
		return {'type': type, "message": "resnet resduial"}
	return {"anythings" : "ok"} 
	
