import matplotlib
matplotlib.use("QtAgg")

from scipy.signal import freqz 
import matplotlib.pyplot as plt 
import numpy as np 

alp = 0.9
K = 1

b_upper = [1+alp, -(1+alp)]
a_upper = [2, -2*alp]

b_lower = [1-alp, 1-alp]
a_lower = [2, -2*alp]

w_upper, h_upper = freqz(b_upper, a_upper)
w_lower, h_lower = freqz(b_lower, a_lower)

fig, (ax1, ax2) = plt.subplots(2,1,)

ax1.plot(w_upper, 20 * np.log10(abs(h_upper)), 'C0', label=r"Upper")
#ax1.set_xlabel(r"$\omega$")
ax1.set_ylabel(r"$|H(e^{j\omega})|$")
ax2.plot(w_lower, 20 * np.log10(abs(h_lower)), 'r', label=r"Lower")
ax2.set_xlabel(r"$\omega$")
ax2.set_ylabel(r"$|H(e^{j\omega})|$")

tick_positions = [0, np.pi/2, np.pi]
tick_labels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']
ax1.set_xticks(tick_positions)
ax1.set_xticklabels(tick_labels)
ax2.set_xticks(tick_positions)
ax2.set_xticklabels(tick_labels)

fig.legend()
plt.savefig("task_3_b")
plt.show()




