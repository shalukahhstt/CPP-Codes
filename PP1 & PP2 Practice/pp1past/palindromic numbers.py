ran = input().split()
total=0
x=0
for i in range(int(ran[0]),int(ran[1])+1):
    if str(i)==str(i)[::-1] :
        if (i**(0.5))%1==0 :
            total=total+i
        else:
            if i==2 :
                total=total+i
            else:
                for j in range(2,i):
                    if i%j==0:
                        x=0
                        break
                    else:
                        x=1
                if x==1:
                    total=total+i
print(total)