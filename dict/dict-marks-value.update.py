#With some addition and
#Dictionary with in Dictionary

student={}
for i in range(3):
	mark={}
	name=input("student name ")
	m=(int)(input("Math "))
	p=(int)(input("Phy "))
	c=(int)(input("Chemistry "))
	mark['math']=m
	mark['chem']=c
	mark['phy']=p
	student[name]=mark
for name,marks in student.items():
	tot=0
	div=0
	for x,y in marks.items():
		tot+=y
		if tot/3>60:
			dev ="First"
		elif tot/3<=45 and tot/3<=60:
			dev="Second"
		else:
			dev="Third"

	print('Name', name,'total marks',tot,dev)




