#instanceVariable.py
#self.bvariable= instance variable
class test:
	def show(self):
		self.x=10
		print(self.x)
	def show2(self):
		print("Total",self.x)

#can be called anywhere inside functions also outside function with the help of object refernce
ob=test()
ob.show()
ob.show2()
print("welcome",ob.x)