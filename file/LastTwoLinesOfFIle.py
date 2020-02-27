#LastTwoLinesOfFIle
with open ("filename.txt",'r') as file:
	line=file.readlines()
x=len(line)
x-=2
print([line[x:]])


