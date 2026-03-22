#### **Primer ejemplo**
Determine para qué valores de $p$ la siguiente integral es convergente:
$$ \int_1^\infty \frac{1}{x^p} dx. $$
**Solución**. Consideremos primero $p=1:$
$$
\int_{1}^{\infty} \frac{1}{x} dx = \lim_{t\to\infty} \int_{1}^{t} \frac{1}{x} dx
$$
$$
= \lim_{t\to\infty} \left[ \ln |x| \right]_{1}^{t}
$$
$$
= \lim_{t\to\infty} (\ln t - \ln 1)
$$
$$
= \lim_{t\to\infty} \ln t = \infty,
$$
por lo tanto, la integral diverge si $p=1$.
Supongamos $p \neq 1$, entonces
$$ \int_{1}^{\infty} \frac{1}{x^p} dx = \lim_{t \to \infty} \int_{1}^{t} \frac{1}{x^p} dx $$
$$ = \lim_{t \to \infty} \left| \frac{x^{-p+1}}{-p+1} \right|_{1}^{t} $$
$$ = \lim_{t \to \infty} \frac{1}{1-p} \left( \frac{1}{t^{p-1}} - 1 \right). $$
Si $p > 1$, entonces $p-1 > 0$ y así $\lim_{t \to \infty} \frac{1}{t^{p-1}} = 0$, por lo tanto,
$$ \int_{1}^{\infty} \frac{1}{x^p} dx = \frac{1}{p-1} \quad \text{si} \quad p > 1. $$
Si $p < 1$, entonces $p-1 < 0$ y así $\lim_{t \to \infty} \frac{1}{t^{p-1}} = \lim_{t \to \infty} t^{1-p} = \infty$, en consecuencia la integral diverge.
****
Entonces, hemos obtenido:
$$
\int_{1}^{\infty} \frac{1}{x^{p}} dx \text{ es convergente si } p > 1 \text{ y divergente si } p \leq 1.
$$
****
#### **Segundo ejemplo**
Determine para qué valores positivos de $p$ la siguiente integral es convergente
$$ \int_{0}^{1} \frac{1}{x^p} $$
Solución. En el Ejemplo 8.3 vimos que si $p=1$ la integral es divergente, así que supongamos $p > 0$ y $p \neq 1$. Entonces
$$ \int_0^1 \frac{1}{x^p} dx = \lim_{t \to 0^+} \int_t^1 \frac{1}{x^p} dx $$
$$ = \lim_{t \to 0^+} \left| \frac{x^{-p+1}}{-p+1} \right|_t^1 $$
$$ = \lim_{t \to 0^+} \frac{1}{1-p} \left( 1 - \frac{1}{t^{p-1}} \right) $$
Si $p > 1$, entonces $p-1 > 0$ y así $\lim_{t \to 0^+} \frac{1}{t^{p-1}} = \infty$, en consecuencia la integral diverge.
Si $0 < p < 1$, entonces $p-1 < 0$ y así $\lim_{t \to 0^+} \frac{1}{t^{p-1}} = 0$, por lo tanto
$$ \int_0^1 \frac{1}{x^p} dx = \frac{1}{1-p} \quad \text{si } 0 < p < 1. $$
Resumiendo, hemos obtenido:
$$ \int_0^1 \frac{1}{x^p} dx \text{ es convergente si } 0 < p < 1 \text{ y divergente si } p \geq 1. $$
