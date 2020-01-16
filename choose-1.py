ans='y'
a=input("First number")
b=input("Second number")
while ans=='y':
	print ("1, Add number")
	print("2, subtract")
	print("3,multiply")
	ch=((int)(input("select the choice")))
	if ch==1:
		print("addition",a+b)
	elif ch==2:
		print("Subtraction",a-b)
	elif ch==3:
		print("Multiply",a*b)

	print("Continue y/n")
	ans=input()


