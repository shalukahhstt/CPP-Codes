# make a function to input the matrix
def matrix_input(row,matrix,column,x):
    for i in range(row):
        matrix.append(input().split()) #insert the input to the matrix list
        if len(matrix[i])!=column: #check if the row is valid
            print("Invalid Matrix")
            x = 0 #take x as a condition to stop the program if matrix is invalid
            break
        else:
            x = 1 #take x=1 if there is no issue in the input
            continue
    return x
def m_transpose(matrix):
    #use zip to get the transpose of the given matrix and add it to a list
    transpose = list(zip(*matrix))
    transpose = [list(row) for row in transpose]
    return transpose
def matrix_multiply(row,column,A,transpose,matrix):
    # Multiplication of the Matrices
    for i in range(row):
        row_matrix = []
        for j in range(row):
            row_sum = 0
            for k in range(column):
                # multiply the corresponding elements of each matrix and take sum to row_sum
                row_sum = row_sum + int(A[i][k]) * int(transpose[k][j])
            # input row_sum to a matrix
            row_matrix.append(row_sum)
        # input row_matrix to the matrix
        matrix.append(row_matrix)
    return
def output(matrix):
    #output the matrix as given
    for x in matrix:
        for y in x:
            print(y, end=" ")
        print("")
    return

try :
    #input the dimensions of the matrix as list and split them as row and column
    dimension=input("Enter the dimension: ").split(',')
    row = int(dimension[0])
    column = int(dimension[1])
    A = []
    B = []
    row_matrix = []
    matrix = []
    condition = 0   #This helps to stop the program if the matrix is invalid
    #input matrix A
    print("Enter Matrix A: ")
    condition = matrix_input(row,A,column,condition)
    if condition == 1:
        #input matrix B
        print("Enter Matrix B: ")
        condition = matrix_input(row,B,column,condition)
        if condition == 1:
            # Get the transpose of the function B using m_transpose function
            BT = m_transpose(B)
            #get the multiplication of A and transpose of B matrix
            matrix_multiply(row,column,A,BT,matrix)

            #print the matrix
            output(matrix)
except :
    print("Error")  #shows if there's an error in the inputs of the matrix