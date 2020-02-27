import ast
import time
filename='bank.txt'
ans='y'
while ans=='y':
	print('1. open account')
	print('2. Deposit')
	print('3 withdraw')
	print('4 show')
	print("5. delete")
	print("6. exit")
	ch=(int)(input("enter choice"))
	if ch==1:
		ac=0
		acno=input("enter account number")
		if acno.isdigit():
				if len(acno)>2:
					ac=int(acno)
					name=input("enter name")
					balance=(int)(input("enter balance"))
				else:
					print("Account number must be > 4 digit")
					time.sleep(10)

					continue
		else:
			print("Enter integer value")
			time.sleep(10)
			continue
		

		with open (filename,'a+') as file:
			li=[ac,name,balance]
			file.write(str(li)+'\n')
		print("Account created")
	elif ch==2:
		acno=int(input("enter account number to deposit"))
		amt=int(input("ENter amount"))
		with open(filename, 'r') as file:
			banklist=file.readlines()
		i=0
		for x in banklist:
			i+=1
			li=[]
			li=ast.literal_eval(x) # To convert into list by default it shows string
			if li[0]==acno:
				bal=li[2]
				bal=bal+amt
				li[2]=bal
				#print(li[0],li[1],li[2])	
				l=str(li)+'\n'
				banklist[i-1]=l
		with open(filename,'w') as file:
			for x in banklist:
				file.write(str(x))
	elif ch==3:
		acno=int(input("enter account number to withdraw"))
		amt=int(input("ENter amount"))
		with open(filename, 'r') as file:
			banklist=file.readlines()
		for x in banklist:
			li=[]
			li=ast.literal_eval(x)
			if li[0]==acno:
				bal=li[2]
				bal=bal-amt
				li[2]=bal
				print(li[0],li[1],li[2])
	elif ch==4:
		with open(filename,'r') as file:
			banklist=file.readlines()
		for x in banklist:
			li=[]
			li=ast.literal_eval(x)
			print(li[0],li[1],li[2])
	elif ch==5:
		with open(filename,'r') as file:
			banklist=file.readlines()
		dcno=(int)(input("enter the account number to delete "))
		m=0
		for x in banklist:
			li=[]
			li=ast.literal_eval(x)
			if li[0]==dcno:
				li1=str(li)+'\n'
				banklist.remove(li1)
				m=1
				with open('dummy.txt','a+') as filed:
					filed.write(li1)
					print("Record removed")
			if m==0:
				print("Record not founds")
		with open('filename','w') as file:
			for x in banklist:
				file.write(str(x))
	elif ch==6:
			exit(0)




	ans=input("Continue y/n")
