from mysql import connector
connection=connector.connect(
    host="localhost",
    database="firstproject",
    user="root",
    password="Manasa@1232003"
)
cursorObj=connection.cursor()
sql="INSERT INTO users(id,name,age,gender)VALUES(%s,%s,%s,%s)"
val=(6,"Hasmitha",15,"F")
cursorObj.execute(sql,val)
connection.commit()
print("data inserted successfully")
