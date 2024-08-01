from mysql import connector
class Database:
    def __init__(self):
        self.host="localhost"
        self.database="firstproject"
        self.user="root"
        self.password="Manasa@1232003"
    def create_connection(self):
        connection=connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return connection

    def create_student(self,STD_ID,NAME, AGE, GENDER):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "INSERT INTO student(STD_ID,NAME,AGE,GENDER)VALUES(%s,%s,%s,%s)"
        val = (STD_ID,NAME, AGE, GENDER)
        cursorObj.execute(query, val)
        conn.commit()
        print(cursorObj.rowcount, "data created successfully")

    def create_marks(self, STD_ID,ID,SUBJECT,MARKS):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "INSERT INTO marks(STD_ID,ID,SUBJECT,MARKS)VALUES(%s,%s,%s,%s)"
        val = (STD_ID,ID,SUBJECT,MARKS)
        cursorObj.execute(query, val)
        conn.commit()
        print(cursorObj.rowcount, "data created successfully")

    def read_students(self):
        arr = []
        conn = self.create_connection()
        cursorObj = conn.cursor()
        sql = "SELECT * FROM student"
        cursorObj.execute(sql)
        records = cursorObj.fetchall()
        for record in records:
            arr.append(record)
        conn.close()
        return arr

    def read_marks(self):
        arr = []
        conn = self.create_connection()
        cursorObj = conn.cursor()
        sql = "SELECT * FROM marks"
        cursorObj.execute(sql)
        records = cursorObj.fetchall()
        for record in records:
            arr.append(record)
        conn.close()
        return arr

    def update_student(self, STD_ID, NAME, AGE, GENDER):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "UPDATE student SET AGE=%s,NAME=%s,GENDER=%s WHERE STD_ID=%s"
        values = (AGE, NAME, GENDER, STD_ID)
        cursorObj.execute(query, values)
        conn.commit()
        print("data updated successfully")

    def update_marks(self, STD_ID,ID,SUBJECT,MARKS):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "UPDATE student SET ID=%s,SUBJECT=%s,MARKS=%s WHERE STD_ID=%s"
        values = (ID, SUBJECT, MARKS, STD_ID)
        cursorObj.execute(query, values)
        conn.commit()
        print("data updated successfully")

    def delete_student(self, STD_ID):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "DELETE FROM student WHERE STD_ID=%s"
        values = (STD_ID,)
        cursorObj.execute(query, values)
        conn.commit()
        print("data deleted successfully")

    def delete_marks(self, ID):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "DELETE FROM marks WHERE ID=%s"
        values = (ID,)
        cursorObj.execute(query, values)
        conn.commit()
        print("data deleted successfully")
studentdb=Database()
#studentdb.create_student(2,"honey",14,"F")
#studentdb.create_marks(2,2,"maths",75)
#studentdb.read_student()
#studentdb.create_marks(2,3,"maths",70)
