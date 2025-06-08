r=1
while r>0:
    n=int(input())
    x=1
    t=0
    if n<0:
        r=0
    else:
        n1 = int(n ** 0.5)
        while x<n1:

            x=x+1
            y = n % x
            if y==0:
                t=2
                break
            else:
                t=1

        if n==2 or n==3:
            print("prime")

        elif n==1 or n==0:
            print("non-prime")


        elif t==2:
            print("non-prime")

        elif t==1:
            print("prime")



