import matplotlib
matplotlib.use("QtAgg")
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.signal import freqz, fftconvolve
from scipy.fft import fft, rfft, irfft

fft_l = 128

n_100 = np.arange(0, 100)
n_1000 = np.arange(0, 1000)
n_30 = np.arange(0, 30)
n_10 = np.arange(0, 10)

f_1 = 7/40
f_2 = 9/40 

x_100 = np.sin(2 * np.pi * f_1 * n_100) + np.sin(2 * np.pi * f_2 * n_100)
X_100 = abs(fft(x_100, fft_l))
x_1000 = np.sin(2 * np.pi * f_1 * n_1000) + np.sin(2 * np.pi * f_2 * n_1000)
X_1000 = abs(fft(x_1000, fft_l))
x_30 = np.sin(2 * np.pi * f_1 * n_30) + np.sin(2 * np.pi * f_2 * n_30)
X_30 = abs(fft(x_30, fft_l))
x_10 = np.sin(2 * np.pi * f_1 * n_10) + np.sin(2 * np.pi * f_2 * n_10)
X_10 = abs(fft(x_10, fft_l))

f = np.linspace(0, 0.5, fft_l)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(10,10))
ax1.plot(f, X_100, label=r"$X_{100}(f)$", c="orange")
ax1.set_xlabel(r"$f$")
ax1.set_ylabel(r"$X_{100}(f)$")
ax1.grid()

ax2.plot(f, X_1000, label=r"$X_{1000}(f)$", c="r")
ax2.set_xlabel(r"$f$")
ax2.set_ylabel(r"$X_{1000}(f)$")
ax2.grid()

ax3.plot(f, X_30, label=r"$X_{30}(f)$", c="g")
ax3.set_xlabel(r"$f$")
ax3.set_ylabel(r"$X_{30}(f)$")
ax3.grid()

ax4.plot(f, X_10, label=r"$X_{10}(f)$", c="b")
ax4.set_xlabel(r"$f$")
ax4.set_ylabel(r"$X_{10}(f)$")
ax4.grid()

fig.suptitle("Task 3 c) 128 Samples")
fig.legend()

plt.show()
