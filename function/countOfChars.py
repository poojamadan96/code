#tell the count of characters
word=input("Enter the string")
c=input("Enter the digit whoes count needs to be checked")
def count(word,c):
	n=0
	for x in word:
		if x==c:
			n+=1
	print("No. of char in given word is = ",n)

count(word,c)