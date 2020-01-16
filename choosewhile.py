ans='y'
student=[]
while ans=='y':
        print('1, Add Name')
        print('2, Search Name')
        print('3, Show All')
        print('4, Modify')
        print('5, Delete')
        print('6, Exit')
        print("Enter Choice")
        ch=((int)(input())
        print(ch)
        if ch==1:
                name=input("Enter name")
                student.append(name)
                print("Record Saved")
        elif ch==2:
                name=input("Enter name for search")
                if name in student:
                        print("Name Found", name)
                else:
                        print("Name not found",name)
        elif ch==3:
                for x in student:
                        print(x)
        elif ch==4:
                oldname=input('oldname')
                newname=input('newname')
                if oldname in student:
                        i=student.index(oldname)
                        student[i]=newname
                        print ("Record Updated", student)
        elif ch==5:
                dname="Enter name to delete"
                if dname in student:
                        student.remove(dname)
                        print("Record Deleted")
                else:
                        print("Record not found")
        elif ch==6:
                exit(0)
                print("continue y/n")
                ans=input()
                