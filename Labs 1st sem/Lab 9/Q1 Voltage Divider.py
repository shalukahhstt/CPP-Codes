import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
from cs1033_evaluator import evaluate_lab9


# Your code should be included here.
# Avoid using the print function in the code, as it may cause errors

#create a function to get the voltages in the given range
def out_volt(v_in,v_out,R1,R2,t):
    #calculate the voltage
    voltage = v_in*int(R1)/(int(R1)+int(R2))
    #check if the voltage in the given range
    if voltage <= v_out+t and voltage >= v_out-t:
        voltage = voltage
    #if voltage is not in the range take voltage as 0
    else:
        voltage = 0
    #return the voltage
    return voltage
#create a function to get power dissipation
def p_dissipation(v_in,R1,R2):
    Power_dissipation = (v_in**(2))/(R1+R2)
    return Power_dissipation
#create a function to get the resistances R1 and R2 corresponding to the power dissipation
def calc(resistance,v_in,v_out,i,j,r_list,power_dlist,t):
    R1 = int(resistance[i])
    R2 = int(resistance[j])
    #take the output voltage as voltage
    voltage = out_volt(v_in,v_out,R1,R2,t)
    #check if voltage is 0 or not
    if voltage != 0:
        #get the power dissipation as power_d
        power_d = p_dissipation(v_in,R1,R2)
        #append the corresponding resisatnces to r_list and power_d to power_dlist
        r_list.append([R1,R2])
        power_dlist.append(power_d)
    #return r_list and power_dlist
    return r_list,power_dlist
#open the input file
file_name = input()
input_file = open(file_name,'r')
#input each line in the file to the list line_list
line_list = input_file.readlines()
#close the input_file
input_file.close()
#take to line to 2 different lists
data_1 = line_list[0].split(',')
resistance = line_list[1].split(',')
#take input voltage as v_in output voltage as v_out and tolerence as t
v_in = int(data_1[0])
v_out = int(data_1[1])
t = float(data_1[2])
#create empty lists power-dlist and r_list
power_dlist = []
r_list = []
#start a loop to get resistance in the resistance list
for i in range(len(resistance)-1):
    for j in range(i+1,len(resistance)):
        #case 1: get ith element as R1 jth element as R2
        r_list,power_dlist = calc(resistance,v_in,v_out,i,j,r_list,power_dlist,t)
        #case 2: get ith element as R2 jth element as R1
        r_list,power_dlist = calc(resistance,v_in,v_out,j,i,r_list,power_dlist,t)
#get the minimum power dissipation as min_power_d
min_power_d = min(power_dlist)
#get the index of that power dissipation as e_index
e_index = power_dlist.index(min_power_d)
#find the relevent Resistences using e_index and make the output_data
output_data = str(r_list[e_index][1])+", "+str(r_list[e_index][0])
#create output.txt file
output_file=open("output.txt","w")
#write output_data in the output_file
output_file.write(output_data +'\n')

#part to calculation to plot the graph
R2 = r_list[e_index][0]
R1 = r_list[e_index][1]
R_L = []
v_new = []
#get data for R_L using a for loop
for i in range(0,1001,10):
    R_L.append(i)
    #calculate RL||R2 and v_new
    RLR2 = (R2*i)/(R2+i)
    v_new.append((v_in*RLR2)/(R1+RLR2))

#plotting the graph
import matplotlib.pyplot as plt
plt.plot(R_L, v_new , label='model_3')
# Adding labels and title
plt.xlabel('Resistance(ohms)')
plt.ylabel('Voltage(V)')
plt.title('Voltage Vs Resistance')
plt.grid()
plt.show()

output_file.close()

################################################################################
# Please do not edit anything below this line.
evaluate_lab9()

##################### End of the programme #####################################