Se verá una técnica que nos permite calcular integrales de la forma 
$$
\int \sqrt{a^2 - x^2} dx, \quad \text{con } a > 0.
$$
Consideremos la sustitución $\theta = \text{arcsen} \left(\frac{x}{a}\right)$ o equivalentemente
$$
x = a \text{ sen } \theta, \qquad -\pi/2 < \theta < \pi/2
$$
y$$
dx = a \cos \theta d\theta.
$$Así,$$
\begin{aligned}
\sqrt{a^2 - x^2} &= \sqrt{a^2 - (a \text{ sen } \theta)^2} \\
&= \sqrt{a^2 (1 - \text{sen}^2 \theta)} \\
&= a \cos \theta.
\end{aligned}
$$Usando esto para hacer la sustitución en la primera expresión tenemos que$$
\begin{aligned}
\int \sqrt{a^2 - x^2} dx &= \int (a \cos \theta) a \cos \theta d\theta \\
&= a^2 \int \cos^2 \theta d\theta.
\end{aligned}
$$Por lo tanto nos basta con poder calcular $\int \cos^2 \theta d\theta$. Para eso, recordemos que$$
\cos^2 \theta + \text{sen}^2 \theta = 1,
$$y$$
\cos^2 \theta - \text{sen}^2 \theta = \cos(2\theta).
$$Luego, sabiendo que ambas expresiones son ciertas, podemos sumar miembro a miembro y obtenemos$$
\qquad \cos^2 \theta = \frac{1 + \cos(2\theta)}{2}.
$$Análogamente, restando miembro a miembro,$$
\qquad \text{sen}^2 \theta = \frac{1 - \cos(2\theta)}{2}.
$$Luego tenemos que
$$
\int \cos^2 \theta d\theta = \int \frac{1 + \cos(2\theta)}{2} d\theta = \frac{1}{2} \left( \theta + \frac{\text{sen}(2\theta)}{2} \right) + c.
$$Finalmente,$$
\begin{aligned}
\int \sqrt{a^2 - x^2} dx &= a^2 \int \cos^2 \theta d\theta \\
&= \frac{a^2}{2} \left( \theta + \frac{\text{sen}(2\theta)}{2} \right) + c \\
&= \frac{a^2}{2} \left[ \text{arcsen} \left( \frac{x}{a} \right) + \frac{1}{2} \text{sen} \left( 2 \text{arcsen} \left( \frac{x}{a} \right) \right) \right] + c.
\end{aligned}
$$
[[E-Sustitución Trigonométrica]]
****
**Observación**.
Para calcular integrales de la forma $\int \sqrt{a^2 + x^2} dx$, con $a > 0$, se puede usar la sustitución $x = a \tan \theta$, $-\pi/2 < \theta < \pi/2$. Así,$$
\sqrt{a^2 + x^2} = \sqrt{a^2 (1 + \tan^2 \theta)} = a \sec \theta.
$$reduciendo el cálculo de esta integral a la integral de la función $\sec^3 \theta$.

Similarmente para calcular $\int \sqrt{x^2 - a^2} dx$ se puede usar la sustitución $x = a \sec \theta$, $0 < \theta < \pi/2$

