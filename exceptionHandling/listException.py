#listException.py
#Finally included
#index and range exception = more then two exceptiom

i=10
j=0
li=[1,2,3,4,5]
try:
	k=i/j
	print(k)
	for x in range(len(li)+1):
		print(li[x])
except ZeroDivisionError as obj:
	print(obj)
except IndexError as ie:
	print(ie)
finally:
	print("Must include me")
print("I am running again :P ")
