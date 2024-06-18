from fastapi import FastAPI ,Path

app = FastAPI() 

student ={
  1:{
    "name" : "eshwar",
    "age"  : 25,
    "profession" : "software development"
  }
}

@app.get("/")
def index():
  return{"name" : "first data"}

@app.get("/get-student/{student_id}")
def getStudent(student_id:int = Path(... ,description="enter the student id to retrive information")):
  return student[student_id]
