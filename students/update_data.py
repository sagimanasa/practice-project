# from mysql import connector
# connection=connector.connect(
#     host="localhost",
#     database="firstproject",
#     user="root",
#     password="Manasa@1232003"
# )
# cursorObj=connection.cursor()
# sql="UPDATE students SET AGE=15 WHERE ID=3"
# cursorObj.execute(sql)
# connection.commit()
# print("data updated successfully")
from mysql import connector
connection=connector.connect(
    host = "localhost",
    database = "firstproject",
    user = "root",
    password = "Manasa@1232003"
)
cursorObj = connection.cursor()
sql = "UPDATE marks set name=%s,cls=%s,maths=%s,physics=%s,chemistry=%s,total=%s WHERE id=%s"
val = (2, "hasmitha", "10B", 85, 80, 82, 85+80+82, id)
cursorObj.execute(sql, val)
connection.commit()
print("data updated successfully")
