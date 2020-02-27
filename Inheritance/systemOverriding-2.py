#systemOverriding-2.py
class Abc:
	def __init__(self,x,y):
		self.x=x # self in isntsance variable here used as to make the variable global
		self.y=y
	def __str__(self):
		return "You are printing object value"
	def __add__(self,other):
		i=self.x+other.x # 
		j=self.y+other.y
		return(i,j)
ob=Abc(12,24)
ob1=Abc(34,56)
print(ob+ob1)