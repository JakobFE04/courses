import matplotlib 
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import numpy as np 


beta = 2 * np.pi
E_0 = 1 

z = np.linspace(0, 10, 100)
E_x_2 = E_0 * np.e**(-2 * z) * np.cos(beta * z)
E_x_1 = E_0 * np.e**(-1 * z) * np.cos(beta * z)
E_x_0_5 = E_0 * np.e**(-1/2 * z) * np.cos(beta * z)

plt.plot(z, E_x_2, label=r"$\alpha=2$", c="r")
plt.plot(z, E_x_1, label=r"$\alpha=1$", c="b")
plt.plot(z, E_x_0_5, label=r"$\alpha=0.5$", c="g")
plt.title(r"$\beta=2\pi$, $E_0=1$")
plt.xlabel(r"$z$")
plt.ylabel(r"$E_x$")
plt.legend()
plt.grid()
plt.show()
