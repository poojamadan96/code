#json
'''
import json
data={}
data['Employee']=[]
for x in range(3):
	name=input("Enter name")
	age=(int)(input("Enter age"))
	data["Employee"].append(
		{
			'Name': name,
			 "Age": age

		})
with open('ax.json','w') as file:
	json.dump(data,file)
'''


import json
data={}
data['Employee']=[]
for x in range(3):
    name=input('Enter Name')
    age=(int)(input('Enter Age'))
    data['Employee'].append(
    {
        'Name':name,
        'Age':age
    })
with open('ax.json','w') as file:
    json.dump(data,file)