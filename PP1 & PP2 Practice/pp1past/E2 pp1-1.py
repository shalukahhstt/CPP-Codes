number = int(input())
x=1
count = 0
while x!=0:
    count=count+1
    if number==1:
        x=0
    else:
        if number%2==0 :
            number=number/2
        else:
            number=number*3+1
print(count-1)
