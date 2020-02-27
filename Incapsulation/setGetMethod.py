class Abc:
	def __init__(self):
		self.__name="Mayank"
	def setName(self,name):
		print("Set method call") # Pre Defined methods set and get
		self.__name=name
	def getName(self):
		print("Get method call")
		return self.__name
	newname=property(getName,setName) # combining both the methods
obj=Abc()
obj.newname="Pooja"
print(obj.newname)