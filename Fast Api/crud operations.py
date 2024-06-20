from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from uuid import UUID,uuid4

app= FastAPI()

class Task(BaseModel):
  id:Optional[UUID]=None
  title:str
  description:Optional[str]=None
  completed :bool=False

task=[]



@app.post("/create-new",response_model=Task)
def postNew(task:Task):
  task.id=uuid4(task)
  task.append
  return task

@app.get("/",response_model=List(Task))
def getFunc():
  return task
