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



print(len(y_2))
print(len(y_4))
