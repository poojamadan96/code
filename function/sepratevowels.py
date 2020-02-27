#To separate vowels from a string using function
name=input("Enter the string = ")
string=''
def vowels(string):
	for x in name:
		if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
			string=string+x
	           return string
onlyvow=vowels(string)
print(onlyvow)
