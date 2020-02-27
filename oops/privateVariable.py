#privateVariable.py
class Test:
	def __init__(self):
		self.__x=10 # Private variable declared by __
	def show(self):
		print(self.__x)

ob=Test()
ob.show()
print(ob.__x) # will throw the error as cant be accessed outside the class 