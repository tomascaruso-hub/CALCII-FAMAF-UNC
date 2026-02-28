**EJEMPLO 1.** Determine la serie de Maclaurin de la función ($f(x) = e^x$) y su radio de convergencia.
**SOLUCIÓN.** Si ($f(x) = e^x$), entonces ($f^{(n)}(x) = e^x$), por lo que ($f^{(n)}(0) = e^0 = 1$) para toda ($n$). Por tanto, la serie de Taylor para ($f$) en 0 (es decir, la serie de Maclaurin) es
$$\sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$
Para determinar el radio de convergencia hacemos ($a_n = x^n/n!$). Entonces
$$\left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{x^{n+1}}{(n+1)!} \cdot \frac{n!}{x^n} \right| = \frac{|x|}{n+1} \to 0 < 1$$
así que, según la prueba de la razón, la serie converge para toda ($x$) y el radio de convergencia es ($R = \infty$).
Conclusión: $$\sum_{n=0}^{\infty} \frac{x^n}{n!}$$ converge ($\forall x \in \mathbb{R}$). Esto nos dice que $$\lim_{n \to \infty} \frac{x^n}{n!} = 0$$para cualquier ($x \in \mathbb{R}$), recordando **criterio de la divergencia** (notas físicas).
