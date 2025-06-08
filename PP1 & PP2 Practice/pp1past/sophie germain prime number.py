def prime(i):
    x=0
    if i<2:
        x=0
    elif i==2:
        x=1
    else:
        for j in range(2,i):
            if i%j==0:
                x=0
                break
            else:
                x=1
    return(x)

p=int(input())
q=int(input())
sum=0
for k in range(p,q+1):
    x=prime(k)
    if x==1:
        y=prime(2*k+1)
    else:
        y=0
    if y==1:
        sum=sum+k
print(sum)

