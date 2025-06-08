student_marks = []
#Start a Loop to input marks

for i in range(0,4):

    mark = input().split()
    #convert string elements in the mark list into integer
    mark = [int(x) for x in mark]
    #input mark list into the 2D list student_marks
    student_marks.append(mark)

for j in student_marks:

    #find the total and average of each students seperatly
    total = sum(j)
    average = total/3
    average = round(average,1)

    #print Total and Average of each student
    print("Total:", total , "Average:",average)