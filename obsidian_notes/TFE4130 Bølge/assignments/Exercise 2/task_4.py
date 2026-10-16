import matplotlib 
matplotlib.use("QtAgg")
import matplotlib.pyplot as plt 
import numpy as np 
import cmath

p_0 = 1.21 
c = 343 


f = np.logspace(2, 4, 20)
w = 2 * np.pi * f
m = 0.005  

Z_2 = [p_0 * c + x * m * 1j for x in w]

Z_air = p_0 * c


R = [(z_2 - Z_air)/(z_2 + Z_air) for z_2 in Z_2]

R_mag = [abs(r) for r in R]

alpha = [1 - R**2 for R in R_mag] 


fig, (ax1, ax2) = plt.subplots(2,1, figsize=(15,10))

ax1.semilogx(f, R, label="Reflection factor", c="r")
ax2.semilogx(f, alpha, label="Absorption coefficient", c="b")

ax1.set_xlabel(r"$f$ [Hz]")
ax2.set_xlabel(r"$f$ [Hz]")
ax1.set_ylabel(r"$|R|$")
ax2.set_ylabel(r"$\alpha$")

ax1.grid()
ax2.grid()
fig.legend()
fig.suptitle("Task 4 c)")

plt.show()
