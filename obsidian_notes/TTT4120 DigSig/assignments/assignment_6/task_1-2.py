import matplotlib
matplotlib.use("QtAgg")
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.signal import freqz, fftconvolve
from scipy.fft import fft, rfft, irfft


# a)

N_x = 28
n = np.arange(0, N_x)
x = 0.9**n 

w, X = freqz(x, worN=2048, whole=True)

f = w / (2 * np.pi)

mag_X = abs(X) / 2048

fig1, ax1 = plt.subplots(1)
ax1.plot(f, mag_X, label=r"$|X(f)|$",)
ax1.grid()
ax1.set_xlabel(r"$f$")
ax1.set_ylabel("|X(f)|")
fig1.legend()
fig1.suptitle("Task 1 a)")




# b)
X_N = fft(x, N_x)
X_N_4 = fft(x, int(N_x/4))
X_N_2 = fft(x, int(N_x/2))
X_2N = fft(x, 2*N_x)

# c)

# Relationship between DFT index k and normalized frequency f is f = k / N 
# f for k=1:

f_N = 1 / N_x
f_N_4 = 1 / (N_x/4) 
f_N_2 = 1 / (N_x/2) 
f_2N = 1 / (2*N_x) 

print(r"$f_N$ is", f_N)
print(r"$f_{N_4}$ is", f_N_4)
print(r"$f_{N_2}$ is", f_N_2)
print(r"$f_2N$ is", f_2N)


# d)


mag_X_N = np.abs(X_N) * f_N
mag_X_N_4 = np.abs(X_N_4) * f_N_4
mag_X_N_2 = np.abs(X_N_2) * f_N_2
mag_X_2N = np.abs(X_2N) * f_2N

f_n = np.arange(0, 1, f_N)
f_n_4 = np.arange(0, 1, f_N_4)
f_n_2 = np.arange(0, 1, f_N_2)
f_2n = np.arange(0, 1, f_2N)

fig2, ((ax2, ax3), (ax4, ax5)) = plt.subplots(2,2, figsize=(10,10))
ax2.stem(f_n, mag_X_N, label=r"$|X_N(f)|$",)
ax2.grid()
ax2.set_xlabel(r"$f$")
ax2.set_ylabel(r"$|X_N(f)|$")


ax3.stem(f_n_4, mag_X_N_4, label=r"$|X_{N_4}(f)|$", linefmt="r")
ax3.grid()
ax3.set_xlabel(r"$f$")
ax3.set_ylabel(r"$|X_{N_4(f)}|$")


ax4.stem(f_n_2, mag_X_N_2, label=r"$|X_{N_2}(f)|$", linefmt="g")
ax4.grid()
ax4.set_xlabel(r"$f$")
ax4.set_ylabel(r"$|X_{N_2}(f)|$")


ax5.stem(f_2n, mag_X_2N, label=r"$|X_{2N}(f)|$",linefmt="b")
ax5.grid()
ax5.set_xlabel(r"$f$")
ax5.set_ylabel(r"$|X_{2N}(f)|$")

fig2.legend()
fig2.suptitle("Task 1 d)")


# Problem 2 

# a) 

N_h = 9 

h_n = np.ones(N_h)

y_n = np.convolve(x, h_n, "full")
N_y = N_x + N_h - 1

n_y = np.arange(0, N_y)

fig3, ax6 = plt.subplots(1)
ax6.stem(n_y, y_n, label=r"$y[n]$", linefmt="orange")
ax6.grid()
ax6.set_xlabel(r"$n$")
ax6.set_ylabel(r"$y[n]$")
fig3.legend()
fig3.suptitle("Task 2 a), len(y)=36")

# b)

X_f = rfft(x, N_y)

H_f = rfft(h_n, N_y)

Y_f = X_f * H_f

#Y_f = fftconvolve(x, h_n, mode="full")


y_n = np.arange(0, N_y)
y_n_4 = np.arange(0, int(N_y/4))
y_n_2 = np.arange(0, int(N_y/2))
y_2n = np.arange(0, 2*N_y)



y_N = irfft(Y_f, n=N_y)
y_N_4 = irfft(Y_f, n=int(N_y/4))
y_N_2 = irfft(Y_f, n=int(N_y/2))
y_2N = irfft(Y_f, n=2*N_y)

fig4, ((axa, axb), (axc, axd)) = plt.subplots(2,2, figsize=(10,10))
axa.stem(y_n, y_N, label=r"$|y_N(n)|$",)
axa.grid()
axa.set_xlabel(r"$n$")
axa.set_ylabel(r"$|y_N(n)|$")


axb.stem(y_n_4, y_N_4, label=r"$|y_{N_4}(n)|$", linefmt="r")
axb.grid()
axb.set_xlabel(r"$n$")
axb.set_ylabel(r"$|y_{N_4(n)}|$")


axc.stem(y_n_2, y_N_2, label=r"$|y_{N_2}(n)|$", linefmt="g")
axc.grid()
axc.set_xlabel(r"$n$")
axc.set_ylabel(r"$|y_{N_2}(n)|$")


axd.stem(y_2n, y_2N, label=r"$|y_{2N}(n)|$",linefmt="b")
axd.grid()
axd.set_xlabel(r"$n$")
axd.set_ylabel(r"$|y_{2N}(n)|$")

fig4.legend()
fig4.suptitle("Task 2 b)")



plt.show()





