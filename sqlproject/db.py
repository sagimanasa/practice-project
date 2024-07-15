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
    def create_record(self,  name, age, gender):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query="INSERT INTO users(name,age,gender)VALUES(%s,%s,%s)"
        val=(name,age,gender)
        cursorObj.execute(query,val)
        conn.commit()
        print(cursorObj.rowcount,"data created successfully")
    def read_records(self):
        arr=[]
        conn=self.create_connection()
        cursorObj = conn.cursor()
        sql="SELECT * FROM users"
        cursorObj.execute(sql)
        records=cursorObj.fetchall()
        for record in records:
            arr.append(record)
        conn.close()
        return arr
    def update_record(self,id,name,age,gender):
        conn=self.create_connection()
        cursorObj = conn.cursor()
        query="UPDATE users SET age=%s,name=%s,gender=%s WHERE id=%s"
        values=(age,name,gender,id)
        cursorObj.execute(query,values)
        conn.commit()
        print("data updated successfully")
    def delete_record(self,id):
        conn = self.create_connection()
        cursorObj = conn.cursor()
        query = "DELETE FROM users WHERE id=%s"
        values = (id,)
        cursorObj.execute(query,values)
        conn.commit()
        print("data deleted successfully")
# db=Database()
# db.create_record(3,"manu",22,"F")
# print(db.read_records())
# db.update_record("2",21)
# db.read_records()
# db.delete_table("3")
# print(db.read_records())
