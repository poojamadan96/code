#Magic numbers
k=x=n=0
no=int(input("Number "))
def magic(no):
	k=x=n=0
	while no>=1:
		n=no%10
		k=k+n
		no=no//10
	if k>1:
		n=0
		while k>=1:
			n=k%10
			x=x+n
			k=k//10
		if x==1:
			print("Magic")
	elif k==1:
		print("Magic")

magic(no)