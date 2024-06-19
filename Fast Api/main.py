from fastapi import FastAPI ,Path
from pydantic import BaseModel
from  typing  import  Optional

app = FastAPI() 

student ={
  1:{
    "name" : "eshwar",
    "age"  : 25,
    "profession" : "software development"
  }
}

class Student(BaseModel):
  name:str
  age:int
  profession:str

class students(BaseModel):
   name: Optional[str] = None
   age: Optional[int] = None
   profession :Optional[str] = None

@app.get("/")
def index():
  return{"name" : "first data"}

@app.get("/get-student/{student_id}")
def getStudent(student_id:int = Path(... ,description="enter the student id to retrive information")):
  return student[student_id]

@app.get("/get-by-name")
def getByName(name:str):
  for st in student:
    if student[st]["name"]==name:
      return student[st]
  return{"data":"not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student_data: Student):
    if student_id in student:
        raise HTTPException(status_code=400, detail="Student already exists")
    student[student_id] = student_data.dict()
    return student[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student_data: students):
    if student_id not in student:
        raise HTTPException(status_code=404, detail="Student not available to update")
    
    updated_data = student[student_id]

    if student_data.name is not None:
        updated_data["name"] = student_data.name
    if student_data.age is not None:
        updated_data["age"] = student_data.age
    if student_data.profession is not None:
        updated_data["profession"] = student_data.profession

    student[student_id] = updated_data
    return student[student_id]

app.delete("/delete-student/{student_id}")
def deleteStudent(student_id:int):
   if student_id not in student:
      raise HTTPException(status_code=404, detail="Student not available to delete")
   del student[student_id]
   return("student record deleted successfully")
      