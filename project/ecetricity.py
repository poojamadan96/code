#ELECTRICITY.PY
from pymysql import *
class electricity:
	def __init__(self):
		self.con=connect(db='new',user='root',passwd='root',host='localhost')
	def createtable(self):
		cur=self.con.cursor()
		cur.execute("create table residen(acno int primary key, name varchar(10)")
		cur.execute("create table trans(acno int ,amt int, reading float foreign key kk(acno) refrence residen(acno))")
	def readingdetails(self):
		acno=(int(input("enter account number"))
		name-input("enter name")
		cur=self.con.cursor()
		i=cur.execute("insert into residen('%d','%s')" %(acno,name))
		reading=(int(input("enter the number of reading used"))
		if i==1:
			self.con.commit()
		print("Record Saved")
	def transac(self):
		type=input("enter type")
		if type=="resi"
		amt= reading*6.5
		cur=self.con.cursor()
		i=cur.execute(insert into residen())
		