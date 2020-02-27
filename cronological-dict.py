#create a dictionary for the grand parent name and then the kids he has then the kids he has
#{ram:{a:{b}}}

grandfinal={}
gname={}
fname={}
for x in range(1):
	gname=input("Enter name of Grand Parent ")
	fname=input("Enter name of father")
	uname=input("enter your name")
	grandfinal[gname]=fname
for x,y in grandfinal.items():
	y=uname[x]

print(grandfinal,gname,fname)