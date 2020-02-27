class student:
	def setProfile(self):
		global name,age
		name=input("Enter name")
		age=int(input("Enter age"))

class Marks(student):
	def setMarks(self):
		global p,c,m
		p=(int(input("enter phy marks")))
		c=(int(input("enter chem marks")))
		m=(int(input("enter math marks")))
class Result(Marks):
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

