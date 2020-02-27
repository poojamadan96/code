# Primary ey, No duplicat erecord insertion
import pymysql
con=pymysql.connect(db='new',user='root',passwd='Poojamadan001',host='localhost')
cur=con.cursor()
id=input("Enter student id")
cur.execute("select * from student where id='%s'" %(id))
rs=cur.fetchall()
if len(rs)>0:
	print("Duplicat records")
else:
	sname=input("Enter sname")
	stream=input("Enter stream")
	i=cur.execute("insert into student values ('%s','%s','%s')"%(id,sname,stream))
	if i==1:
		con.commit()
	con.close()
	print("Record saved")

