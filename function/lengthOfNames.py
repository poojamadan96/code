#to calculate length of all names
#names=input("Enter the name")
def add (*name):
	for x in name:
		size=len(x)
		print("Name and length is  ",x,size)

add('Pooja','Dog','Rajesh')


#======================================================
#USing List
def clength(name):
	for x in name:
		print(len(x))
li=['Ram','Shty','Sujal']
clength(li)
#====================

li=[]
for x in range(2):
	li.append(input("Enter name"))

clength(li)