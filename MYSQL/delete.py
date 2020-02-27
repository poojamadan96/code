#delete.py
import pymysql
con=pymysql.connect(db='new',user='root',passwd='Poojamadan001',host='localhost')
cur=con.cursor()
id=input("Enter student id to delete")
i=cur.execute("delete from student where id='%s'" %(id))
if i==1:
	con.commit()
	print("Record saved")
con.close()