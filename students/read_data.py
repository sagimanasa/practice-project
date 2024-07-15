# from mysql import connector
# connection=connector.connect(
#     host="localhost",
#     database="firstproject",
#     user="root",
#     password="Manasa@1232003"
# )
# cursorObj=connection.cursor()
# sql="SELECT * from students"
# cursorObj.execute(sql)
# for record in cursorObj.fetchall():
#     print(record)
from mysql import connector
connection=connector.connect(
    host="localhost",
    database="firstproject",
    user="root",
    password="Manasa@1232003"
)
cursorObj=connection.cursor()
sql="SELECT * from marks"
cursorObj.execute(sql)
for record in cursorObj.fetchall():
    print(record)
