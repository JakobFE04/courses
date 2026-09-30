import matplotlib
matplotlib.use("QtAgg")

from scipy.fft import fft
from scipy.signal import freqz, lfilter, convolve, correlate
from scipy.io import loadmat
import matplotlib.pyplot as plt 
import numpy as np 

# a)
mat_dict = loadmat("signals.mat")

x = mat_dict["x"][0]

y = mat_dict["y"][0]

n = np.arange(0, len(x))

fig_a, (ax1_a, ax2_a) = plt.subplots(2, 1)

ax1_a.stem(n[0:10], x[0:10], label=r"$x[n]$", linefmt="r")
ax2_a.stem(n, y, label=r"$y[n]$", linefmt="b")

fig_a.legend()
#plt.savefig("task_2_a")

# b)
r_yx = correlate(y,x)

l = np.arange(-255, 256)

fig_b, ax_b = plt.subplots(1)
ax_b.stem(l, r_yx, label=r"$r_{yx}[l]$")
fig_b.legend()
#plt.savefig("task_2_b")


# c)

r_yx_v2 = np.convolve(y, np.flip(x))

fig_c, ax_c = plt.subplots(1)
ax_c.stem(l, r_yx_v2, label=r"$r_{yx}[l]$", linefmt="g")
fig_c.legend()
plt.savefig("task_2_c")

# d)
print(r"Max of r_{yx}[l] is:")
print(f"{np.argmax(r_yx_v2) - 255}")

plt.show()
