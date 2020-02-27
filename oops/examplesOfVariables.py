#examplesOfVariables
class Test:
	z=30
	def __init__(self):
		self.x=10 # Instance variable
	def show(self):
		self.__y=20 # Private variable
		print(self.__y)
	def show1(self):
		print(self.__y)
		print(self.z)
		print(self.x)

ob=Test()
ob.show()
ob.show1()
print(ob.__y) # error as just private variable
