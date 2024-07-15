import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Manasa@1232003"
)
cursorObj=connection.cursor()
cursorObj.execute("Drop DATABASE MySqlPythonDB")
print("DATABASE DROPPED SUCCESSFULLY")
connection.close()
