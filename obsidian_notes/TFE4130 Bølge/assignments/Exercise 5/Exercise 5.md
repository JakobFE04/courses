# 1)
## a)
Total reflection is when a wave in a given medium collides with another medium at such an angle that no wave starts to propagate in the second medium. This can be used in a waveguide by making it out of a material that has a larger dielectric constant then the minimum for the waveguide to achieve total internal reflection. Then the wave/signal will have no loss propagating through the waveguide, which can be achieved for quartz or glass as an example.

## b)
$$
 \begin{equation} 
 \theta_{c}=\sin^{-1} \left(  \frac{n_{2}}{n_{1}} \right) =\sin^{-1}\left(  \frac{1}{1.44} \right) = 0.77 \approx 44.12^o
 \end{equation} 
$$
## c)
The Brewsters angle is the angle when a perpundicular polarized wave hits a medium and there is no reflection. Meaning all the wave propagates through to the other medium.

# 2)
## a)
$$
 \begin{equation} 
 Q_{in} = \frac{I}{\pi a^2}= \int_{S}^{} \mathbf{D}\cdot dS = \int_{0}^{l}\int_{0}^{2\pi} D(r) \ r d\theta d L = 2\pi rl D(r)
 \end{equation} 
$$
$$
 \begin{equation} 
 \implies D(r)=\frac{I}{2\pi^2a^2rl} 
 \end{equation} 
$$
$$
 \begin{equation} 
 E(r)=\frac{I}{2\pi^2 a^2rl\epsilon} 
 \end{equation} 
$$

## b)
The E-field is zero for $r<a$ and $r>b$ because the internally induced electric field in the metal conductor cancels out the external E-field. 

## c)
For $r<a$:
$$
 \begin{equation} 
  I_{f_{enc}} = \frac{I}{\pi r^2} \implies \oint_{}^{} \mathbf{H} \cdot dl = I_{f_{enc}} \implies 2\pi rH(r)=I_{f_{enc}} \implies H(r)=\frac{I}{2\pi^2r^3}
 \end{equation} 
$$
For $a<r<b$: 
$$
 \begin{equation} 
  I_{f_{enc}}=I \frac{r^2}{a^2} \implies H(r) = \frac{Ir}{2\pi a^2}
 \end{equation} 
$$
For $b<r$:
$$
 \begin{equation} 
 I_{fenc} = \frac{I}{\pi a^2} \implies H(r)=\frac{I}{2\pi^2a^2r} 
 \end{equation} 
$$

## d)
For $a<r<b$:
$$
 \begin{equation} 
 P=EH = \frac{I^2}{4\pi^4a^4l\epsilon } 
 \end{equation} 
$$
And 0 for the other cases since E=0.

## e)
![[Pasted image 20260927152532.png]]
The E-field is radially outward from the core, while H is perpendicular to E in the plane around the cross-section of the cable ($\hat{\theta}$), and P is flowing along the current in z-direction (Given that the magnetization of the cable makes the H-field flow with the right-hand rule).

# 3)
## a)
$$
 \begin{equation} 
 Z_{0} = \sqrt{ \frac{L}{C} } = \sqrt{ \frac{0.18\mu}{50p} } = 60 \Omega
 \end{equation} 
$$
The characteristic impedance is the transmission line's "signature" which shows the traits of the line that the load will experience. It does not depend on the length of the line as both L and C depends on the length, but this gets crossed out when calculating $Z_{0}$.

## b)
If you place z=0 at the load $Z_{L}$, you get that:
$$
 \begin{equation} 
 \Gamma = \frac{V_{0}^-}{V_{0}^+} = \frac{Z_{L}-Z_{0}}{Z_{L}+Z_{0}} = \frac{75-60}{75+60}= \frac{1}{9}\approx0.11
 \end{equation} 
$$
Which is then defined in at the load.

## c)
The standing wave ratio (SWR) is:
$$
 \begin{equation} 
 S=\frac{|V_{max}|}{|V_{min}|} = \frac{1+|\Gamma|}{1-|\Gamma|} =\frac{1 + \frac{1}{9}}{1-\frac{1}{9}} = \frac{5}{4}=1.25
 \end{equation} 
$$
## d)
$$
 \begin{equation} 
 \Gamma_{Z_{L}\to0} = -\frac{Z_{0}}{Z_{0}} = -1 
 \end{equation} 
$$
## e)
$$
 \begin{equation} 
 \Gamma_{Z_{L}\to\infty}  = \frac{\infty-Z_{0}}{\infty+Z_{0}} = 1
 \end{equation} 
$$
## f)
$$
 \begin{equation} 
 \Gamma_{Z_{L}=Z_{0}} = \frac{Z_{0}-Z_{0}}{Z_{0}+Z_{0}}=0
 \end{equation} 
$$
No reflection! This is what we want and why we often terminate input to match the impedance of the transmission line!

