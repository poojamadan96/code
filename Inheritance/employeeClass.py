#employeeClass.py
class Employee:
	def setEmployee(self):
		global name,salary
		li=[]
		sli=[]
	for x in range(3):
		na=input('Name')
		sal=(int)(input("Salary"))
		li.append(na)
		sli.append(sal)
	name=li
	salary=sli
class Transaction:
	def mTrans(self):
		global day
		dli=[]
		for x in range(3):
			d=(int)(input("Days"))
			dli.append(d)
		day=dli
class Final(Employee,Transaction):
	def __init__self():
		super().setEmployee()
		super().mTrans()
	def show(self):
		for x in ramge(3):
			onesal=salary[x]