##### **Ejemplo.** Encuentre $\frac{d}{dx} \int_1^{x^4} \sec t \, dt.$
El problema es calcular la derivada con respecto a $x$ de la integral definida.
Vemos que el límite inferior es constante, mientras que el superior es $x^4$ que depende de $x$. 
Si el límite superior fuera simplemente $x$, por el [[2. Teorema Fundamental del Cálculo]] directo, la derivada sería $\sec x$. Como en realidad es $x^4$, usamos la regla de la cadena, y definimos $u=x^4$. Entonces, reescribimos
$$\frac{d}{dx} \int_1^{x^4} \sec t \, dt = \frac{d}{du} \int_1^{u} \sec t \, dt \cdot \frac{du}{dx}$$Donde se trata $\int_1^{u} \sec t \, dt$ como una función de $u$ y se multiplica por la derivada de $u$ (el argumento de la función) respecto a $x$, como indica la regla de la cadena: $[g(u(x))]'= g'(u) \cdot u'(x)$.
Luego,$$= \sec u \cdot \frac{du}{dx}$$ (por **TFC1**) $$= \sec(x^4) \cdot 4x^3$$

