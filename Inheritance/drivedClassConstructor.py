# In default case the constructor of dervided class is fired
class base:
	def __init__(self):
		print("fire House")
	def show(self):
		print("HEllo")
class derived(base): # In case of inheritance if we make a constructor then it will print first of all  its value like fire derived in this case later 
	def __init__(self):
		print("Fire Derived")
	def display(self):
		print("Welcome")

ob=derived()
ob.show()
ob.display()