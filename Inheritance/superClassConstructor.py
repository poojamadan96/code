#super class constructor
# In default case the constructor of dervided class is fired
class base:
	def __init__(self):
		print("fire House")
	def show(self):
		print("HEllo")
class derived(base):
	def __init__(self):
		super().__init__() # It will call teh constructor of base class first and then will call it sel

		print("Fire Derived")
	def display(self):
		print("Welcome")

ob=derived()
ob.show()
ob.display()

'''fire House
Fire Derived
HEllo
Welcome
''''