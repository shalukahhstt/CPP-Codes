from cs1033_evaluator import evaluate_lab9

INPUT_FILE_NAME = input()
################################################################################
# Do not change anything above this line
################################################################################
# import re(regex patterns) to select elements from the list
import re


# create a function to take a specific element and get the count
def e_count(element, composition):
    count = 0
    # check if there is the specific element in the composition list and take it to match_elements list
    match_elements = [i for i in composition if re.search(element, i)]
    # check elements in the match_elements and get the count of that element
    for j in match_elements:
        if len(element) == len(j):
            count = count + 1
        else:
            count = count + int(j[len(element):])
    # return the number of elements in the composition as counnt
    return count


# create a function to categorize the material into relevent file
def categroiz(composition, l0, l1, l2, l3, l4):
    # use e_count function and get the element count of the relavent elements
    S_count = e_count('S', composition)
    O_count = e_count('O', composition)
    Na_count = e_count('Na', composition)
    Mg_count = e_count('Mg', composition)
    Cl_count = e_count('Cl', composition)
    # make a variable as count to add data to lvl4 and lvl0
    count = 0
    # check the condition 1 in the problem
    if S_count >= 1 and O_count >= 4 and Na_count >= 1:
        t = 1
        count = count + 1
        S_count -= 1
        O_count -= 4
        Na_count -= 1
    # check the condition 2 in the problem
    if S_count >= 1 and O_count >= 3 and Mg_count >= 1:
        t = 2
        count = count + 1
        S_count -= 1
        O_count -= 3
        Mg_count -= 1
    # check the condition 3 in the problem
    if O_count >= 2 and Cl_count >= 3:
        t = 3
        count = count + 1
    # check the condition 4 in the problem if its true add the material to the relevent file
    if count > 1:
        l4.write(name + '\n')
    # check the condition 5 in the problem if its true add the material to the relevent file
    elif count == 0:
        l0.write(name + '\n')
    # if condition 4 and 5 is false then check condition 1 or 2 or 3 is true and write the name of the material in the relavalent file
    elif count == 1:
        if t == 1:
            # write the material name in l1 file if condition 1 is true(t=1)
            l1.write(name + '\n')
        elif t == 2:
            # write the material name in l2 file if condition 2 is true(t=2)
            l2.write(name + '\n')
        elif t == 3:
            # write the material name in l3 file if condition 3 is true(t=3)
            l3.write(name + '\n')


# Input data from the file and get the lines into a list
f_input = open(INPUT_FILE_NAME, "r")
line_list = f_input.readlines()
# create 5 new files as below to give outputs and take them as l0,l1,l2,l3,l4,l5
l0 = open("Level_0.txt", "w")
l1 = open("Level_1.txt", "w")
l2 = open("Level_2.txt", "w")
l3 = open("Level_3.txt", "w")
l4 = open("Level_4.txt", "w")
# check data in the line_list
for i in line_list:
    # take the name of the material
    name = i.split()[0]
    # take the chemical compostion of the previous substance into a list
    composition = i.split()[1].split('-')
    # use categroiz function to write the material name in the relevent file
    categroiz(composition, l0, l1, l2, l3, l4)

# close all files
l0.close()
l1.close()
l2.close()
l3.close()
l4.close()

# Enter your code here
# Use INPUT_FILE_NAME variable to read the file instead of 'contamination_analysis.txt'


################################################################################
# Do not change anything below this line.
evaluate_lab9()