import math
import matplotlib.pyplot as plt
o=[]
vcl=[]

for i in range (0,361):
    tita=math.radians(i)
    tita1=(math.pi/2)-tita
    bd=(((10**2)+(37**2)-(2*10*37*math.cos(tita)))**0.5)
    bcd=math.acos(((42**2)+(34**2)-(bd**2))/(2*42*34))
    adc=math.asin((10*math.sin(tita))/bd)+math.asin((42*math.sin(bcd))/bd)
    tita2=adc-(math.pi/2-bcd)
    tita3=adc-math.pi/2
    vc=(8*math.sin(tita1-tita2))/(math.sin(tita2-tita3))
    tita=math.degrees(tita)
    o.append(tita)
    print((tita1-tita2)*180/(math.pi),(tita2-tita3)*180/(math.pi))
    if vc<0:
        vc = vc*(-1)
    vcl.append(vc)
    print(i,round(vc,4))


plt.plot(o,vcl)
plt.xlabel('Crank angle (degree)')
plt.ylabel('|Vc| (cms-1)')
plt.title('Crank angle (θ) vs Absolute Velocity of point C (Vc)')
plt.grid()
plt.show()