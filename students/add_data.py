# from mysql import connector
# connection=connector.connect(
#     host="localhost",
#     database="firstproject",
#     user="root",
#     password="Manasa@1232003"
# )
# cursorObj =connection.cursor()
# sql="INSERT INTO students(ID,NAME,AGE,GENDER)VALUES(%s,%s,%s,%s)"
# val=("1","manasa","21","F")
# cursorObj.execute(sql,val)
# connection.commit()
# print("row inserted")
from mysql import connector
connection=connector.connect(
    host="localhost",
    database="firstproject",
    user="root",
    password="Manasa@1232003"
)
cursorObj=connection.cursor()
sql="INSERT INTO marks(id,name,cls,maths,physics,chemistry,total)VALUES(%s,%s,%s,%s,%s,%s,%s)"
val=("1","manasa","10A",90,70,85,90+70+85)
cursorObj.execute(sql,val)
connection.commit()
print("row inserted")
