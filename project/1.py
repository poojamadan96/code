# %s= string, %d = digit like accoungt number, %f= float for float values
from pymysql import *
class Bank:
	def __init__(self):
		self.con=connect(db='new',user='root',passwd='Poojamadan001',host='localhost')
	def createtable(self):
		cur=self.con.cursor()
		cur.execute("create table bank(acno int primary key,name varchar(30),balance float)")
		cur.execute("create table trans(acno int,amt float, transtype varchar(10),foreign key kk(acno) references bank(acno))")
		self.con.commit()
	def openaccount(self):
		acno=(int)(input("Enter account no. "))
		name=input("Enter name")
		balance=(float)(input("Enter account balance"))
		cur=self.con.cursor()
		i=cur.execute("insert into bank values('%d','%s','%f')" %(acno,name,balance))
		if i==1:
			self.con.commit()
		print("Record saved")
	def amoountwithdraw(self):
		acno=(int)(input("Enter account number"))
		amt= (float)(input("Enter amount"))
		ttype='w'
		cur=self.con.commit()
		i=cur.execute("update bank set balance=balance-'%f' where acno='%d'" %(amt,acno))
		if i==1:
			j=cur.execute("insert into trans values('%d','%f','%s')" %(acno,amt,ttype))
			if j==1:
				self.con.commit()
		print("account updated")
	def amountdeposit(self):
		acno=(int)(input("Enter account number"))
		amt= (float)(input("Enter amount"))
		ttype='d'
		cur=self.con.commit()
		i=cur.execute("update bank set balance=balance + '%f' where acno='%d'" %(amt,acno))
		if i==1:
			j=cur.execute("insert into trans values('%d','%f','%s')" %(acno,amt,ttype))
			if j==1:
				self.con.commit()
		print("account updated")

ob=Bank()
#ob.createtable() # Tbale has to be created once so we have to run the object once and then comment this line
ans='y'
while ans=='y':
	print('1. Account open')
	print('2. Amount withdraw')
	print('3. Amount Deposit')
	print('4 Exit')
	print('Enter choice')
	ch=(int(input()))
	if ch==1:
		ob.openaccount()
	elif ch==2:
		ob.amountdeposit()
	elif ch==4:
		exit(0)
	print('Continue  ')
	ans=input()



