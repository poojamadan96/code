#factorial using recursive function = Fucntion which calls itself
num=int(input("Enter no. to get factorial "))
def fact(num):
	if num==1:
		return 1
	else:
		return num*fact(num-1)

factorial=fact(num)
print(factorial)