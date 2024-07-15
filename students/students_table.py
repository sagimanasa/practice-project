from mysql import connector
class students:
    def __init__(self):
        self.host = "localhost"
        self.database = "firstproject"
        self.user = "root"
        self.password = "Manasa@1232003"
    def create_connection(self):
        connection = connector.connect(
            host = self.host,
            database = self.database,
            user = self.user,
            password = self.password
        )
        return connection
    def create_record(self, ID, NAME, AGE, GENDER):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "INSERT INTO students(ID ,NAME, AGE, GENDER)VALUES(%s,%s,%s,%s)"
        val = (ID, NAME, AGE, GENDER)
        cursorObj.execute(query,val)
        conn.commit()
        print(cursorObj.rowcount, "data created successfully")
    def read_record(self):
        arr = []
        conn = self.create_connection()
        cursorObj = conn.cursor()
        sql = "SELECT * FROM students"
        cursorObj.execute(sql)
        records = cursorObj.fetchall()
        for record in records:
            arr.append(record)
        conn.close()
        return arr
    def update_record(self, ID ,NAME, AGE, GENDER):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "UPDATE students SET AGE=%s,NAME=%s,GENDER=%s WHERE ID=%s"
        values = (AGE, NAME, GENDER, ID)
        cursorObj.execute(query, values)
        conn.commit()
        print("data updated successfully")
    def delete_record(self, ID):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "DELETE FROM students WHERE ID=%s"
        values = (ID,)
        cursorObj.execute(query, values)
        conn.commit()
        print("data deleted successfully")
db = students()
# db.create_record(3, "hasmitha", 16, "F")
# print(db.read_record())
# db.update_record(1, "manasa", 22, "F")
# print(db.read_record())
# db.delete_record("2")
print(db.read_record())
