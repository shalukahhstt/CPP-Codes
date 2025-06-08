n=int(input())
list1=[0,1]
for i in range(n-2):
    list1.append(int(list1[-1]+list1[-2]))
for j in list1:
    print(j,end=" ")
