ans='y'
student=[]
while ans=='y':
	print('1,Add name')
	print('2,Search name')
	print('3,Show All')
	print('4,Modify')
	print('5,Delete')
	print('6,exit')
	print("Enter choice")
	choice=(int(input()))
	if choice==1:
		name=input("Enter name")
		student.append(name)
		print("record Updated",student)
	elif choice==2:
		searchname=input("write the name to be searched")
		if searchname in student:
			print("Name Found", searchname)
		else:
			print("Name not found")
	elif choice==3:
		for x in student:
			print(x)
	elif choice==4:
		oldname=input("Enter oldname")
		newname=input("Enter newname")
		if oldname in student:
			i=student.index(oldname)
			student[i]=newname
			print("Student List", student)
		else:
			print("Name not found")

	elif choice==5:
		print("NAme to be Deleted from list")
		dname=input()
		if dname in student:
			student.remove(dname)
			print("Entry Removed",student)
		else:
			print("Name is not there")
	elif choice==6:
		exit(0)
	print("Continue y/n")
	ans=input()