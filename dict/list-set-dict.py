#Make set and list from Dictionary
dict={'a':1,'b':2,'c':3,'d':4,'e':5}
li=[]
sets=set()
for x,y in dict.items():
	li.append(x)
	sets.add(y)
print("List = ",li)
print("sets = ",sets          /