#multipleInheritance.py
class Aone:
	def __init__(self):
		print("1")
	def show1(self):
		print("Welcome 1")

class Atwo:
	def __init__(self):
		print("2")
	def show2(self):
		print("Welcome two")
class Athree(Aone,Atwo):
	def __init__(self):
		print("3")
	def show3(self):
		print("Welcome three")
ob=Athree()
ob.show1()
ob.show2()
ob.show3()