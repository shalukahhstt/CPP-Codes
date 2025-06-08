from cs1033_evaluator import evaluate_lab8
# Please do not edit anything above this line.
################################################################################
#import math library to calculate cosines
import math
#Function to calculate for series circuit
def analyseSeriesCircuit(R,L,C,V,f):
    #get the angular frequency as w
    w = 2*f*math.pi
    #get the inductance as L in Henries
    L = L*10**(-3)
    #get the conductance as c in Farads
    C = C*10**(-6)
    #get the impedence of the inductor as z_L
    z_L = w*L
    #get the impedence of the capacitor as z_c
    z_c = 1 / (w*C)
    #get the total impedence as z_tot
    z_tot = math.sqrt((R**2)+(z_L-z_c)**2)
    #get the cuurent through the circuit as I
    I = V/z_tot
    #get the Phase angle in radians
    tita_rad = math.atan((z_L-z_c)/R)
    #get the Phase angle in degrees
    tita_degree = tita_rad*180/math.pi
    #make the output and get it to variable
    output_line = (str("%.1f"%z_L)+" "+str("%.1f"%z_c)+" "+str("%.1f"%z_tot)+" "+str("%.1f"%I)+" "+str("%.1f"%tita_degree))
    return output_line
#Function to calculate for series circuit
def analyseParallelCircuit(R,L,C,V,f):
    #get the angular frequency as w
    w = 2*f*math.pi
    #get the inductance as L in Henries
    L = L*10**(-3)
    #get the conductance as c in Farads
    C = C*10**(-6)
    #get the impedence of the inductor as z_L
    z_L = w*L
    #get the impedence of the capacitor as z_c
    z_c = 1 / (w*C)
    #get the total impedence as z_tot
    z_tot_inverse = math.sqrt((1/(R**2))+((1/z_L)-(1/z_c))**2)
    z_tot = z_tot_inverse**(-1)
    #get the cuurent through the circuit as I
    I = V*z_tot_inverse
    #get the Phase angle in radians
    tita_rad = math.atan(((1/z_L)-(1/z_c))*R)
     #get the Phase angle in degrees
    tita_degree = tita_rad*180/math.pi
    #make the output and get it to variable
    output_line = (str("%.1f"%z_L)+" "+str("%.1f"%z_c)+" "+str("%.1f"%z_tot)+" "+str("%.1f"%I)+" "+str("%.1f"%tita_degree))
    return output_line
#read the data in the input file
f_name = input()
input_f = open(f_name,"r")
#add all the lines in the file to a list
line_list = list(input_f.readlines())
#close the file
input_f.close()
#Create a new file as result.txt
output_f = open("result.txt","w")
for j in line_list:
    #get the j th element in the line_list and split by " " and take it as list i
    i = j.split()
    #get the values for R,L,C,v,f from the data in i
    R = float(i[1])
    L = float(i[2])
    C = float(i[3])
    V = float(i[4])
    f = float(i[5])
    #check whether the circuit is series or parallel
    if i[0] == "series":
        output = analyseSeriesCircuit(R,L,C,V,f)
    elif i[0]  == "parallel":
        output = analyseParallelCircuit(R,L,C,V,f)
    #write the output data in output_f(output file)
    output_f.write(output + '\n')
#close the output file
output_f.close()
# Your code should be included here.
# You should define and use the analyseSeriesCircuit(), analyseParallelCircuit() functions in your solution.


################################################################################
# Please do not edit anything below this line.
evaluate_lab8()

##################### End of the programme #####################################