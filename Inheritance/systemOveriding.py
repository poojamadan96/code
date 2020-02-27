#systemOveriding.py
class Abc:
	def __init__(self):
		print('1')
	def __str__(self): # Object message comes from here
		return "You are printing wrong object value"

ob=Abc()
print(ob) # It will now show the str message