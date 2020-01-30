#Pass n no. of argumants
names=['ram','Shyam','Pooja']
def sayHello(names):
	for x in range(len(names)):
		print("Welcome", names[x])

sayHello(names)