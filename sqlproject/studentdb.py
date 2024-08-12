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

    def create_student(self,name, age, gender):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "INSERT INTO student(name,age,gender)VALUES(%s,%s,%s)"
        val = (name,age,gender)
        cursorObj.execute(query, val)
        conn.commit()
        print(cursorObj.rowcount, "data created successfully")

    def create_marks(self,std_id,id,subject,marks):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "INSERT INTO marks(std_id,id,subject,marks)VALUES(%s,%s,%s,%s)"
        val = (std_id,id,subject,marks)
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

    def read_marks_student(self, std_id):
        arr = []
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "SELECT * FROM marks WHERE std_id = %s"
        cursorObj.execute(query, (std_id,))
        records = cursorObj.fetchall()

        for record in records:
            arr.append(record)
        return arr


    def update_student(self, std_id,name,age,gender):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "UPDATE student SET age=%s,name=%s,gender=%s WHERE std_id=%s"
        values = (age, name, gender, std_id)
        cursorObj.execute(query, values)
        conn.commit()
        print("data updated successfully")

    def update_marks(self, id,marks,subject):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "UPDATE marks SET marks=%s,subject=%s WHERE id=%s"
        values = (marks,subject,id)
        cursorObj.execute(query, values)
        conn.commit()
        print("data updated successfully")

    def delete_student(self, std_id):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "DELETE from student WHERE std_id=%s"
        values = (int(std_id),)
        cursorObj.execute(query, values)
        conn.commit()
        print("data deleted successfully")

    def delete_marks_id(self, id):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "DELETE FROM marks WHERE id=%s"
        values = (id,)
        cursorObj.execute(query, values)
        conn.commit()
        print("data deleted successfully")
    def delete_marks_std_id(self,std_id):
        conn=self.create_connection()
        cursorObj=conn.cursor()
        query="DELETE FROM marks WHERE std_id=%s"
        values=(int(std_id),)
        cursorObj.execute(query,values)
        conn.commit()
        print("data deleted successfully")
studentdb=Database()
#studentdb.create_student(2,"honey",14,"F")
#studentdb.create_marks(2,2,"maths",75)
#studentdb.read_student()
#studentdb.create_marks(2,3,"maths",70)
