class base:
	def show(Self):
		print("HEllo")
class derived(base):
	def display(self):
		print("Welcome")

ob=derived()
ob.show() # Object of base class can access both the classes methods
ob.display()