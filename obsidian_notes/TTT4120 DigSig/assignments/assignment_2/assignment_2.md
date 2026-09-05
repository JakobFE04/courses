# Problem 1, 2, 3: a-b
![[Pasted image 20260902171945.png]]

# Problem 3: c-e (And image 1: b)
## c)
![[Problem_1_b.png]]

## d)
It looks like the first system is a lowpass filter as it has a high magnitude for low frequencies and low magnitude for higher frequencies. The second system seems to be a really sharp highpass filter.

## e)
![[Pasted image 20260902171849.png|650]]
```python
import matplotlib.pyplot as plt 
import numpy as np 
from scipy import signal

M = 10 
w = np.linspace(-np.pi, np.pi, 1000)
Y = np.sin(w*(M + 1/2))/(np.sin(w/2))

fig, ax = plt.subplots(2,2, figsize=(10,10))
ax[0,0].plot(w,Y,label="Y(w)")
ax[0,0].set_xlabel(r"w[$\pi$]")
ax[0,0].set_ylabel("Y(w)")
ax[0,0].set_title("Problem_1_b")
ax[0,0].legend()
tick_positions = [-np.pi, -np.pi/2, 0, np.pi/2, np.pi]
tick_labels = [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']
ax[0,0].set_xticks(tick_positions)
ax[0,0].set_xticklabels(tick_labels)


# Problem 3 
# sum a_k y_k[n] = sum b_k x_k[n]

a_1 = [1]
b_1 = [1, 2, 1]

w1, h1 = signal.freqz(b_1, a_1)
mag_1 = np.abs(h1)
phase_1 = np.unwrap(np.angle(h1))


ax[0,1].plot(w1, mag_1, label="Magnitude Sys 1", color="green")
ax[0,1].set_xlabel(r"w")
ax[0,1].set_ylabel(r"$|H_1(w)$")
tick_positions = [0, np.pi/2, np.pi]
tick_labels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']
ax[0,1].set_xticks(tick_positions)
ax[0,1].set_xticklabels(tick_labels)

ax1_2 = ax[0,1].twinx()
ax1_2.plot(w1, phase_1, label="Phase Sys 1", color="red")
ax1_2.set_ylabel(r"$\angle H_1(w)$")

ax[0,1].set_title("Problem_3_c")

a_2 = [1, 0.9]
b_2 = [1]

w2, h2 = signal.freqz(b_2, a_2)
mag_2 = np.abs(h2)
phase_2 = np.angle(h2)

ax[1,1].plot(w2, mag_2, label="Magnitude Sys 2", color="yellow")
ax[1,1].set_xlabel(r"w")
ax[1,1].set_ylabel(r"$|H_2(w)$")
tick_positions = [0, np.pi/2, np.pi]
tick_labels = [r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']
ax[1,1].set_xticks(tick_positions)
ax[1,1].set_xticklabels(tick_labels)

ax2_2 = ax[1,1].twinx()
ax2_2.plot(w2, phase_2, label="Phase Sys 2", color="purple")
ax2_2.set_ylabel(r"$\angle H_2(w)$")

ax[1,1].set_title("Problem_3_c")

fig.legend()
plt.savefig("Problem_1_b.png")

``` 

# Problem 4:
## a)
![[Pasted image 20260902171831.png]]

## b)
```python
import numpy as np
import sounddevice as sd

# Working script to play tones sampled from a cosine!

F_S1 = 4000
F_S2 = 1500
F = 1000
F_PLAYBACK = 44100

t_total = 1

N1 = np.arange(0, t_total, 1/F_S1)
N2 = np.arange(0, t_total, 1/F_S2)

def x_func(t):
    return np.array(np.cos(2 * np.pi * F * t))


x1 = x_func(N1)
x1_play = np.repeat(x1, int(F_PLAYBACK/F_S1))
x2 = x_func(N2)
x2_play = np.repeat(x2, int(F_PLAYBACK/F_S2))


sd.default.device = 7
sd.play(x2_play, samplerate=F_PLAYBACK)
sd.wait()
```

Because one of them is undersampled so the signal gets aliased. This makes it so it sounds like a 500 Hz sine instead of a 1000 Hz as shown in a).

