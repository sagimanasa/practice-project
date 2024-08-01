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

@app.delete("/student/{STD_ID}")
async def delete_student(STD_ID):
    studentdb.delete_student(STD_ID)
    return {"message":"sucess"}
@app.post("/student/{STD_ID}")
async def update_student(STD_ID,student:student):
    studentdb.update_student(STD_ID,student.NAME,student.AGE,student.GENDER)
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
@app.delete("/marks/{ID}")
async def delete_marks(ID):
    studentdb.delete_marks(ID)
    return {"message":"sucess"}
@app.post("/marks/{ID}")
async def update_marks(STD_ID,marks:marks):
    studentdb.update_marks(marks.ID,marks.SUBJECT,marks.MARKS,STD_ID)
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



