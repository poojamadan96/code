#MAking 4th letter caps leader= leaDer
i=0
m=''
name='leader'
for x in name:
	i+=1
	if i==4:
		m=m+x.upper()
	else:
		m=m+x.lower()
print(m)
