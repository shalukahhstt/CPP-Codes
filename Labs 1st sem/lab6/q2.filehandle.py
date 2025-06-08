from datetime import datetime
#from cs1033_evaluator import evaluate_L6_E2

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################

#Take file name as f_name
f_name = input()
#open f_name file as a read only file
file = open(f_name, "r")
#input all the lines in the file to line_list
line_list = list(file.readlines())
#make a new file as output.txt and open it
output_file = open("output.txt", "w")
#make 2 empty lists as main and duplicates
main = []
duplicates = []
#check for every elements in line_list
for i in line_list:
    #split the element i and add that to list2
    list2 = i.split()
    #check if the person is a male or female and take days to birthday using the function "days_to_birthday" and take it as birth_days
    if list2[2] == 'M':
        birth_days = days_to_birthday(list2[1])
    elif list2[2] == 'F':
        birth_days = days_to_birthday(list2[1]) + 500 #add 500 if the person is a female
    #input the date into list3 by spliting from '-'
    list3 = list2[1].split('-')
    #append the only the year from list3 to the year
    year = int(list3[0])
    #check if there are any repetions of that year
    if year in main:
        #if the year already added add that year to duplicates and take the year count as given
        duplicates.append(year)
        year_count = int(duplicates.count(year))+1
    else:
        #if year is looping 1st time append it to main and take year count as 1
        main.append(year)
        year_count = 1
    #use if conditions and create the last 3 digits of the id using year count
    if year_count < 10 :
        last_digits = "00"+ str(year_count)
    elif year_count < 100:
        last_digits = "0"+ str(year_count)
    else:
        last_digits = str(year_count)
    #use if conditions and create middle 3 digits using birth_days and take it as middle digits
    if birth_days < 10:
        middle_digits = "00"+ str(birth_days)
    elif birth_days < 100:
        middle_digits = "0"+ str(birth_days)
    else:
        middle_digits = str(birth_days)
    #create the id number 1st 4 digits is year and middle 3 digits is middle_digits and last_digits at the end
    id_sub = str(year)+ middle_digits + last_digits
    #make a new variable and iput the line we need to write in the output file which is "name ID number"
    new_data = str(list2[0]) + " " + id_sub
    #write new_data in the output file use \n to break the line and start a new one
    output_file.write(new_data + '\n' )
#close input file and output file
file.close()
output_file.close()


################################################################################
# Please do not edit anything below this line.
#evaluate_L6_E2()

##################### End of the programme #####################################