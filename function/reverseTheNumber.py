#reverseTheNumber.py
#Reverse the number of total>10
#123 = 6
def rev(no):
	k=0
	t=0
	while no>=1:
		i=no%10
		k=k*10+i
		t+=1
		no=no//12
	if t>=10:
		print(k)
	else:
		print("No is small")
rev(123435)

