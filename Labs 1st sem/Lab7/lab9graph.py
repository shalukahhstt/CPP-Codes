import fileinput
import os

os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
#from cs1033_evaluator import evaluate_lab7

R2 = 150
R1 = 204
R_L = []
v_new = []
v_in = 12
for i in range(0, 1001, 10):
    R_L.append(i)
    RLR2 = (R2 * i) / (R2 + i)
    v_new.append((v_in * RLR2) / (R1 + RLR2))

plt.plot(R_L, v_new , label='model_3')

# Adding labels and title
plt.xlabel('Resistance(ohms)')
plt.ylabel('Voltage(V)')
plt.title('Voltage Vs Resistance')
plt.grid()
plt.show()

##################### End of the programme #####################################