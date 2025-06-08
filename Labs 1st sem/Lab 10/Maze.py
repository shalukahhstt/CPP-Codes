# virtical lines of each cell on each row
coord_vertical = ['100010010001001', '110011000100011', '000101011000101', '111000100100111' ,'111110001010011' ,
'111111011101011', '110111100111111', '111111101110111', '111011010111001' ,'100010010001111',
'111000101001111', '101101011001100' ,'110110011001011', '100001000000001' ]

# horizontal lines of each cell on each row
coord_horizontal = [
'11111111111111', '01010101011010', '01110110011110', '00101010111000', '00001111101100',
'00000110010110', '00100010000001', '10000001100000' ,'00000001010100', '01010110100010',
'01111101110000', '10011000011000', '00000110110011', '01101011011110' ,'11111111111111' ]

# Create functions for stack
class Stack:
    def __init__(self):
        self.elements = []

    def push(self, elements):
        self.elements.append(elements)

    def pop(self):
        if not self.delete():
            return self.elements.pop()
        return None

    def peak(self):
        if not self.delete():
            return self.elements[-1]
        return None

    def delete(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

# Create maze as a matrix
maize = []

# creating the maze as a matrix using coord_vertical and coord_horizontal
for i in range(14):
    row_m = []
    for j in range(14):
        # take correct data from v and h for each cell
        cell_value = [coord_horizontal[i][j], coord_vertical[i][j + 1], coord_horizontal[i + 1][j], coord_vertical[i][j]]
        row_m.append(cell_value)
    maize.append(row_m)

def stuck(situation):
    # Check if cell is blocked on all sides
    return situation.count('1') == 4

# Starting position
way = ''
stack = Stack()
stack.push((2, 0))
i, j = stack.peak()
print(f'Start at ( {i} , {j} )')

# program to solve the maize
while True:
    # Exit when the current position is (11, 13)
    if (i, j) == (11, 13):
        # Leaving way
        print(f'{way}Leaving at ( {i} , {j} )')
        break

    # Name the sides of the cell as follows
    North = maize[i][j][0]
    East = maize[i][j][1]
    South = maize[i][j][2]
    West = maize[i][j][3]

    if North == '0':
        # Block the side of North
        maize[i][j][0] = '1'
        way += 'North '
        # Change the current position
        i -= 1
        maize[i][j][2] = '1'  # Block the side of South

    elif East == '0':
        # Block the side of East
        maize[i][j][1] = '1'
        way += 'East '
        # Change the current position
        j += 1
        maize[i][j][3] = '1'  # Block the side of West

    elif South == '0':
        # Block the side of South
        maize[i][j][2] = '1'
        way += 'South '
        # Change the current position
        i += 1
        maize[i][j][0] = '1'  # Block the side of North

    elif West == '0':
        # Block the side of West
        maize[i][j][3] = '1'
        way += 'West '
        # Change the current location
        j -= 1
        maize[i][j][1] = '1'  # Block the side of East

    # Add coordinates to the stack
    stack.push((i, j))

    # Getting current position
    i, j = stack.peak()

    # Backtrack if stuck
    while stuck(maize[i][j]):
        # Location where stuck
        print(f'{way}Stuck at ( {i} , {j} )')
        # Clear path
        way = ''
        stack.pop()  # Backtrack
        # Getting Previous location (i, j)
        if not stack.delete():
            cp = stack.peak()
            i, j = cp[0], cp[1]
            # Message backtrack
            print(f'Back to ( {i} , {j} )')
        else:
            print('No more paths to backtrack.')
            break
