def matrix_input(dimension):
    row_1 = int(dimension[0])
    column = int(dimension[1])
    matrix = []
    for i in range(row_1):
        input_row = input().split()
        if len(input_row) != column :
            print("Invalid Input")
            break
        else:
            matrix.append(input_row)
    return(matrix)
try:
    matrix_3 = []
    dimension_1 = input().split()
    matrix_1 = matrix_input(dimension_1)
    dimension_2 = input().split()
    matrix_2 = matrix_input(dimension_2)

    if dimension_1[1] != dimension_2[0]:
        print("Invalid Input")
    else:

        for i in range(int(dimension_1[0])):
            row = []
            for j in range(int(dimension_2[1])):
                element = 0
                for k in range(int(dimension_1[1])):
                    element = element + (int(matrix_1[i][k]) * int(matrix_2[k][j]))
                row.append(element)
            matrix_3.append(row)

        for r in range(int(dimension_1[0])):
            for c in range(int(dimension_2[1])):
                print(matrix_3[r][c],end=" ")
            print("")
except:
    print("Error")