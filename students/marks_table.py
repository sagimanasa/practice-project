from mysql import connector
class marks:
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
    def create_record(self,id,name,cls,maths,physics,chemistry,total):
        conn=self.create_connection()
        cursorObj=conn.cursor()
        sql="INSERT into marks(id,name,cls,maths,physics,chemistry,total)VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val=(id,name,cls,maths,physics,chemistry,total)
        cursorObj.execute(sql,val)
        conn.commit()
        print("row created successfully")
    def read_record(self):
        arr=[]
        conn=self.create_connection()
        cursorObj=conn.cursor()
        sql="SELECT * from marks"
        cursorObj.execute(sql)
        records=cursorObj.fetchall()
        for record in records:
            arr.append(record)
        conn.close()
        return arr
    def update_record(self,id,name,cls,maths,physics,chemistry,total):
        conn=self.create_connection()
        cursorObj=conn.cursor()
        sql="UPDATE marks set name=%s,cls=%s,maths=%s,physics=%s,chemistry=%s,total=%s WHERE id=%s"
        val=(name,cls,maths,physics,chemistry,total,id)
        cursorObj.execute(sql,val)
        conn.commit()
        print("data updated successfully")
    def delete_record(self,id):
        conn=self.create_connection()
        cursorObj=conn.cursor()
        sql="DELETE from marks WHERE id=%s"
        val=(id,)
        cursorObj.execute(sql,val)
        conn.commit()
        print("data deleted successfully")
db=marks()
# db.create_record(2,"honey","10B",80,85,86,80+85+86)
# db.create_record(3,"mamatha","10c",75,80,86,75+80+86)
# print(db.read_record())
# db.update_record(2,"hasmitha","10B",85,80,82,85+80+82)
# print(db.read_record())
db.delete_record(3)
print(db.read_record())

