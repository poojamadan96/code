#basics.txt.py
class Abc:
	self.x=10 #  Instance 
	self.__x=10 # Private
	self._x=10 #Protected

ob=Abc()
print(ob.x)
print(ob._x)
print(ob.__x)
