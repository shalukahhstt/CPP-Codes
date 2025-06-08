n = int(input())
list=[]
y=n
if n==2:
    print("2")
elif n>2:
    for i in range(2,n):
        x=1
        power=0
        factor=0
        while x>0:
            if n%i==0:
                power = power+1
                if power==1:
                    factor=str(i)
                elif power>1:
                    factor=str(i)+"^"+str(power)
                n=n/i
            else:
                x=0
        if int(power)!=0:
            list.append(factor)
            list.append("X")
    for j in range(len(list)-1):
        print(list[j],end=" ")
    if len(list)==0:
        print(y)
elif n<2:
    print("No Prime Factors")