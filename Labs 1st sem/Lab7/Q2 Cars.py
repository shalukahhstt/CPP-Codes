import fileinput
import os

os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
#from cs1033_evaluator import evaluate_lab7

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()


################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
    ################## YOUR CODE STARTS HERE. ######################################
    file = open(file_name,"r") #open the file_name file as file
    data_list = list(file.readlines()) #read every line in file and add them to data_list
    for i in data_list: # check every ith element in the data list
        speed.append(int(i.split()[1])) #append the 2nd element in i to sppeed list
    file.close() #close the file
    ################## YOUR CODE ENDS HERE. ########################################
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
    speed_ms = []
    speed_kmh = get_speed(filename) #use the previous function to get the speeds to the list
    for i in speed_kmh: #check for every i in speed_kmh list
        speed_ms.append("%.4f" %(i*5/18)) #convert kmh to ms and append them to a list
    return speed_ms


################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
model_speed = []
#use the previous function and add speed lists in ms for each model to the model_speed list
model_speed.append(convert_kmph_to_ms(MODEL_1_INPUT_FILE))
model_speed.append(convert_kmph_to_ms(MODEL_2_INPUT_FILE))
model_speed.append(convert_kmph_to_ms(MODEL_3_INPUT_FILE))

################## YOUR CODE ENDS HERE. ########################################


# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    # Acceleration list is initialized to zero.
    # i.e. acceleration at time=0 is zero.
    acceleration = [0]
    #make the time interval list as the list is same for all 3 times
    time_intervals = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    ################## YOUR CODE STARTS HERE. ######################################
    # Write the code to calculate the acceleration.
    for i in range(len(speeds)):
        #if ith element of time_intervals is 0 the continue the loop else calculate the acceleration and append it to the acceleration list
        if time_intervals[i] == 0:
            continue
        else:
            acceleration.append((float(speeds[i])-float(speeds[i-1]))/((time_intervals[i]-time_intervals[i-1])*0.001))

    ################## YOUR CODE ENDS HERE. ########################################
    return acceleration


######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

# Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable
# names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
#make the time list like previous time
time = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
#create a new file as max_acceleration.txt and get it as output_file
output_file = open("max_acceleration.txt","w")
#make a list to add acceleration of each model
model_acceleration = []
#loop for  3 time for 3 models
for i in range(3):
    #use get acceleration function and append accelerations of model(i+1) as a list to the model_acceleration list
    model_acceleration.append(get_acceleration(model_speed[i]))
    #write the output on the output_file
    output_file.write('model'+str(i+1)+" "+str(round(max(model_acceleration[i]),2)) + '\n')

# Plotting the lines with different styles
    #plot the graphs using data obtained
    plt.plot(time, model_acceleration[i] , label='model_'+str(i+1))


# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.show()
#close the output_file
output_file.close()

################################################################################
# Please do not edit anything below this line.
#evaluate_lab7()

##################### End of the programme #####################################