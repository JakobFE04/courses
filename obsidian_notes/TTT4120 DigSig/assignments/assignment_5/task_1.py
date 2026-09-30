import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.signal import freqz, correlate

# c)

n = np.arange(0,51)

a1 = 0.5
a2 = 0.9
a3 = -0.9
a = [a1,a2,a3]

x = [a[0]**n, a[1]**n, a[2]**n]

l = np.arange(-50, 51)

r_xx = [a[0]**abs(l)/(1-a[0]**2), 
        a[1]**abs(l)/(1-a[1]**2), 
        a[2]**abs(l)/(1-a[2]**2),]

f = np.linspace(-0.5, 0.5, 1000)

S_xx = [1/(1 - 2 * np.cos(2 * np.pi * f) + a[0]**2), 
        1/(1 - 2 * np.cos(2 * np.pi * f) + a[1]**2),
        1/(1 - 2 * np.cos(2 * np.pi * f) + a[2]**2),]

fig, (ax1, ax2, ax3) = plt.subplots(3,3, figsize=(15,10))

ax1[0].stem(n, x[0], linefmt="r", label=f"a={a[0]}")
ax2[0].stem(n, x[1], linefmt="g", label=f"a={a[1]}")
ax3[0].stem(n, x[2], linefmt="b", label=f"a={a[2]}")

ax1[0].set_ylabel("x[n]")
ax2[0].set_ylabel("x[n]")
ax3[0].set_ylabel("x[n]")

ax1[0].set_xlabel("n")
ax2[0].set_xlabel("n")
ax3[0].set_xlabel("n")


ax1[1].stem(l, r_xx[0], linefmt="r", )
ax2[1].stem(l, r_xx[1], linefmt="g", )
ax3[1].stem(l, r_xx[2], linefmt="b", )

ax1[1].set_ylabel(r"$r_{xx}[l]$")
ax2[1].set_ylabel(r"$r_{xx}[l]$")
ax3[1].set_ylabel(r"$r_{xx}[l]$")

ax1[1].set_xlabel("l")
ax2[1].set_xlabel("l")
ax3[1].set_xlabel("l")


ax1[2].plot(f, S_xx[0], c="r", )
ax2[2].plot(f, S_xx[1], c="g", )
ax3[2].plot(f, S_xx[2], c="b", )

ax1[2].set_ylabel(r"$S_{xx}[f]$")
ax2[2].set_ylabel(r"$S_{xx}[f]$")
ax3[2].set_ylabel(r"$S_{xx}[f]$")

ax1[2].set_xlabel("f")
ax2[2].set_xlabel("f")
ax3[2].set_xlabel("f")




fig.suptitle("Task 1 c)")
fig.legend()


f_4 = np.linspace(-1/4, 1/4, 100)

S_yy_1 = ( (1 + 2*a[0]*np.cos(2*np.pi*f_4) + a[0]**2) * np.cos(2*np.pi*f_4)**2 ) / ( 1 - 2*a[0]*np.cos(2*np.pi*f_4) + a[0]**2)

S_yy_2 = ( (1 + 2*a[1]*np.cos(2*np.pi*f_4) + a[1]**2) * np.cos(2*np.pi*f_4)**2 ) / ( 1 - 2*a[1]*np.cos(2*np.pi*f_4) + a[1]**2)

S_yy_3 = ( (1 + 2*a[2]*np.cos(2*np.pi*f_4) + a[2]**2) * np.cos(2*np.pi*f_4)**2 ) / ( 1 - 2*a[2]*np.cos(2*np.pi*f_4) + a[2]**2)


fig2, ax = plt.subplots(3,1, figsize=(10,5))
ax[0].plot(f_4, S_yy_1, c="r", label=f"a={a[0]}")
ax[0].set_xlabel("f")
ax[0].set_ylabel(r"$S_{yy}(f)$")
ax[1].plot(f_4, S_yy_2, c="g", label=f"a={a[1]}")
ax[1].set_xlabel("f")
ax[1].set_ylabel(r"$S_{yy}(f)$")
ax[2].plot(f_4, S_yy_3, c="b", label=f"a={a[2]}")
ax[2].set_xlabel("f")
ax[2].set_ylabel(r"$S_{yy}(f)$")
fig2.legend()
fig2.suptitle("Task 1 e)")
plt.show()
