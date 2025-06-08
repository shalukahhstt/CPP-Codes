import fileinput
import os

os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
from cs1033_evaluator import evaluate_lab7

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()


################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
    ################## YOUR CODE STARTS HERE. ######################################
    file = open(file_name,"r")
    data_list = list(file.readlines())
    for i in data_list:
        speed.append(int(i.split()[1]))
    file.close()
    ################## YOUR CODE ENDS HERE. ########################################
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
    speed_ms = []
    speed_kmh = get_speed(filename)
    for i in speed_kmh:
        speed_ms.append("%.4f" %(i*5/18))
    return speed_ms


################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
model1_speed = convert_kmph_to_ms(MODEL_1_INPUT_FILE)
model2_speed = convert_kmph_to_ms(MODEL_2_INPUT_FILE)
model3_speed = convert_kmph_to_ms(MODEL_3_INPUT_FILE)

################## YOUR CODE ENDS HERE. ########################################


# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    # Acceleration list is initialized to zero.
    # i.e. acceleration at time=0 is zero.
    acceleration = [0]
    time_intervals = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    ################## YOUR CODE STARTS HERE. ######################################
    # Write the code to calculate the acceleration.
    for i in range(len(speeds)):
        if time_intervals[i] == 0:
            continue
        else:
            acceleration.append((float(speeds[i])-float(speeds[i-1]))/((time_intervals[i]-time_intervals[i-1])*0.001))

    ################## YOUR CODE ENDS HERE. ########################################
    return acceleration


######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

# Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable
# names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
time = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
model_acceleration1 = get_acceleration(model1_speed)
model_acceleration2 = get_acceleration(model2_speed)
model_acceleration3 = get_acceleration(model3_speed)
output_file = open("max_acceleration.txt","w")
output_file.write('model1 '+str(round(max(model_acceleration1),2)) + '\n')
output_file.write('model2 '+str(round(max(model_acceleration2),2)) + '\n')
output_file.write('model3 '+str(round(max(model_acceleration3),2)) + '\n')
# Plotting the lines with different styles
plt.plot(time, model_acceleration1 , label='model_1')
plt.plot(time, model_acceleration2 , label='model_2')
plt.plot(time, model_acceleration3 , label='model_3')

# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.show()
output_file.close()

################################################################################
# Please do not edit anything below this line.
evaluate_lab7()

##################### End of the programme #####################################