import ast
filename='bank.txt'
ans='y'
while ans=='y':
    print('1. Open Account')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Show')
    print('5. Exit')
    ch=(int)(input('Enter Choice'))
    if ch==1:
        ac=0
        acno=input('Account No')
        if acno.isdigit():
            ac=int(acno)
            name=input('Name')
            balance=(int)(input('Enter Balance Amount'))
        else:
            continue
        with open(filename,'a+') as file:
            li=[ac,name,balance]
            file.write(str(li)+'\n')
        print('Account Created')
    elif ch==2:
        acno=(int)(input('Account No to Deposit'))
        amt=(int)(input('Enter Amt'))
        with open(filename,'r') as file:
            banklist=file.readlines()
        i=0
        for x in banklist:
            i+=1
            li=[]
            li=ast.literal_eval(x)
            if li[0]==acno:
                bal=li[2]
                bal=bal+amt
                li[2]=bal
                #print(li[0],li[1],li[2])
                l=str(li)+'\n'
                banklist[i-1]=l
        with open(filename,'w') as file:
            for x in banklist:
                file.write(str(x))
                
    elif ch==3:
        acno=(int)(input('Account No to withdraw  '))
        amt=(int)(input('Enter Amt'))
        with open(filename,'r') as file:
            banklist=file.readlines()
        i=0
        for x in banklist:
            i+=1
            li=[]
            li=ast.literal_eval(x)
            if li[0]==acno:
                bal=li[2]
                bal=bal-amt
                li[2]=bal
                #print(li[0],li[1],li[2])
                l=str(li)+'\n'
                banklist[i-1]=l
        with open(filename,'w') as file:
            for x in banklist:
                file.write(str(x))
                
    elif ch==4:
        with open(filename,'r') as file:
            banklist=file.readlines()
        for x in banklist:
            li=[]
            li=ast.literal_eval(x)
            print(li[0],li[1],li[2])
    elif ch==5:
        exit(0)
    ans=input('continue y/n')