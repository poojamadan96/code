#abcd
#efgh
#ijkl
#mnop
#qrst
#uvwx
#yz```
ch=97
i=0
for x in range(7):
	for y in range(4):
		print(chr(ch),end='')
		ch+=1
		if ch==123:
			break
	else:
		print()
print()
	