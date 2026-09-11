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

## b)
$$
 \begin{equation} 
 H(z)=\frac{1}{\left( 1+\frac{1}{2}z^{-1} \right)(1-z^{-1})}= \frac{1}{\left( 1-\frac{1}{2}z^{-1}-\frac{1}{2}z^{-2} \right)}=\frac{-2}{(2z^{-1})}
 \end{equation} 
$$

## c)
$$
 \begin{equation} 
 H(z)=\frac{z^{-1}}{\left( 1-\frac{3}{2}z^{-1} \right)(1-3z^{-1})} 
 \end{equation} 
$$



# Problem 3)
## a)






# Problem 4)
