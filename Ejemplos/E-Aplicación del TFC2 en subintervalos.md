**Observación.** Si $f$ es acotada y con un único número de discontinuidades en $[a,b]$, también podemos aplicar la segunda parte del **TFC** en cada subintervalo donde $f$ es continua. 
****
Supongamos que $f(x) = \begin{cases} 1 & \text{si } a \leq x < c, \\ 2 & \text{si } c \leq x \leq b, \end{cases}$ con una discontinuidad en $x = c$.
• Dividimos $[a, b]$ en $[a, c]$ y $[c, b]$.
• En $[a, c]$, $f(x) = 1$, que es continua. Una antiderivada es $F_1(x) = x$. Entonces:
$$\int_a^c f(x) \, dx = \int_a^c 1 \, dx = F_1(c) - F_1(a) = c - a$$
• En $[c, b]$, $f(x) = 2$, que es continua. Una antiderivada es $F_2(x) = 2x$. Entonces:
$$\int_c^b f(x) \, dx = \int_c^b 2 \, dx = F_2(b) - F_2(c) = 2b - 2c$$
• La integral total es:
$$\int_a^b f(x) \, dx = (c - a) + (2b - 2c) = 2b - c - a$$
Aunque las antiderivadas $F_1$ y $F_2$ son diferentes en cada subintervalo, la integral total se calcula correctamente sumando las contribuciones de cada subintervalo.