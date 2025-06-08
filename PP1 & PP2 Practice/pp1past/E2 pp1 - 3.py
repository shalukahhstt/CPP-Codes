list=input().split()
main=[]
repeat=[]
for i in list:
    if i in main:
        repeat.append(i)
    else:
        main.append(i)
if len(repeat)!=0:
    print("True")
else:
    print("False")