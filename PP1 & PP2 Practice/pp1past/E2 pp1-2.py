list1=[]
max=0
min=999999
mx=[]
mn=[]
absent=[]
sum=0
for i in range(3):
    list1.append(input().split(":"))
for j in list1:
    if j[1]=="":
        absent.append(j[0])
    else:
        sum=sum+int(j[1])
        if max==int(j[1]):
            mx.append(j[0])
        elif max<int(j[1]):
            max=int(j[1])
            mx=[]
            mx.append(j[0])
        else:continue
        if min == int(j[1]):
            mn.append(j[0])
        elif min > int(j[1]):
            min = int(j[1])
            mn = []
            mn.append(j[0])
        else:
            continue
print("Maximum : ",end="")
for k in mx:
    print(k,end=" ")
print("")
print("Minimum : ",end="")
for h in mn:
    print(h,end=" ")
print("")
print("Average :",sum/3)
