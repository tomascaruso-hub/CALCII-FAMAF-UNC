**EJEMPLO 1**. Exprese ($1/(1 + x^2)$) como la suma de una serie de potencias y determine el intervalo de convergencia.

**SOLUCIÓN**. Al reemplazar ($x$) por ($-x^2$) en la ecuación 1, tenemos
$$\frac{1}{1 + x^2} = \frac{1}{1 - (-x^2)} = \sum_{n=0}^{\infty} (-x^2)^n$$
$$= \sum_{n=0}^{\infty} (-1)^n x^{2n} = 1 - x^2 + x^4 - x^6 + x^8 - \cdots$$
Como ésta es una serie geométrica, es convergente cuando ($|-x^2| < 1$), es decir, ($x^2 < 1$), o bien, ($|x| < 1$). Por tanto, el intervalo de convergencia es $(-1, 1)$. Naturalmente, podría haber determinado el radio de convergencia aplicando la prueba de la razón, pero esa cantidad de trabajo es innecesaria en este caso.
****
**EJEMPLO 2** Determine una representación en serie de potencias para ($1/(x + 2)$).

**SOLUCIÓN** Con objeto de poner esta función en la forma del lado izquierdo de la ecuación 1, primero se factoriza un 2 del denominador:
$$\frac{1}{2 + x} = \frac{1}{2(1 + \frac{x}{2})} = \frac{1}{2[1 - (-\frac{x}{2})]}$$
$$= \frac{1}{2} \sum_{n=0}^{\infty} \left(-\frac{x}{2}\right)^n = \sum_{n=0}^{\infty} \frac{(-1)^n}{2^{n+1}} x^n$$
Esta serie converge cuando ($|-x/2| < 1$), es decir, ($|x| < 2$). De modo que el intervalo de convergencia es ($(-2, 2)$).
****
**EJEMPLO NOTAS 1.** Expresar la función ($ln(1-x)$) como una serie de potencias.
Observemos que $$-ln(1-x) = \int f(x) dx$$con $f(x) = \frac{1}{1-x}$.
Además, $$f(x) = \sum_{n=0}^{\infty} x^n$$si $|x|<1$.
Luego $$-ln(1-x) = \int f(x) dx = \int \sum_{n=0}^{\infty} x^n dx = \sum_{n=0}^{\infty} \int x^n dx = C + \sum_{n=1}^{\infty} \frac{x^n}{n}$$si $|x|<1$.
Para determinar ($C$), evaluamos en ($x=0$) obteniendo
$$-ln(1) = C \implies C = 0.$$
Por lo tanto ($ln(1-x) = - \sum_{n=1}^{\infty} \frac{x^n}{n}$), si ($|x|<1$) (o sea ($R=1$)).
****
**EJEMPLO NOTAS 2.** 
Expresar la función $$g(x) = \frac{1}{(1-x)^2}$$como una serie de potencias.
Notemos que $g(x) = f'(x)$ con $$f(x) = \frac{1}{1-x}$$Además sabemos que $$f(x) = \sum_{n=0}^{\infty} x^n$$ si ($|x| < 1$), o sea su radio de convergencia. es 1.
Luego, $$\frac{1}{(1-x)^2} = g(x) = f'(x) = \left[ \sum_{n=0}^{\infty} x^n \right]' = \sum_{n=0}^{\infty} n x^{n-1} = \sum_{n=0}^{\infty} (n+1) x^n$$ y el radio de convergencia es ($R=1$)
La última igualdad $\sum_{n=0}^{\infty} n x^{n-1} = \sum_{n=0}^{\infty} (n+1) x^n$ simplemente reescribe la expresión ya que el primer término de la sumatoria es $0$ y por lo tanto, no aporta nada a la suma de la serie.
****
https://gemini.google.com/app/1f9df2dd12a44598?hl=es
ejemplo explicado paso a paso