#constructorChaining
#multiLevel
class one:
	def __init__(self):
		print('1')
	def show1(self):
		print("one")
class two(one):
	def __init__(self):
		super().__init__()
		print('2')
	def show2(self):
		print('two')

class three(two):
	def __init__(self):
		super().__init__()
		print(3)
	def show3(self):
		print("Three")
ob=three()
ob.show1()
ob.show2()
ob.show3()