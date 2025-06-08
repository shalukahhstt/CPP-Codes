#Input the file name into f_name
f_name = input()
#open the f_name as a read only file get that to new_file
new_file = open(f_name,"r")
#save every line in new_file into the list, line_list
lines_list = list(new_file.readlines())
#make a variable to count how many beams included in the file
beam_count = 0
#check every line in the line_list and take the ith element
for i in lines_list:
    #add 1 to beam_count to get the count in the each loop
    beam_count = beam_count +1
    #split i by space and take it as data list
    data = i.split(" ")
    #take each element of the data and convert them to floating numbers and take them to variables as shown below
    length = float(data[0])
    Y_Modulus = float(data[1])*(10**9)
    Inertia = float(data[2])
    load = float(data[3])*1000
    #calculate the max deflection and max bending stress as below
    D_max = load*(length**3)/(48*Inertia*Y_Modulus)
    S_max = load*length/(4*Inertia)
    #output the beam number,length,d_max,s_max and use %f to round the numbers to floating points
    print("Beam "+str(beam_count)+": Length: "+str(length)+" m, Max Deflection:","%.6f" %D_max,"m, Max Bending Stress:","%.2f" %S_max,"Pa")