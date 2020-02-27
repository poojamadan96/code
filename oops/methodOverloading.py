'''Python does not support method overloading
so if use more then 1 moethod with the same name so python will forget all the methosds and will remember only the last method used.
'''
class Abc:
	def __init__(self):
		print('1')
	def __init__(Self,name):
		print(name)
	def show(Self):
		print(name)

ob=Abc('Kumar') # Kumar will be printed but not 1 as kumar has overwriiten the 1
ob.show('Poojas')


'''pmadan-macOS:oops pmadan$ python3 methodOverloading.py 
Kumar
Traceback (most recent call last):
  File "methodOverloading.py", line 13, in <module>
    ob.show('Poojas')
TypeError: show() takes 1 positional argument but 2 were given
pmadan-macOS:oops pmadan$ 
