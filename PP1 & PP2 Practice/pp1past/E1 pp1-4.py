end = int(input())
sum=0
sum2=0
for i in range(1,end+1):
    if int(i**0.5)==float(i**0.5):
        sum=sum+i
    else:continue
if sum==1:
    print(1)
else:
    for j in range(1,sum):
        if sum%j==0:
            if int(j**0.5)==float(j**0.5):
                sum2=sum2+j
    print(sum2)