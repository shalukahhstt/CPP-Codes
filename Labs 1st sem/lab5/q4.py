matrix = []
r=1
row_length = []
row = []
y=0
q=1
try:
    while r > 0:
        row = input().split()
        row = [int(x) for x in row]
        if len(row)==1 and row[0]==-1 :
            break
        else:
            matrix.append(row)
    for k in matrix:
        row_length.append(len(k))
    for z in range(0,len(matrix)-1):
        if row_length[z] != row_length[z-1]:
            q=0
            break
        else:
            q=1
    if q==0:
        print("Invalid Matrix")
    else:
        y = row_length[0]
        for i in range(y):
            for j in range(len(matrix)):
                print(matrix[j][i],end=" ")
            print("")
except:
    print("Error")