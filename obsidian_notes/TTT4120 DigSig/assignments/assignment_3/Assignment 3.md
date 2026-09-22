# Problem 1)
## a)
Assuming the voltages $x(t)$ and $y(t)$:
For RC:
$$
 \begin{equation} 
 i(t)=C\cdot \frac{\partial y(t)}{dt}
 \end{equation} 
$$
$$
 \begin{equation} 
 x(t)=R\cdot i(t) + y(t)=RC \dot{y}(t) + y(t) 
 \end{equation} 
$$
For RL:

$$
 \begin{equation} 
  y(t)=L \cdot \frac{\partial i(t)}{dt}
 \end{equation} 
$$
$$
 \begin{equation} 
 x(t)=Ri(t) + L\dot{i}(t) 
 \end{equation} 
$$ 
$$
 \begin{equation} 
 H_{RC}(s)=\frac{Y(s)}{X(s)} =\frac{\frac{1}{Cs}}{R+\frac{1}{Cs}}=\frac{1}{1+RCs}
 \end{equation} 
$$
$$
 \begin{equation} 
 H_{RL}(s)=\frac{Y(s)}{X(s)} = \frac{Ls}{R+Ls}=\frac{s}{\frac{R}{L}+s} =\frac{1}{1+\frac{R}{Ls}}
 \end{equation} 
$$
## b)
$$
 \begin{equation} 
 H_{RC}(j\omega) = \frac{1}{1+j\omega RC} 
 \end{equation} 
$$
$$
 \begin{equation} 
 H_{RL}(j\omega)=\frac{j\omega}{\frac{R}{L}+j\omega}=\frac{1}{1+ \frac{R}{j\omega L}} 
 \end{equation} 
$$
RC is a lowpass, while RL is a highpass.

## c)
For RC $\tau=RC$ and for RL $\tau=\frac{L}{R}$
Unit pulse response is the given as:
$$
 \begin{equation} 
 h(t)=\frac{1}{\tau} e^{-t/\tau}u(t)
 \end{equation} 
$$

# Problem 2)
## a)
$$
 \begin{equation} 
 H(z)=\frac{1}{1-\frac{2}{3}z^{-1}} 
 \end{equation} 
$$
$$
 \begin{equation} 
 \implies h[n]=\left( \frac{2}{3} \right)^n u[n] \ \ \& \ \ \text{ ROC: }|z|> \frac{2}{3} 
 \end{equation} 
$$
## b)
$$
 \begin{equation} 
 H(z)=\frac{1}{\left( 1+\frac{1}{2}z^{-1} \right)(1-z^{-1})} = \frac{A}{\left( 1+\frac{1}{2}z^{-1} \right)} + \frac{B}{(1-z^{-1})}\implies \frac{\frac{1}{3}}{1+\frac{1}{2}z^{-1}}+\frac{\frac{2}{3}}{1-z^-1}
 \end{equation} 
$$
$$
 \begin{equation} 
 \implies h[n]=\left( \frac{1}{3} \left( -\frac{1}{2} \right)^n+\frac{2}{3} \right) u[n] \ \ \ \& \ \ \text{ROC: |z|> 1} 
 \end{equation} 
$$
## c)
$$
 \begin{equation} 
 H(z)=\frac{z^{-1}}{\left( 1-\frac{3}{2}z^{-1} \right)(1-3z^{-1})} =\frac{A}{\left( 1-\frac{3}{2}z^{-1} \right)} + \frac{B}{(1-3z^{-1})} \implies-\frac{2}{3}\left(  \frac{1}{1-\frac{3}{2}z^{-1}} + \frac{1}{(1-3z^{-1})} \right)
 \end{equation} 
$$
$$
 \begin{equation} 
 \implies h[n]=-\frac{2}{3} \left[ -\left( \frac{3}{2} \right)^n-3^n \right] u[-n-1]
 \end{equation}  \ \ \& \ \ \ \text{ROC: } |z|< \frac{3}{2}
$$
## d)
For the system to be BIBO stable, the unit circle has to be within ROC, which goes for a) and c) as they are both true for $|z|=1$.


# Problem 3)
## a)
![[Pasted image 20260914145319.png|650]]
## b & c)
![[Pasted image 20260914153917.png|650]]

# Problem 4)
![[Pasted image 20260914162629.png|650]]