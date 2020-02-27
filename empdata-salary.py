#create Employee collection that takes name of employee, salary and monthly working days
employee={}
for x in range(2):
	name=input("Name of employee ")
	daysw=(int)(input("no. of days worked "))
	fixsal=(int)(input("Enter fixed salary "))
	oneday=fixsal//30
	sal=oneday*daysw
	employee[name]=sal
print(employee)








                                                   