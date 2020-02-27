#file
#Significance of \n==. ??????
# with open('name','mode ') as file: = Automatic file closure
ans='y'
fname='ado.txt'
while ans=='y':
	print("1.Add Record")
	print('2 Display record')
	print('3 search record')
	print('4 modify record')
	print('5 Delete record')
	print(' 6 Exit record')
	print("Enter choice from 1 to 6 ")
	ch=int(input())
	if ch==1:
		name=input("enter name ")+'\n'
		with open(fname,'a+') as file:
			file.write(name)
			print("Record Saved")
	elif ch==2:
		with open(fname) as file: #Automatic read mode
			slist=file.readlines()
			for x in slist:
				print(x,end='')

	elif ch==3:
		sname=input("Enetr the name to be searched ")+'\n'
		with open(fname) as file:
			slist=file.readlines()
		if sname in slist:
			print("Found ", sname)
		else:
			print("Name not found")
	elif ch==4:
		oname=input("enter old name") +'\n'
		nname=input("Enter new name")+'\n'
		with open(fname,'a+') as file:
			file.write(mode)
			print("Record Updated")
	elif ch==5:
		pass
	elif ch==6:
		exit(0)
	print("Continue y/n")
	ans=input()
