data = input().split()
n1=int(data[0])
n2=int(data[1])
series=[]
sub_max=[]
sub_interval = []
if n1==0 and n2==1:
    print(0)
    print(1)
elif n1==0 and n2==2:
    print(1)
    print(2)
elif n1==1 and n2==2:
    print(1)
    print(2)
elif n1>=0 and n2>n1:
    if n1==0 or n1==1:
        n1=2
    else: n1=n1
    for i in range(n1,n2+1):
        series.append(i)
        k=int(i)
        a=0
        series=[]
        while a != 1:
            if k==1:
                a=1
                break
            if k%2==0:
                k=k/2
                series.append(k)
            else:
                k=3*k+1
                series.append(k)
        sub_interval.append(len(series))
        sub_max.append(max(series))
    print(max(sub_interval))
    print(int(max(sub_max)))