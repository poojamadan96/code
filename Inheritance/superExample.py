class base:
	def __init__(self):
		super().__init__()
		print("base")
class subchild:
	def __init__(self):
		print("Sub child")
class superchild(base,subchild): # vase is parent class , subchild is child class
	def __init__(self):
		super().__init__()
		print("HEllo")
ob=superchild() # First It will go to superchild will see a  parent which is base classsuper so will reach to base class 
#there again is a super so will go to subchild and print that later base then will come to hello


Sub child
base
HEllo

