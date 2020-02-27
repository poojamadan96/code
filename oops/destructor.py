#destructor
# with the help of self we are able to make the object of class Test
class Test:
	def __init__(Self):
		print("fired") # will be printed at first
	def __del__(self):
		print("Welcome") # will be printed at last since destructor
	def show(Self,name):
		print("Welcome","NAme") # parasmeters are passed along with self

ob=Test() # No need to call the object for constructor to execute
ob.show("Pooja")