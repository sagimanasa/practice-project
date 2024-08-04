from fastapi import FastAPI
from pydantic import BaseModel
from studentdb import Database
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
studentdb=Database()
class student(BaseModel):
    STD_ID:int
    NAME:str
    AGE:int
    GENDER:str
@app.delete("/student/{std_id}")
async def delete_student(std_id):
    studentdb.delete_marks_std_id(std_id)
    studentdb.delete_student(std_id)
    return {"message":"sucess"}
@app.post("/student/{std_id}")
async def update_student(std_id,student:student):
    studentdb.update_student(std_id,student.NAME,student.AGE,student.GENDER)
    return {"message":"sucess"}
@app.put("/student")
async def create_student(student:student):
    studentdb.create_student(student.STD_ID,student.NAME,student.AGE,student.GENDER)
    return {"message":"sucess"}
@app.get("/student")
async def read_students():
    studentlist=studentdb.read_students()
    arr=[]
    for student in studentlist:
        arr.append({"STD_ID":student[0],"NAME":student[1],"AGE":student[2],"GENDER":student[3]})
    return {"records":arr}

class marks(BaseModel):
    STD_ID:int
    ID:int
    SUBJECT:str
    MARKS:int

@app.delete("/marks/marks_id/{marks_id}")
async def delete_marks_id(marks_id):
    studentdb.delete_marks_id(marks_id)
    return {"message":"sucess"}
@app.delete("/marks/student_id/{student_id}")
async def delete_marks_std_id(student_id):
    studentdb.delete_marks_std_id(student_id)
    return {"message":"success"}
@app.post("/marks/{marks_id}")
async def update_marks(marks_id,marks:marks):
    studentdb.update_marks(marks_id,marks.MARKS,marks.SUBJECT)
    return {"message":"sucess"}
@app.put("/marks")
async def create_marks(marks:marks):
    studentdb.create_marks(marks.STD_ID,marks.ID,marks.SUBJECT,marks.MARKS)
    return {"message":"sucess"}
@app.get("/marks")
async def read_marks():
    markslist=studentdb.read_marks()
    arr=[]
    for marks in markslist:
        arr.append({"STD_ID":marks[0],"ID":marks[1],"SUBJECT":marks[2],"MARKS":marks[3]})
    return {"records":arr}



