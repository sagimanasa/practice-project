from mysql import connector
connection=connector.connect(
    host="localhost",
    database="firstproject",
    user="root",
    password="Manasa@1232003"
)
cursorObj=connection.cursor()
mysql ='''select * from employee'''
cursorObj.execute(mysql)
result = cursorObj.fetchmany(size =2)
print(result)
connection.close()
