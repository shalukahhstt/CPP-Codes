numbers = input().split()
duplicates = []
main = []
x=1
y=0
total=0
for i in numbers:
    y=y+1
    if i=="-1":
        break
    elif i in main:
        duplicates.append(i)
        print("Duplicate number"," ",x," = ",i,", Position ",int(numbers.index(i))+1," and ",y)
        x=x+1
    else:
        main.append(i)
if len(duplicates)==0:
    print("No Duplicate numbers")
else:
    for i in duplicates:
        total=total+int(i)
    print("Sum of the duplicate numbers = ",total)