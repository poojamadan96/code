#To shopw words char lines an a file


file=open("filename.txt","r")
all=file.read()
file.seek(0)
line=file.readlines()
print("Total no. of lines",len(line))
print("total no. of words",len(all.split()))
print("total no. of characters",len(all))
