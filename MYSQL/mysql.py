#mysql.py
import pymysql
con=pymysql.connect(db='new',user='root',passwd='Poojamadan001',host='localhost')
#print(con) # <pymysql.connections.Connection object at 0x102c38bd0>
# python3 -m pip install PyMySQL
cur=con.cursor()
id=input('id')
sname=input('sname')
stream=input('Enter stream')
i=cur.execute("insert into student values('%s','%s','%s')" %(id,sname,stream))
if i==1:
	con.commit()
con.close()
print("Record Saved")


'''

mysql> select * from student
    -> ;
+------+-------+--------+
| id   | sname | stream |
+------+-------+--------+
| 101  | Pooja | MCA    |
+------+-------+--------+
1 row in set (0.00 sec)
'''