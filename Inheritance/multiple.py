#multiple.py
class student:
	def __init__(self):
		print("1")
	def setProfile(self):
		global name,age
		name=input("Enter name")
		age=int(input("Enter age"))

class Marks:
	def __init__(self):
		super().__init__()
		print("2")

	def setMarks(self):
		global p,c,m
		p=(int(input("enter phy marks")))
		c=(int(input("enter chem marks")))
		m=(int(input("enter math marks")))

class Result(student,Marks):  # In this case it will only print 1 since constructor goes from down to up , change the sequence if want all constructor to get print
#first class is super parent and second is second parent so student is first and marks is second parent class
	def __init(self):
		super().__init__()
		print("3")
	def show(self):
		total=p+c+m
		per=total/3
		if per>=60:
			div="First"
		else:
			div="Last"
		print("Name",name)
		print('Age',age)
		print("total= ",total)
		print("Percentage",per)

os=Result() #child object can access Parent thing so object has to be made from the base/dervied class
os.setProfile()
os.setMarks()
os.show()

