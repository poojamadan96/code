#printmysql.py
import pymysql
con=pymysql.connect(db='new',user='root',passwd='Poojamadan001',host='localhost')
cur=con.cursor()
cur.execute("select * from student")
result=cur.fetchall()
print(result) # In JSon lets do it in row column field
for x in range(len(result)):
	for i in range(len(result[x])):
		print(result[x][i])
	print ('----------------------------------------------')

	'''
	(('101', 'Pooja', 'MCA'), ('102', 'Lakshmi', 'ASD'), ('sd', 'ff', 'dx'), ('1223', 'dd', '23df'))
101
Pooja
MCA
----------------------------------------------
102
Lakshmi
ASD
----------------------------------------------
sd
ff
dx
----------------------------------------------
1223
dd
23df
----------------------------------------------'''
