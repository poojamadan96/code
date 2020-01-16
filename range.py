for x in range(10):
	print(x,end= ' ') 
#to print the range in one hoprizontal line



for y in range(1,30,3):
	print(y,end= "  ")
# with specific range



for z in range(1,10):
	for a in range(1,z+1):
		print(a,end='')
	print()
#To get a prism structure



for x in range(10,0,-1):
	for y in range(x,0,-1):
		print(y,end='')
	print()
#Back side prism

#----------------------------
#Print 1 121 12321 1234321 123454321

i=1
j=1
for x in range(5):
	print(i)
	j=j*10+1
	i=j*j


#------------------------



print()


for x in range(5):
	print(11**x)
