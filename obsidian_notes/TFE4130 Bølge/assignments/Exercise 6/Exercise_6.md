# Problem 1)
In order to remove the unwanted reflections, you would want to match the impedances of the transmission line and the load. There are multiple ways you can do this depending on the load and the transmission line. F.ex if you can change the impedance of the load by terminating it with the same impedance as the line using a T-connector (See image) and a terminator that matches. Then your signal will remove the unwanted reflections.
![[Pasted image 20261005114512.png|300]]
If you cant change the termination of the load, F.ex if its the input of a transistor, then you will have to do some change to the line. This could be either adding a single-stub to the line or changing the length and frequency of the line and signal if the line is lossless.

# Problem 2
## a)
The incident voltage wave is described by $e^{-j\beta z}$ and reflected stress wave by $e^{j\beta z}$ because the $\pm$ indicates the direction of the wave defined for the $z$-direction. We can sum these for the total voltage and they vary along the line because of different phase. 

## b & c)
![[Pasted image 20261005155231.png|650]]

## d) 
For the rest of the problem we assume that
$$
 \begin{equation} 
 Z_{L}=0 \ \ \ \text{ at } \ \ z=0 
 \end{equation} 
$$
### i)
$$
 \begin{equation} 
 \Gamma_{0}  = \frac{-Z_{0}}{Z_{0}}=-1
 \end{equation} 
$$
$$
 \begin{equation} 
 \Gamma_{in}=\Gamma_{0}\cdot e^{-j{2}\beta l}  = -e^{2\pi / 5}
 \end{equation} 
$$
### ii)
$$
 \begin{equation} 
 Z_{in}=Z_{0} \cdot \frac{Z_{0}\tanh(j\beta l)}{Z_{0}}= Z_{0}\tanh(j\beta l)=50\tanh\left( \frac{j\pi}{5} \right) \approx j 36.33 \Omega
 \end{equation} 
$$
## e)
We have
$$
 \begin{equation} 
 V_{0}^- =\Gamma_{0} \cdot V_{0}^+ = -1 \cdot 2 = -2V \implies |V_{0}^-|=2 \ \& \ \angle \pi \ \ (180^o)
 \end{equation} 
$$

## f)
$$
 \begin{equation} 
 V_{L}(z) = V_{0} ^+ e^{-\gamma z} + V_{0}^-e^{\gamma z} \implies V_{L}(0)=2-2=0V
 \end{equation} 
$$

## g)
$$
 \begin{equation} 
 P_{in}=\frac{|V_{0}^+|^2}{2Z_{0}} = 40 \text{mW}
 \end{equation} 
$$
$$
 \begin{equation} 
 P_{ref}= |\Gamma_{0}|^2 \cdot P_{in} = 40 \text{ mW} 
 \end{equation} 
$$
## h)
$$
 \begin{equation} 
 V_{i}=\frac{Z_{in}}{Z_{g}+Z_{in}} =  \frac{j36.33}{50+j 36.33} = 0.3455 + 0.4755j
 \end{equation} 
$$
$$
 \begin{equation} 
 I_{i}=\frac{V_{g}}{Z_{g}+Z_{in}}=\frac{1}{50+j 36.33} =0.0131 - 0.0095j
 \end{equation} 
$$
$$
 \begin{equation} 
 P_{av}=\frac{1}{2}\mathrm{Re}\left\{  V_{i}I_{i}^*  \right\} \approx 0 
 \end{equation} 
$$
Or
$$
 \begin{equation} 
 P_{av} = P_{in}- P_{ref} = 40-40 = 0 
 \end{equation} 
$$

# Problem 3)
## a)
Since the second transmission is perfectly matched the load, the impedance looking into B-B is exactly the characteristic impedance $Z_{L_{eff}}=300\Omega$.

And since
$$
 \begin{equation} 
 f=500 MHz \implies \lambda = \frac{c}{f}= 0.6 \implies L_{0} = 5\lambda
 \end{equation} 
$$
the length of the transmission line is a multiple of $\lambda / 2$, the impedance will repeat 10 times and be matched with the load again looking into it at A-A, so we get:
$$
 \begin{equation} 
 Z_{in} = Z_{L_{eff}} = 300 \Omega
 \end{equation} 
$$

## b)
$$
 \begin{equation} 
 L_{0} = 5.25\cdot \lambda 
 \end{equation} 
$$
This makes it so that we get the impedance repeated 10 times and then a quarterwave-transformation of the line. We then get that 
$$
 \begin{equation} 
 Z_{in}=\frac{Z_{0}^2}{Z_{L_{eff}}}  = \frac{600^2}{300} = 1200 \Omega
 \end{equation} 
$$
