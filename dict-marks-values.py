
#To Take three names and there 3 subject marks and show in a dictionary name marks grade Pooja 230 First
#Ram:{'Math':55,'Phy':45,'Che':55}
student={}
li=[]
for x in range(3):
	name=input("Enter the name of student")
	for y in range(3):
		m=int(input("marks"))
		li.append(m)
	student[name]=li
print(student)