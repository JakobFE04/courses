# 1)
## a)
$$
 \begin{equation} 
 |E_{1}| = \sqrt{ (-2)^2+4^2 + 1^2 }=\sqrt{ 21 }
 \end{equation} 
$$
## b)
$$
 \begin{equation} 
 E_{3}=E_{1}+E_{2}=\begin{pmatrix}-2 \\
 4 \\
 1 
 \end{pmatrix}  +\begin{pmatrix}0 \\
 1 \\
 1 
 \end{pmatrix} =\begin{pmatrix}-2 \\
 5 \\
 2 
 \end{pmatrix} 
 \end{equation} 
$$
$$
 \begin{equation} 
 W=E_{1}\cdot E_{2}= -2\cdot 0 + 4 \cdot 1 + 1\cdot 1 = 5 
 \end{equation} 
$$
## c)
$$
 \begin{equation} 
 P = E_{1}\times H_{1} = \begin{pmatrix}-2 \\
 4 \\
 1 
 \end{pmatrix} \times \begin{pmatrix}1 \\
 -2 \\
 0 
 \end{pmatrix}  = \begin{pmatrix} 2 \\
  1 \\
  0
 \end{pmatrix}   
 \end{equation} 
$$
## d) 
A phasor notation is a notation used to contain information about the amplitude and phases that are independent of time $t$, like $I_{s}=Ie^{j\phi}$ for a current, that we multiply by $e^{j\omega t}$ and take the real part of:
$$
 \begin{equation} 
 i(t)=\mathrm{Re}\{I_{s}e^{j\omega t}\} 
 \end{equation} 
$$
This is very useful for solving differential equations for time harmonic systems, and can be generalised for a signal/wave $U(r,t)$:
$$
 \begin{equation} 
 U(r,t)=\mathrm{Re} \{U(r)e^{j\omega t}\}
 \end{equation} 
$$
Where $U(r)$ gives the amplitude and phase of the signal/wave at a given location $r$.

# 2)
(1a) is Gauss's law. Gives that the divergence of an electric field is the same as the total charge density divided by the permitivity of vacuum.

(1b) is that there is no isloated magnetic charge, meaning there isn't a single source point like with electric charges. Gives that the divergence of an magnetic field is always 0.

(1c) is Faraday's law. Gives that the curl of electric field is always equal to the negative derivative with respect to time $t$ of the magnetic field.

(1d) is Ampere's circuital law. Gives that the curl of magnetic field is equal to the sum of the current charge density multiplied by the vaccum permeability, and the derivative with respect to time $t$ of the electric field, divided by the speed of light squared. $\epsilon_{0}\mu_{0}=\frac{1}{c^2}$

(2a) is all the same, just written over to the electric field displacement $D$ using $D=\epsilon E$ and have it now be for the volume density of free charegs, usually written $\rho_{f}$. 

(2b) nothing changed.

(2c) same here.

(2d) Now we have swapped $B$ for the auxiliary magnetic field $H$, again the electric displacement field and $J$ is the density of free currents. 

All the equations are usefull when trying to figure out how an E-field or H-field reacts and induces eachother when meeting different materials.


# 3)
## a)
A plane wave is a wave that only propagates in a straight line where the phase/amplitude is constant across a perpendicular plane to the straight line. An example is $E = a_{x}E_{x}$ that propagates in the +z direction.

Transverse electromagnetic waves (TEM) are plane waves propagating in an arbitrary direction $a_{n}$ that has both $E \perp H$ and that both are normal to $a_{n}$. 

## b)
The wave $f(t,z)=A\cos(kz-\omega t)$ would travel in positive z-direction, while with $+\omega t$ would go in negative z-direction.
![[task_3_rotated.png]]
Code for plots:

```python
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
ax2.set_yticks(tick_positions)
ax2.set_yticklabels(tick_labels)

fig.legend()
plt.show()


``` 


## c)
$$
 \begin{equation} 
 \nabla \cdot E = 0, \ \ \ \nabla \cdot B = 0, \ \ \ \nabla \times E = -\frac{\partial B}{\partial t}, \ \ \ \nabla \times B = \frac{1}{c^2} \frac{\partial E}{\partial t} 
 \end{equation} 
$$
## d)
$$
 \begin{equation} 
 \nabla \times ( \nabla \times E) = \nabla (\nabla \cdot E) - \Delta E = -\Delta E 
 \end{equation}  = \nabla \times \left( -\frac{\partial B}{\partial t}  \right)
$$
$$
 \begin{equation} 
 \frac{\partial }{\partial t}(\nabla \times B) = \nabla \times \frac{\partial B}{\partial t}=  -(-\Delta E) = \frac{\partial}{\partial t}\left( \frac{1}{c²} \frac{\partial E}{\partial t}\right) = \frac{1}{c^2}\frac{\partial^2E}{\partial t ^2}
 \end{equation} 
$$
$$
 \begin{equation} 
 \implies \Delta E -\frac{1}{c^2}\ddot{E} = 0 
 \end{equation} 
$$
Can do the same for B or H, by doing it the other way round and.

## e)
Helmholtz equation:
$$
 \begin{equation} 
 \Delta E + k^2E=0 
 \end{equation} 
$$
Seperating E-field into its components:
$$
 \begin{equation} 
 E= \hat{a}_{x}E_{x}+ \hat{a}_{y}E_{y} + \hat{a}_{z}E_{z}
 \end{equation} 
$$
If we have only a $E_{x}$ component in a plane wave normal on z-direction:
$$
 \begin{equation} 
 \implies \frac{\partial^2}{\partial z^2} E_{x}+k_{0}^2E_{x} = 0
 \end{equation} 
$$
Which is solved by
$$
 \begin{equation} 
 E_{x}(z)=E_{0}^{+} e^{-jk_{0}z}+E_{0}^- e^{jk_{0}z} 
 \end{equation} 
$$

## f)
We would then multiply the solution with $e^{j\omega t}$ and take the real part of it:
$$
 \begin{equation} 
  E(z,t)=\mathrm{Re}\{E_{0}^+e^{-jkz}e^{jwt}\} = \mathrm{Re}\{E_{0}^+e^{-j(wt-kz)}\}=E_{0}^+\cos(wt-kz)
 \end{equation} 
$$
Its a cosine! Amplitude is given by its boundary conditions.

# 4)
## a)
The loss angle
$$
 \begin{equation} 
 \tan \delta = \frac{\sigma}{\omega \epsilon}
 \end{equation} 
$$
Gives the ratio between the conductive current and permative current in a dielectric, making it so that for values $\sigma \gg \omega \epsilon$ it will be a good conductor (bad dielectric) and for $\omega \epsilon\gg \sigma$ it will be a bad conductor (good dielectric).

## b)
Movement of electrons or currents is the main factor contibuting to thermal loss in metals. For higher frequencies the "skin effect" does come into play, but the main thing is that all metals will have a resistance $(\Omega)$ and thus by having current run through it, some of the power will go to thermal loss.

## c)
Using:
$$
 \begin{equation} 
  E_{x}=\mathrm{Re}\{E_{0}e^{-\alpha z}e^{-j\beta z}\}=E_{0}e^{-\alpha z}\cos(\beta z)
 \end{equation} 
$$
![[taks_4.png]]

Code:

```python
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
``` 

