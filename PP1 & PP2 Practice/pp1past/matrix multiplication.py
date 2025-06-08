def input_matrix(length,list,col):

    for i in range(length):
        x=[]
        x.append(input().split())
        list.append(input().split())
        if len(x)!= col:
            print("Invalid Matrix")
            return False
            break
        else:
            continue
    return True
dimensions=input("Enter the dimension: ").split(",")

row=int(dimensions[0])
column=int(dimensions[1])
row_A=[]
row_B=[]
BT=[]
matrix_3=[]
print("Enter Matrix A:")
condition=input_matrix(row,row_A,column)
print(condition)
print("Enter Matrix B:")
input_matrix(row,row_B,column)

for j in range(column):
    BT_row=[]
    for k in range(row):
        BT_row.append(row_B[k][j])
    BT.append(BT_row)

for i in range(int(row)):
    rowp = []
    for j in range(int(row)):
        element = 0
        for k in range(int(column)):
            element = element + (int(row_A[i][k]) * int(BT[k][j]))
        rowp.append(element)
    matrix_3.append(rowp)

for r in range(int(row)):
    for c in range(int(row)):
        print(matrix_3[r][c], end=" ")
    print("")
