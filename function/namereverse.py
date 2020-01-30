#reverse the name using function
def names(name):
		y=name[::-1]
		return y
reversename=names("pooja")
print(reversename)

#==========================================================
name=input("Enter the name")
def reversename(name):
	s=len(name)
	for x in range(s-1,-1,-1):
		print(name[x],end='')
reversename(name)
print ()


#==================================================
# Reverse the number
no=(int)(input("Enter the number to reverse"))
def numreverse(no):
	k=0
	while no>=1:
		i=no%10
		k=k*10+i
		no=no//10 #Division
	print(k)
numreverse(no)
