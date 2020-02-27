import json
with open("ax.json",'r') as file:
	di=json.load(file)
name=input("Enter name")
for p in di["Employee"]:
	if p['name']==name:
		print('Name:', p['Name'])
		print('Age: ', p['Age'])
	