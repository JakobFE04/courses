from typing import final

import matplotlib
matplotlib.use("QtAgg")

from scipy.fft import fft
from scipy.signal import freqz, lfilter, convolve
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

fig.suptitle("Task 4 a)")
fig.tight_layout(pad=1.0)
fig.legend()



w0_x = 0.04 * 2 * np.pi 
w0_y = 0.10 * 2 * np.pi
r = 0.95

b = [1,0,-1]
a_x = [1, -2*r*np.cos(w0_x), r**2]
a_y = [1, -2*r*np.cos(w0_y), r**2]


w_x, h_x = freqz(b, a_x, 2048)
w_y, h_y = freqz(b, a_y, 2048)

zeros = np.roots(b)
poles_x = np.roots(a_x)
poles_y = np.roots(a_y)

fig3, (ax) = plt.subplots()
theta = np.linspace(-np.pi, np.pi, 1000) 
ax.plot(np.sin(theta), np.cos(theta), '--k')  
ax.set_aspect(1)
ax.plot(np.real(poles_x), np.imag(poles_x), "Xb", label = r"Poles $H_x(z)$")
ax.plot(np.real(poles_y), np.imag(poles_y), "Xg", label = r"Poles $H_x(z)$")
ax.plot(np.real(zeros), np.imag(zeros), "or", label = "Zeros")

fig40, xa1 = plt.subplots()
#xa1.plot(w_x, 20 * np.log10(abs(h_x)), 'blue', label=r"$H_x$")
#xa1.plot(w_y, 20 * np.log10(abs(h_y)), 'orange', label=r"$H_y$")
xa1.plot(w_x, abs(h_x), 'blue', label=r"$H_x$")
xa1.plot(w_y, abs(h_y), 'orange', label=r"$H_y$")
xa1.set_xlabel(r"$\omega$")
xa1.set_ylabel(r"$|H(e^{j\omega})|$")

tick_positions = [0, np.pi/2, np.pi]
tick_labels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']
xa1.set_xticks(tick_positions)
xa1.set_xticklabels(tick_labels)
fig40.legend()


fig3.suptitle("Task 4 b)")
fig3.legend()
ax.grid()



q_x = lfilter(b, a_x, g,)
q_y = lfilter(b, a_y, g,)

Q_x = abs(fft(x=q_x, n=2048)) / 2048
Q_y = abs(fft(x=q_y, n=2048)) / 2048


fig4, (ax5, ax6,) = plt.subplots(2,2, figsize=(15,8))

ax5[0].stem(n, q_x, label=r"$q_x[n]$")
ax5[1].plot(freq_steps, Q_x, label=r"$|Q_x(f)|$", c="blue")
ax5[1].set_xlabel(r"$f$")
ax5[1].set_ylabel(r"$|Q_x(f)|$",)
ax5[0].set_ylabel(r"$q_x[n]$",)
ax5[0].set_xlabel(r"n")



ax6[0].stem(n, q_y, label=r"$q_y[n]$", linefmt="r")
ax6[1].plot(freq_steps, Q_y, label=r"$|Q_y(f)|$", c="orange")
ax6[0].set_xlabel(r"$n$")
ax6[0].set_ylabel(r"$q_y[n]$")
ax6[1].set_xlabel(r"$f$")
ax6[1].set_ylabel(r"$|Q_y(f)|$",)

fig4.suptitle("Task 4 c)")
fig4.tight_layout(pad=1.0)
fig4.legend()


b_combined = convolve(b,b)
a_combined = convolve(a_x, a_y)

zeros_combined = np.roots(b_combined)
poles_combined = np.roots(a_combined)


q = lfilter(b_combined, a_combined, g)
 
Q = abs(fft(x=q, n=2048)) / 2048 

w, h_q = freqz(b_combined, a_combined, 2048)


# pole-zero, q[n], |Q(f)|, |H(w)|

final_fig, (axx1, axx2) = plt.subplots(2,2, figsize=(15,8))
axx1[0].stem(n, q, label=r"$q[n]$", )
axx1[0].plot(n, q, linestyle="dashed", c="purple")
axx1[0].set_xlabel("n")
axx1[0].set_ylabel("q[n]")

axx1[1].plot(freq_steps, Q, label=r"$|Q(f)|$", c="green")
axx1[1].set_xlabel("f")
axx1[1].set_ylabel(r"$|Q(f)|$")

axx2[0].plot(w, abs(h_q), label=r"$|H(e^{j\omega})|$", c="orange")
axx2[0].set_xlabel(r"$\omega$")
axx2[0].set_ylabel(r"$|H(e^{j\omega})|$")
axx2[0].set_xticks(tick_positions)
axx2[0].set_xticklabels(tick_labels)

axx2[1].plot(np.sin(theta), np.cos(theta), '--k')  
axx2[1].set_aspect(1)
axx2[1].plot(np.real(poles_combined), np.imag(poles_combined), "Xb", label = "Poles")
axx2[1].plot(np.real(zeros_combined), np.imag(zeros_combined), "or", label = "Zeros")
axx2[1].grid()
axx2[1].set_xlabel("Re")
axx2[1].set_ylabel("Im")

final_fig.suptitle("Task 4 d)")
final_fig.legend()
final_fig.tight_layout(pad=1.0)
final_fig.savefig(("taks_4_d.png"))


plt.show()
