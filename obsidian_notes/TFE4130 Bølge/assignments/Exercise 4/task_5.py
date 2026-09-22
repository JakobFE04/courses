import matplotlib
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt 
import numpy as np 

t = np.linspace(0, 5, 100)
w = 2*np.pi

n = 1/1.2
E_0 = 1 


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, subplot_kw={'projection': '3d'})

x = np.linspace(0,5,100)
y = np.linspace(0,5,100)
x_zero = np.zeros(100)
y_zero = np.zeros(100)
E_1 = E_0 * np.cos(w*t)
H_1 = E_0/n * np.cos(w*t)
z_1_H = np.array([x_zero, H_1])
z_1_E = np.array([E_1,y_zero])
ax1.plot_surface(x_zero,y,z_1_H, cmap="viridis", label=r"$H_1$")
ax1.plot_surface(x,y_zero,z_1_E, cmap="magma", label=r"$E_1$")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")


E_2_x = E_0 * np.cos(w*t)
E_2_y = E_0 * np.cos(w*t)
E_2 = np.array([E_2_x, E_2_y])

H_2_x = -E_0/n * np.cos(w*t)
H_2_y = E_0/n * np.cos(w*t)
H_2 = np.array([H_2_x, H_2_y])

ax2.plot_surface(x,y,E_2, cmap="viridis", label=r"$E_2$")
ax2.plot_surface(-x,y,H_2, cmap="magma", label=r"$H_2$")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")



fig.legend()
plt.show()


