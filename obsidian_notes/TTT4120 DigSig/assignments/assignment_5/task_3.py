import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.signal import freqz, dlti, dimpulse, lfilter
import sounddevice as sd 
from scipy.io.wavfile import read 


alpha = 0.9
R = 10

fs, x = read("piano.wav")
print(f"fs: {fs}")

x_scaled = x / np.max(x)
#sd.play(x_scaled, fs)
#input("Playing original")

b = np.zeros(R+1)
b[0] = 1 
b[R] = alpha
a = np.zeros(R+1)
a[0] = 1



w, h_w = freqz(b, a, 22050)

filter = dlti(b,a)

t, y_out = dimpulse(filter)
y_impulse = y_out[0].flatten()

y = lfilter(b, a, x)
y_scaled = y / np.max(y)
#sd.play(y_scaled, fs)
#input("Playing filtered")

tick_positions = [0, np.pi/2, np.pi]
tick_labels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(15,5))


ax1.plot(w, h_w, label="Frequency response", c="b")
ax1.set_xlabel(r"$\omega$")
ax1.set_ylabel(r"$H(\omega)$")
ax1.set_xticks(tick_positions)
ax1.set_xticklabels(tick_labels)
ax1.grid()

ax2.plot(t, y_impulse, label="Unit sample response", c="r")
ax2.set_xlabel("n")
ax2.set_ylabel("h[n]")
ax2.grid()



fig.legend()
fig.suptitle("Task 3 c)")

print("Test")
N = 3

e1 = abs(-R-(N-1)*R)
e2 = abs(-2*R-(N-1)*R)

b2 = np.zeros(e2+1)
a2 = np.zeros(e2+1)
#b2 = np.zeros(abs(-2*R-(N-1)*R)+1)
#a2 = np.zeros(abs(-2*R-(N-1)*R)+1)
a2[0] = 1 
b2[0] = 1
b2[R] = alpha
b2[e1] = -alpha**N
b2[e2] = alpha**(N+1)

y2 = lfilter(b2, a2, x)
y2_scaled = y2 / np.max(y2)
#sd.play(y2_scaled, fs)
#input("Playing second filter")


w2, h_w2 = freqz(b2, a2, 22050)
filter2 = dlti(b2, a2)
t2, y2_out = dimpulse(filter2)
y2_impulse = y2_out[0].flatten()

print(len(y2_impulse))
print(len(t2))

fig2, (ax3, ax4) = plt.subplots(1,2, figsize = (10,5))
ax3.plot(w2, h_w2, label="Frequency response", c="b")
ax3.set_xlabel(r"$\omega$")
ax3.set_ylabel(r"$H_2(\omega)$")
ax3.set_xticks(tick_positions)
ax3.set_xticklabels(tick_labels)
ax3.grid()

ax4.plot(t2, y2_impulse, label="Unit sample response", c="r")
ax4.set_xlabel("n")
ax4.set_ylabel(r"h_2[n]")
ax4.grid()

fig2.legend()
ax3.grid()
ax4.grid()


print("Exiting")
plt.show()



