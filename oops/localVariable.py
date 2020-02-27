#localVariable.py
class Test:
	def show(self):
		x=10
		print(x)
	def show(self):
		print(x)

#x is a local variable  so cant be used in diff function
ob=Test()
ob.show()
ob.show2()

