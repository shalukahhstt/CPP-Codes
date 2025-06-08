x=0
while x==0:
    n=int(input())
    if n==-1:
        x=1
        print("Good Bye")
        break
    else:
        for i in range(1,n+1):
            print(" "*2*(n-i),end=" ")
            for j in range(i,0,-1):
                print(j ,end=" ")
            for j in range (2,i+1):
                print(j, end=" ")
            print("")