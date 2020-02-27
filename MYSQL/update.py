#update record 
import pymysql
con=pymysql.connect(db='new',user='root',passwd='Poojamadan001',host='localhost')
cur=con.cursor()
id=input("Enter student id")
sname=input("Enter updated name")
i=cur.execute("update student set sname='%s' where id='%s'" %(sname,id))
if i==1:
	con.commit()
	print("Record saved")
cur.execute("select * from student where sname='%s'" %(sname))
rs=cur.fetchall()
print(rs)
con.close()