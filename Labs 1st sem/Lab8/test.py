# Function to calculate the determinant of a matrix
def determinant(matrix):
    # Base case for 2x2 matrix
    if len(matrix) == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:

    # Recursive case for larger matrices
        det = 0
        for i in range(len(matrix)):
            det = det + ((-1) ** (i+2)) * matrix[0][i] * (determinant(minor(matrix, 0, i)))
    return det

# Function to calculate the minor matrix (matrix without a specific row and column)
def minor(matrix, row, column):
    minor_m = []
    for i in matrix[:row]:
        minor_m.append(i[:column] + i[column + 1:])
    for i in matrix[row + 1:]:
        minor_m.append(i[:column] + i[column + 1:])
    print(minor_m)
    return minor_m

# Example matrix (3x3)
matrix = [[2, 3, 1,1],
          [4, 5, 6,1],
          [7, 8, 9,1],
          [7, 5, 9,1]]

# Calculate determinant
det = determinant(matrix)

print(f"Determinant of the matrix is: {det}")

