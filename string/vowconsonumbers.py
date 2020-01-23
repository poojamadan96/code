#Vowconsonumbers.py 
#Separate Consonents numbers and vowels
#>>> ord('3')
#>>51
#Calculate for 0 to 9

message="26 January is repulic day. It will be off for me.. Yeppeee.... 5 3 "
c=[]
v=[]
n=[]
for x in message:
	if x=='a' or x=='e' or x=='o' or x=='i' or x=='u':
		v.append(x)
	elif ord(x)>=48 and ord(x)<=57:
		n.append(x)
	elif x==' ' or x=='.':
		pass
	else:
		c.append(x)

consolnents=''.join(c)
numbers=''.join(n)
vowels=''.join(v)
print("consolnents =  ",consolnents)
print("numbers =  ",numbers)
print("vowels= ",vowels)

