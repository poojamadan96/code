emp={}
for x in range(2):
	name=input("Enter name ")
	sal=(int)(input("salary"))
	nod=int(input("No of working days "))
	emp[name]=[sal,nod]

print(emp)
for x,y in emp.items():
	oneday=y[0]//30
	totalsalary=y[1]*oneday
	print(x,totalsalary)