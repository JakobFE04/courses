# Problem 1) 
![[Pasted image 20260828111529.png|700]]


# Problem 2)
## a)
Since the discrete time signal is periodic in the frequency domain with $f_{1 }\epsilon \ [-\frac{1}{2} \frac{1}{2})$ or $[0,1)$ we get that:
$$
 \begin{equation} 
 f_{1}=\frac{F_{1}}{F_{s}} \implies F_{1}=f_{1}\cdot F_{s} = [-3000, 3000) Hz 
 \end{equation} 
$$
## b)
The code i used:
```python
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


F_S = 1000
f_1 = 0.3
F_1 = f_1 * F_S

t_total = 4

N = np.arange(0, t_total, 1/F_S) # Getting F_S samples from 0 to 4 seconds

def x_func(t):
    return np.array(np.cos(2 * np.pi * F_1 * t))

x = x_func(N) # 4 seconds of x[n]

sd.default.device = 7
sd.play(x)
sd.wait()
```
****
## c)
When i use a total of 4 seconds, i get a short light "beep" for $F_{s}=1000$ Hz and a slightly longer one for $F_{s}=3000$ Hz. With $F_{s}=12000$ Hz I can hear it "flicker" a bit. See b) for code i used.

## d)
For $F_{1}=1000$ Hz i got a really high pitch tone, for $F_{1}=6000$ Hz i got a slightly deeper tone. But with $F_{1}=3000$ Hz the tone got really dark. I think this has to do with the periodicity from the normalised frequency, as $f_{1}=0.75$ or $0.25$ for $1-f_{1}$ for $F_{1}=6000$ Hz, while for 1000 Hz $f_{1}=0.125$ and for 3000 Hz $f_{1}=0.375$ which is alot closer to the edge of 0.5.


# Problem 3)
![[Pasted image 20260824185425.png]]
## a)
Its time-invariant, as there is no factor $n$ outside of the $x[n]$ that the system depends on. Its causal as it depends on current or past values. $x^2[n-1]$ is non-linear as its squared.

## b)
Its linear, as all factors in the system is linear so the superposition principle still holds. Its causual as it depends on future values in $2x[n-2]$. Its time-variant because it has a factor $n$ in $nx[n]$.

## c)
Its linear, time-invariant and causal. All linear factors so superposition counts and no $n$ factors outside of the $x[n]$. Its causal since it depends current or past values..

## d)
This is a linear, time-invariant and non-causal system. All linear factors so superposition counts, no $n$ factors outside of the $x[n]$ and it depends on future values in $3x[n+4]$.

# Problem 4)

![[Pasted image 20260828111514.png|650]]

# Problem 5)
## a)
![[problem5_a.png]]
$$
 \begin{equation} 
 y_{1}[n] = [1,3,6,5,3]
 \end{equation} 
$$

## b)
![[problem5_b.png]]


## c)
The length of $y_{1}$ is given by:
$$
 \begin{equation} 
 \texttt{len(y\_1) = len(x) + len(h\_1) - 1}
 \end{equation} 
$$
And then $y_{2}$ is given by:
$$
 \begin{equation} 
 \texttt{len(y\_2) = len(y\_1) + len(h\_2) - 1} 
 \end{equation} 
$$
Which gives:
$$
 \begin{equation} 
 (3 + 3 - 1) + 11 - 1 = 15
 \end{equation} 
$$

## d) 
Swapping $h_{1}[n]$ and $h_{2}[n]$ and getting $y_{3}[n]$ and $y_{4}[n]$ instead:
![[problem5_d.png]]

We can clearly see that $y_{1}[n]$ and $y_{3}[n]$ are different as they are the convolution of $x[n]$ with $h_{1}[n]$ and $h_{2}[n]$ respectively. However we can see that associative propery of convolution from $y_{2}[n]=y_{4}[n]$ as the order of the subsystems in a system only matters for the outputs in between the subsystems. The total output does not.

Code:
```python
import numpy as np 
import matplotlib.pyplot as plt

# a)
x = np.array([0, 1, 2, 3, 0,])

h_1 = np.array([0, 1, 1, 1, 0,])

h_2 = np.array([0] + [0.9**n for n in range(0, 11, 1)] + [0])

y_1 = np.convolve(x, h_1, "full")

n_1 = np.arange(0, len(y_1))

fig_1, ax1 = plt.subplots()
ax1.stem(n_1, y_1, label="y_1[n]")
ax1.set_ylabel("Amplitude")
ax1.set_xlabel("n")
ax1.legend()
plt.savefig("problem5_a.png")

# b)
y_2 = np.convolve(y_1, h_2, "full")

n_2 = np.arange(0, len(y_2))

fig_2, ax2 = plt.subplots()
ax2.stem(n_2, y_2, label="y_2[n]")
ax2.set_ylabel("Amplitude")
ax2.set_xlabel("n")
ax2.legend()
plt.savefig("problem5_b.png")

# d)
y_3 = np.convolve(x, h_2, "full")

n_3 = np.arange(0, len(y_3))

y_4 = np.convolve(y_3, h_1, "full")

n_4 = np.arange(0, len(y_4))


fig, ax = plt.subplots(2,2, layout="constrained")
ax[0,0].stem(n_1, y_1, label="y_1[n]")
ax[0,0].set_ylabel("Amplitude")
ax[0,0].set_xlabel("n")
ax[0,0].legend()


ax[0,1].stem(n_2, y_2, label="y_2[n]")
ax[0,1].set_ylabel("Amplitude")
ax[0,1].set_xlabel("n")
ax[0,1].legend()


ax[1,0].stem(n_3, y_3, label="y_3[n]")
ax[1,0].set_ylabel("Amplitude")
ax[1,0].set_xlabel("n")
ax[1,0].legend()

ax[1,1].stem(n_4, y_4, label="y_4[n]")
ax[1,1].set_ylabel("Amplitude")
ax[1,1].set_xlabel("n")
ax[1,1].legend()

plt.savefig("problem5_d.png", dpi=300)



```