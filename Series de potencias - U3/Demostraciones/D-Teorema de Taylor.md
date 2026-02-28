Del ejemplo 1 de **[[E-Serie de Taylor y Maclaurin]]**, se concluye que $e^x$ tiene un desarrollo en serie de potencias en $0$, entonces 
$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$$
Así que, **¿cómo podemos determinar si ($e^x$) tiene una representación como serie de potencias?**
Investiguemos la cuestión más general: **¿en qué circunstancias una función es igual a la suma de su serie de Taylor?** En otras palabras, si ($f$) tiene derivadas de todos los órdenes, cuándo es cierto que
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n$$
Como sucede con cualquier serie convergente (de lo contrario no estarían definidas las derivadas $f^{(n)}$), esto quiere decir que ($f(x)$) es el límite de la sucesión de sumas parciales. En el caso de la serie de Taylor, las sumas parciales son
$$T_n(x) = \sum_{i=0}^{n} \frac{f^{(i)}(a)}{i!} (x - a)^i$$
$$= f(a) + \frac{f'(a)}{1!} (x - a) + \frac{f''(a)}{2!} (x - a)^2 + \cdots + \frac{f^{(n)}(a)}{n!} (x - a)^n$$
Observe que ($T_n$) es una polinomial de grado ($n$) llamado [[Polinomio de Taylor]]. Del ejemplo 1 de **[[E-Serie de Taylor y Maclaurin]]**, se concluye que $e^x$ tiene un desarrollo en serie de potencias en $0$. 
En general, ($f(x)$) es la suma de su serie de Taylor si$$f(x) = \lim_{n \to \infty} T_n(x)$$Si hacemos
$$R_n(x) = f(x) - T_n(x) \quad \text{de manera que} \quad f(x) = T_n(x) + R_n(x)$$
entonces ($R_n(x)$) se llama residuo de la serie de Taylor. Si podemos de alguna manera demostrar que ($\lim_{n \to \infty} R_n(x) = 0$), entonces se sigue que
$$\lim_{n \to \infty} T_n(x) = \lim_{n \to \infty} [f(x) - R_n(x)] = f(x) - \lim_{n \to \infty} R_n(x) = f(x)$$
