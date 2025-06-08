n = int(input())
list1 = input().split(',')
row=[]
sub_row=[]
column = []
sub_column = []
def search(n,list2):
    condition = True
    for i in range(n):
        x=0
        for j in range(n):
            data=list2[i][j]
            if data=="1":
                x=x+1
            else: continue
        if x!=1:
            condition = False
        else: continue
    return (condition)
condition1=False
for x in list1:
    if int(x)==0 or int(x)==1:
        condition1 = True
    else:
        condition1 = False
        print("NO")
        break
if condition1 == True:
    for i in range(len(list1)):
        sub_row.append(list1[i])
        if (i+1)%n==0:
            row.append(sub_row)
            sub_row=[]
        else:pass
    #print(row)
    for j in range(n):
        for k in range(n):
            sub_column.append(row[k][j])
        column.append(sub_column)
        sub_column=[]
    #print(column)

    row_condition = search(n,row)
    column_condition = search(n,column)
    #print(row_condition,column_condition)
    if column_condition==True and row_condition==True:
        print("YES")
    else: print("NO")
else:pass