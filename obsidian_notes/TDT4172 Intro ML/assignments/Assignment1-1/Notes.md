Vi vil ha en ny transformasjon slik at: 
$$
 \begin{equation} 
 \{x_{1},x_{2},x_{3}\} = \{x_{0},x_{1},x_{0}\cdot x_{1}\}
 \end{equation} 
$$
$$
 \begin{equation} 
 y_{pred} = \sigma(\beta_{0}+\mathbf{\beta_{1}x_{1} + \beta_{2}x_{2}+\beta_{3}x_{3}}) 
 \end{equation} 
$$


$$
 \begin{equation} 
 gradient_{j} = (y_{pred}-y)x_{j} 
 \end{equation} 
$$
$$
 \begin{equation} 
 gradient_{\beta_{0}} = (y_{pred}-y) 
 \end{equation} 
$$


NB! Lage ROC graf ved å regne de ut som funksjon av klassifiseringsterskelen