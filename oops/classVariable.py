#Class variable
class Test:
	x=100
	def __init__(self):
		self.x=100 # constructor has declared its variable as instance variable
	def show(self):
		#self.x=105 could be done 
		self.x+=1
		Test.x+=1
		print("Instance", self.x)
		print("class",Test.x)

ob=Test()
ob.show()
ob1=Test()
ob1.show()
ob2=Test()
ob2.show()

# class variable shares its value with diff methods so keep on updating it like 101 102 103 but instance variable doest so stagnant value