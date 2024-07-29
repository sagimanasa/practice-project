# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/student")
# async def root():
#     return{'message':"helloworld"}
# @app.post("/items")
# def create_item(name:str,price:int):
#     return{"name":name,"price":price}
# from fastapi import FastAPI
# from pydantic import BaseModel
# class item(BaseModel):
#     name:str
#     description:str=None
#     price:float
#     tax:float=None
# app=FastAPI()
# @app.post("/user/{user_id}")
# async def create_item(item:item):
#     item_dict=item.dict()
#     if item.tax:
#         price_with_tax=item.price+item.tax
#         item_dict.update({"price_with_tax":price_with_tax})
#     return item_dict

# from fastapi import FastAPI
# from pydantic import BaseModel
# from db import Database
# from fastapi.staticfiles import StaticFiles
# app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
# db=Database()
# class User(BaseModel):
#     name:str
#     age:int
#     gender:str
# @app.delete("/users/{id}")
# async def delete_record(id):
#     db.delete_record(id)
#
#     return {"message":"sucess"}
# @app.post("/users/{id}")
# async def update_record(id,user:User):
#     db.update_record(id,user.name,user.age,user.gender)
#
#     return {"message":"sucess"}
# @app.put("/users")
# async def create_record(user:User):
#     db.create_record(user.name,user.age,user.gender)
#
#     return {"message":"sucess"}
#
# @app.get("/users")
# async def read_records():
#     userlist=db.read_records()
#     arr=[]
#     for user in userlist:
#         arr.append({"id":user[0],"name":user[1],"age":user[2],"gender":user[3]})
#     return {"records":arr}

from fastapi import FastAPI
from pydantic import BaseModel
from db import Database
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
studentdb=Database()
class student(BaseModel):
    STD_ID:int
    NAME:str
    AGE:int
    GENDER:str
class marks(BaseModel):
    STD_ID:int
    ID:int
    SUBJECT:str
    MARKS:int
@app.delete("/student/{STD_ID}")
async def delete_record(STD_ID):
    studentdb.delete_record(STD_ID)

    return {"message":"sucess"}
@app.post("/student/{STD_ID}")
async def update_record(STD_ID,student:student):
    studentdb.update_record(STD_ID,student.NAME,student.AGE,student.GENDER)

    return {"message":"sucess"}
@app.put("/student")
async def create_record(student:student):
    studentdb.create_record(student.NAME,student.AGE,student.GENDER)

    return {"message":"sucess"}

@app.get("/student")
async def read_records():
    studentlist=studentdb.read_records()
    arr=[]
    for student in studentlist:
        arr.append({"STD_ID":student[0],"NAME":student[1],"AGE":student[2],"GENDER":student[3]})
    return {"records":arr}

@app.delete("/student/{ID}")
async def delete_record(ID):
    studentdb.delete_record(ID)
    return {"message":"sucess"}
@app.post("/marks/{ID}")
async def update_record(STD_ID,marks:marks):
    studentdb.update_record(STD_ID,marks.ID,marks.SUBJECT,marks.MARKS)
    return {"message":"sucess"}
@app.put("/marks")
async def create_record(STD_ID,marks:marks):
    studentdb.create_record(STD_ID,marks.ID,marks.SUBJECT,marks.MARKS)
    return {"message":"sucess"}
@app.get("/marks")
async def read_records():
    markslist=studentdb.read_records()
    arr=[]
    for marks in markslist:
        arr.append({"STD_ID":marks[0],"SUBJECT":marks[2],"MARKS":marks[3]})
    return {"records":arr}


