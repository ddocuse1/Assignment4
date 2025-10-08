import math
import numpy as np
import matplotlib.pyplot as plt
k = 1.3807e-23
sl = 299792458
v = [0.6e9,1.2e9,2.4e9,4.8e9,9.6e9,22e9]
a = [2e-4,4e-4,8e-4,1.6e-3,3.2e-3,7e-3]
b = [1.15,1.18,1.2,1.23,1.26,1.3]
d = [0.0025,0.0027,0.003,0.0033,0.0036,0.004]
D = [0,50,100,170,250,375]
F = [7.59342e-21,6.15189e-20,3.90419e-19,1.86758e-18,8.12656e-18,4.14506e-17]
Tf = []
def func(T,n):
    return ((2*k*v[n]**2)/(sl**2))*(T/(1+d[n]*T**0.5))*(1-math.e**(-1*a[n]*T**b[n]))

g1,g2 = 0,1000

c=(g1+g2)/2

for i in range(6):
    while (np.abs(func(c,i)-F[i]))/F[i] > 0.00001:
        c=(g1+g2)/2
        if (func(g1,i) - F[i])*(func(c,i) - F[i]) < 0:
            g2 = c
        else:
            g1 = c
    Tf.append(c)
    c=(g1+g2)/2
    g1,g2 = 0,1000
plt.plot(Tf,D)
plt.xlabel("Temperature (K)")
plt.ylabel("Depth (m)")
plt.title("Temperature vs Depth")
plt.savefig("mwrTemperature.png")
