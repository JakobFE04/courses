import matplotlib 
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt 
import numpy as np 

z_list = np.linspace(-2*np.pi, 2*np.pi, 100)
t_plus = np.linspace(0, 5, 100)

t, z = np.meshgrid(t_plus, z_list)
f = np.cos(z - t)
f_inv = np.cos(z + t)

fig, (ax, ax2) = plt.subplots(1, 2, subplot_kw={'projection': '3d'})

ax.plot_surface(t,z,f, cmap="viridis", label="f(t,z)=cos(z-t)")
ax.set_xlabel("Time [t]")
ax.set_ylabel("z")
ax.set_zlabel("f(z,t)")
tick_positions = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
tick_labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
ax.set_yticks(tick_positions)
ax.set_yticklabels(tick_labels)



ax2.plot_surface(t,z,f_inv, cmap="magma", label="f(t,z)=cos(z+t)")
ax2.set_xlabel("Time [t]")
ax2.set_ylabel("z")
ax2.set_zlabel("f(z,t)")
tick_positions = [-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
tick_labels = [r'$-2\pi$', r'$-\frac{3\pi}{2}$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$']
ax2.set_yticks(tick_positions)
ax2.set_yticklabels(tick_labels)
fig.legend()


#plt.savefig("taks_3.png")
plt.show()


