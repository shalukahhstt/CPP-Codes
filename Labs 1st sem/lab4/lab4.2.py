n=int(input("Input number: "))
x=2
i=0
total=0
while x<=n:
    for y in range (1,x):
        z=x%y
        if z==0:
            total=total+y


    if total > x:
        i=i+1
    x=x+1
    total=0

if n<2:
    print("Invalid Input")
elif n==2:
    print("Number of abundant numbers from 1 to " + str(n) + " is " + str(i))
else:
    print("Number of abundant numbers from 1 to "+str(n)+" is "+str(i))