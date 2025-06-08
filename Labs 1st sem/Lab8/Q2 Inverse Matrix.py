INPUT_FILE_NAME = input()


########################################################################################
# Do not change anything above this line
########################################################################################

# Use INPUT_FILE_NAME variable to read the file instead of 'matrix_data.txt'
# Enter your code here
#Function to get the minor of a matrix
def minor(matrix, row, column):
    minor_m = []
    #select the wich minor we want by selecting row & column and add the elements in the matrix which r not in the given column or row in the correct order
    for i in matrix[:row]:
        minor_m.append(i[:column] + i[column + 1:])
    for i in matrix[row + 1:]:
        minor_m.append(i[:column] + i[column + 1:])
    #output the minor matrix with return
    return minor_m
#Function to get the determinant of a matrix
def determinant(matrix):
    #check whether the matrix is 2x2 or higher
    if len(matrix) == 2:
        #find the determinant of the matrix using given equation
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(len(matrix)):
            #find the determinant of the matrix using given equation and use determinant and minor function here for the equation
            det = det + ((-1) ** (i + 2)) * matrix[0][i] * (determinant(minor(matrix, 0, i)))
    return det
#Function to get the transpose of a matrix
def transpose(matrix):
    matrix_t=[]
    for row in range(len(matrix)):
        m_row=[]
        for column in range(len(matrix)):
            #add elements into the transpose matrix by replacing columns with row or rows with columns
            m_row.append(matrix[column][row])
        matrix_t.append(m_row)
    return matrix_t
#function to give output of a 2D list as a matrix
def output(i,matrix):
    print("Inverse of Matrix " + str(i + 1) + ":")
    #use join and f function to get the output as given in the problem
    for row in matrix:
        print("".join(f"{elem:7.2f}" for elem in row))
#function to read data in the file
def read_data(filename):
    #open the file as a read only file
    file = open(filename, "r")
    #read every line and append all the lines into a list
    lines = list(file.readlines())
    return(lines)
#function to get the inverse of a matrix
def inverse_matrix(dimension,matrix,matrix_det):
    matrix_inverse = []
    #check if the matrix is 2x2 or higher
    #get the equation for 2x2 matrices as below
    if dimension == 2:
        row1 = [matrix[1][1] / matrix_det] + [(matrix[0][1] * (-1) / matrix_det)]
        matrix_inverse.append(row1)
        row1 = [(matrix[1][0] * (-1) / matrix_det)] + [matrix[0][0] / matrix_det]
        matrix_inverse.append(row1)
        #output the inverse matrix
        output(i,matrix_inverse)
    #get the equation for higher matrices than 2x2 as  below
    else:
        for row in range(dimension):
            inverse_row = []
            for column in range(dimension):
                element = (determinant(minor(matrix, row, column)) / matrix_det) * (-1) ** (row + column + 2)
                if str(element) == "-0.0":
                    inverse_row.append(0)
                else:
                    inverse_row.append(element)
            matrix_inverse.append(inverse_row)
        matrix_inverse_transpose = transpose(matrix_inverse)
        #output the inverses matrix
        output(i,matrix_inverse_transpose)
#function to seperate the matrix data in the file
def get_matrix(dimension,line_list,x):
    row_m = []
    matrix = []
    for j in range(dimension):
        row_m.append(line_list[x + 1 + j].split(','))
    for k in row_m:
        row_m2 = []
        for l in k:
            row_m2.append(int(l))
        matrix.append(row_m2)
    return (matrix)
#read the data in the file to a list
line_list=read_data(INPUT_FILE_NAME)
#get how many matrices data are there in the file
matrix_no = int(line_list[0])
#take a variable as x=1 to seperate matrices
x = 1
#start a loop which loops for the number of matrices in the data
for i in range(matrix_no):
    #take the dimension of the i th matrix
    dimension = int(line_list[x])
    #get the data into the 2D matrix list
    matrix=get_matrix(dimension,line_list,x)
    #add the values to x as given to get the next matrix
    x = dimension + 1 + x
    #find the determinent of the matrix
    matrix_det = determinant(matrix)
    #find the inverse of the matrix and output it
    inverse_matrix(dimension,matrix,matrix_det)
