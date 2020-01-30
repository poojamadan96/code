#lambda
mylist=[1,2,3,4]
newlist=list(filter(lambda x: (x%2==0), mylist))
print(newlist)


#map == filter


mylist2=[23,44,555,33,2,1]
newlist2=list(map(lambda x: x**2, mylist2))
print(newlist2)