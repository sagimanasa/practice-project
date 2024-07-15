from mysql import connector
connection=connector.connect(
    host="localhost",
    database="firstproject",
    user="root",
    password="Manasa@1232003"
)
cursorObj =connection.cursor()
#to delete data from table
# sql="DELETE FROM students WHERE std_id= 5"
# cursorObj.execute(sql)
# connection.commit()
# print("row deleted")
#to update data in table
# sql="UPDATE students SET std_id=3 WHERE std_id=6"
# cursorObj.execute(sql)
# connection.commit()
# print("row updated")
#to read the data in table
cursorObj.execute("SELECT * FROM students")
result=cursorObj.fetchall()
for x in result:
    print(x)




