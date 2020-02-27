                   # Ram Kumar sharma = Sharma R  K
name=input("Enter name")
sname=name.split()
size=len(sname)
#len=3 Ram Kumar Sharma - split
newname=''
for x in range(size-1):
	newname=sname[size-1]
newname=newname +' '+ sname[0][0] + ' '+sname[x][0]

print(newname.title())

