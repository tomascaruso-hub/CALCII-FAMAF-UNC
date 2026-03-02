**Demostración**: Para cada ($x \neq a$), podemos aplicar el criterio del cociente para series numéricas a la serie ($I = \sum_{n=0}^{\infty} \underbrace{c_n(x-a)^n}_{a_n}$). Tenemos que
$$\lim_{n \to \infty} \frac{|a_{n+1}|}{|a_n|} = \lim_{n \to \infty} \left| \frac{c_{n+1}(x-a)^{n+1}}{c_n(x-a)^n} \right| = \lim_{n \to \infty} \frac{|c_{n+1}|}{|c_n|} |x-a| = L|x-a|.$$
(1) Supongamos ($0 < L < \infty$).
Luego, por el Crit. cociente para series numéricas si
$$\begin{cases} L|x-a| < 1 \implies I \text{ conv. abs.} \\ L|x-a| > 1 \implies I \text{ diverge} \end{cases}$$
O sea si ($|x-a| < \frac{1}{L} \implies I \text{ conv. abs}$)
si ($|x-a| > \frac{1}{L} \implies I \text{ diverge}$)
($\therefore R = \frac{1}{L}$).

(2) Si ($L=0$), entonces ($L|x-a| < 1 \quad \forall x \in \mathbb{R}$) y ($\therefore R = \infty$).
(3) Si ($L=\infty$), entonces ($L|x-a| = \infty \quad \forall x \neq a$) y ($\therefore R = 0$).
