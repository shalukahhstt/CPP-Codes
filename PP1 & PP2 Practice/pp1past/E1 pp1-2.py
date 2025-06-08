row1=input().split()
row=[]
row.append(row1)
column=[]
x=1

for i in range(len(row1)-1):
    row.append(input().split())
for l in row:
    if len(l)!=len(row1):
        print("Error")
        break
    else: x=0
if x==0:
    for j in range(len(row1)):
        column1=[]
        for k in range(len(row1)):
            column1.append(row[k][j])
        column.append(column1)

    condition1 = 1
    condition2 = 1
    for z in range(1,len(row)-1):

        if sum(map(int,column[z-1])) != sum(map(int,column[z])):
            condition1 = 0
            break
        else: condition1 = 1

    for w in range(1,len(row)):

        if sum(map(int,row[w-1])) != sum(map(int,row[w])) :

            condition2= 0
            break
        else: condition2 = 1

    if condition1 == 1 and condition2 == 1:
        print("Yes")
    elif condition2 == 0 or condition1 == 0:
        print("No")
else: pass






