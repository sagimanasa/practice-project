import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    database="firstproject",
    user="root",
    password="Manasa@1232003"
)
cursorObj=connection.cursor()
sql='''CREATE TABLE students(
         std_id INT NOT NULL,
         std_name VARCHAR(20) NOT NULL,
    PRIMARY KEY(std_id)
    )'''
cursorObj.execute(sql)
print("TABLE CREATED SUCCESSFULLY")
connection.close()
