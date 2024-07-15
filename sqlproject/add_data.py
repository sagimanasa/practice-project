from mysql import connector
connection=connector.connect(
    host="localhost",
    database="firstproject",
    user="root",
    password="Manasa@1232003"
)
cursorObj =connection.cursor()
sql="INSERT INTO students(std_id,std_name)VALUES(%s,%s)"
val=("6","hasmitha")
cursorObj.execute(sql,val)
connection.commit()
print("row inserted")
