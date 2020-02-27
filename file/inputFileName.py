#input file name and store the data respectively
import os
os.mkdir('d123')
os.chdir()
filename=input("enter file name to be created")
with open(filename,"a+") as file:
	value=input("Enter the file data") +'\n'
	file.write(value)

