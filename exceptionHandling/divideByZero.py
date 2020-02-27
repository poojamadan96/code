#divideByZero.py
i=10
j=0
try:
	k=i/j
	print(k)
except ZeroDivisionError as obj:
	print(obj)
print("I am running")
