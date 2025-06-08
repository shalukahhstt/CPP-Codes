n=int(input())
x=0
i=1
y=0
count=1
while x<n:
    i=i+1
    if i==2 or i==3 or i==5 or i==7:
        y=1
    else:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                y=0
                break
            else:
                y=1
    if y==1:
        count=count*i
        x=x+1
if count!=1:
    Euclid_num=count+1
    print(Euclid_num)

