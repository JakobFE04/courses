import matplotlib
matplotlib.use("QtAgg")

from scipy.fft import fft
from scipy.signal import freqz 
import matplotlib.pyplot as plt 
import numpy as np 

L = 500 
A_x = A_y = 0.25
f_x = 0.04 
f_y = 0.10
n = np.arange(0, L)

d = A_x * np.cos(2*np.pi*f_x*n) + A_y * np.cos(2*np.pi*f_y*n)
e = np.random.normal(size=L)
g = d + e

D_mag = abs(fft(x=d, n=2048)) / 2048
G_mag = abs(fft(x=g, n=2048)) / 2048
freq_steps = np.arange(0, 2048)


fig, (ax1, ax2,) = plt.subplots(2,2, figsize=(15,8))

ax1[0].stem(n, d, label=r"$d[n]$")
ax1[1].plot(freq_steps, D_mag, label=r"$|D(f)|$", c="blue")
ax1[1].set_xlabel(r"$f$")
ax1[1].set_ylabel(r"$|D(f)|$",)
ax1[0].set_ylabel(r"$d[n]$",)
ax1[0].set_xlabel(r"n")



ax2[0].stem(n, g, label=r"$g[n]$", linefmt="r")
ax2[1].plot(freq_steps, G_mag, label=r"$|G(f)|$", c="orange")
ax2[0].set_xlabel(r"$n$")
ax2[0].set_ylabel(r"$g[n]$")
ax2[1].set_xlabel(r"$f$")
ax2[1].set_ylabel(r"$|G(f)|$",)

#tick_positions = [0, np.pi/2, np.pi]
#tick_labels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']
#ax1.set_xticks(tick_positions)
#ax1.set_xticklabels(tick_labels)
#ax2.set_xticks(tick_positions)
#ax2.set_xticklabels(tick_labels)
fig.suptitle("Task 4 a)")
fig.tight_layout(pad=1.0)
fig.legend()
plt.savefig("task_3_b")
plt.show()

