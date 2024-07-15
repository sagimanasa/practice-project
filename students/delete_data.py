# from mysql import connector
# connection=connector.commit(
#     host="localhost",
#     database="firstproject",
#     user="host",
#     password="Manasa@1232003"
# )
# cursorObj=connection.cursor()
# sql="Delete from students where id=%s"
# val=(2)
# cursorObj.execute(sql,val)
# connection.commit()
# print ("data deleted successfully")
from mysql import connector
connection=connector.connect(
    host="localhost",
    database="firstproject",
    user="host",
    password="Manasa@1232003"
)
cursorObj=connection.cursor()
sql="Delete from marks where id=%s"
val=(3)
cursorObj.execute(sql,val)
connection.commit()
print("data deleted successfully")

