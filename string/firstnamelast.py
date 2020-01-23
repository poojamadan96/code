#ram kumar Sharma r k sharma
name=input("Enter name")
#name.split() It separated with the space
sname=name.split()
size=len(sname)
#sname = ram kumar sharma - len =3
newname=''
for x in range(size-1):
	newname=newname+ ''+ sname[x][0]
newname=newname+' '+sname[size-1]
print(newname.title())