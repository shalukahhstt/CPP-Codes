
y=0
y=int(input("Number of Students : "))
x=0
while x<y:
    tot=0
    avg=0
    mark=0
    i=0
    name=(input("Name of the student : "))
    x=x+1
    while i<=3:
        mark=int(input("Input Marks : "))
        tot=tot+mark
        i=i+1
    print("\nTotal Marks of ",name," is ",tot,"\n")
    avg=tot/4
    print("Average is ",avg)
