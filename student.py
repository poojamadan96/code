student={}
li=[]
for x in range(2):
	name=input("name")
	for y in range(2):
		m=int(input("Marks"))
		li.append(m)
	student[name]=li[0]+li[1]
print(student)