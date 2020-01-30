#count vowels in a string
def countvowels():
	c=0
	word='RamKrishan'
	for w in word:
		if w=='a' or w=='e' or w=='i' or w=='o' or w=='u':
			c+=1
	print(c)
countvowels()