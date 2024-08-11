from fastapi import FastAPI
from pydantic import BaseModel
from studentdb import Database
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
studentdb=Database()
class Student(BaseModel):
    name:str
    age:int
    gender:str
@app.delete("/student/{std_id}")
async def delete_student(std_id):
    studentdb.delete_marks_std_id(std_id)
    studentdb.delete_student(std_id)
    return {"message":"sucess"}
@app.post("/student/{std_id}")
async def update_student(std_id,student:Student):
    studentdb.update_student(std_id,student.name,student.age,student.gender)
    return {"message":"sucess"}
@app.put("/student")
async def create_student(student:Student):
    studentdb.create_student(student.name,student.age,student.gender)
    return {"message":"sucess"}
@app.get("/student")
async def read_students():
    studentList=studentdb.read_students()
    arr=[]
    for student in studentList:
        arr.append({"std_id":student[0],"name":student[1],"age":student[2],"gender":student[3]})
    return {"records":arr}

class Marks(BaseModel):

    id:int
    subject:str
    marks:int

@app.delete("/marks/marks_id/{marks_id}")
async def delete_marks_id(marks_id):
    studentdb.delete_marks_id(marks_id)
    return {"message":"sucess"}
@app.delete("/marks/student_id/{student_id}")
async def delete_marks_std_id(student_id):
    studentdb.delete_marks_std_id(student_id)
    return {"message":"success"}
@app.post("/marks/{marks_id}")
async def update_marks(marks_id,marks:Marks):
    studentdb.update_marks(marks_id,marks.marks,marks.subject)
    return {"message":"sucess"}
@app.put("/marks/student_id/{student_id}")
async def create_marks(student_id,marks:Marks):
    studentdb.create_marks(student_id,marks.id,marks.subject,marks.marks)
    return {"message":"sucess"}
@app.get("/marks")
async def read_marks():
    marksList=studentdb.read_marks()
    arr=[]
    for marks in marksList:
        arr.append({"std_id":marks[0],"id":marks[1],"subject":marks[2],"marks":marks[3]})
    return {"records":arr}

@app.get("/marks/student_id/{student_id}")
async def read_marks_student(student_id):
    marksList = studentdb.read_marks_student(student_id)
    arr = []
    for marks in marksList:
        arr.append({"std_id": marks[0], "id": marks[1], "subject": marks[2], "marks": marks[3]})
    return {"records": arr}

