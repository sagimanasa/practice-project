import mysql.connector
connection=mysql.connector.connect(
host ="localhost",
user ="root",
password ="Manasa@1232003"
)
cursorObj=connection.cursor()
cursorObj.execute("CREATE DATABASE MySqlPythonDB")
print("DATABASE CREATED SUCCESSFULLY")
connection.close()

