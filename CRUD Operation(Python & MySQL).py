#----------------------crud opetation--------------------------------------------
#Requrements:
1. MySQL
2. Python
3. MySQL connector(software)

#--------------------------------------------------------------------------------
#Code:
#CONNECTION SETUP
import mysql.connector as c

conn=c.connect(
    host='localhost',
    user='root',
    password='123456',#type your mysql password
    database='crud' #type your database name
    )

obj=conn.cursor() 

#CRUD OPERATION
class CRUD:
    def create_table(self):
        q='CREATE TABLE student(id int(2), name varchar(10), loc varchar(20))'
        obj.execute(q)
        conn.commit()
    def insert_data(self,id,name,loc):
        q='INSERT INTO student VALUES(%s, %s, %s)'
        obj.execute(q,(id, name, loc))
        conn.commit()

    def get_all_data(self):
        q='SELECT * FROM student'
        obj.execute(q)
        return obj.fetchall()

    def update_data(self,id,name,loc):
        q="UPDATE student SET name = %s, loc =%s WHERE id = %s "
        obj.execute(q,(name,loc,id))
        conn.commit()

    def delete_data(self,id):
        q='DELETE FROM student WHERE id=%s'
        obj.execute(q,(id,))
        conn.commit()
        
        
crud=CRUD()
#crud.create_table()
#crud.insert_data(2,'kamal','patna')
#print(crud.get_all_data())
#crud.update_data(2,'babu','delhi')
#crud.delete_data(1)
