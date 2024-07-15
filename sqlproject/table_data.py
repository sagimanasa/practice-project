import mysql.connector
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        database="firstproject",
        user="root",
        password="Manasa@1232003"
    )
    return connection
# def create_table(connection):
#     cursor = connection.cursor()
#     sql = '''CREATE TABLE users(
#                id=INT NOT NULL
#                name= VARCHAR(20) NOT NULL,
#                age= INT NOT NULL,
#                gender=CHAR(1) NOT NULL,
#              PRIMARY KEY(id)
#           )'''
#     cursor.execute(sql)
#     print("table created successfully")
#     connection.close()
def create_record(connection):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users(id,name,age,gender)VALUES(5,'manasa',22,'female')")
    connection.commit()
    print("record created successfully")
def read_record(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * from users")
    for record in cursor.fetchall():
        print(record)
def update_record(connection):
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET age=21 WHERE id=1")
    connection.commit()
    print("record updated successfully")
def delete_record(connection):
    cursor = connection.cursor
    cursor.execute("DELETE FROM users WHERE id=1")
    connection.commit()
    print("record deleted successfully")
conn = create_connection()

