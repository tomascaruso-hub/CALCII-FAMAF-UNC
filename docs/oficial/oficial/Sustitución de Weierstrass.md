Esta sustitución, tal como la vista en el inciso de [[Sustitución Trigonométrica]], se basa en **usar un triángulo rectángulo y las identidades trigonométricas** para transformar una expresión compleja en una algebraica (polinomios sin raíces).

Llegaremos a los siguientes resultados desde un enfoque puramente algebraico$$
\cos(x) = \frac{1 - t^2}{1 + t^2}, \qquad \text{sen}(x) = \frac{2t}{1 + t^2} \qquad \text{y} \qquad dx = \frac{2}{1 + t^2} dt.
$$****
Definimos $a = \frac{x}{2}$ (por lo que $x = 2a$) y la sustitución es $t = \tan(a)$.

**1. Identidad fundamental y división**
Partimos de la identidad trigonométrica básica:$$
\text{sen}^2(a) + \cos^2(a) = 1
$$Dividimos cada término entre $\cos^2(a)$:$$
\frac{\text{sen}^2(a)}{\cos^2(a)} + \frac{\cos^2(a)}{\cos^2(a)} = \frac{1}{\cos^2(a)}
$$Aplicando las definiciones de tangente y secante, obtenemos:$$
\tan^2(a) + 1 = \sec^2(a)
$$**2. Despeje de $\cos^2(a)$**
Reemplazamos $t = \tan(a)$ y sabemos que $\sec^2(a) = \frac{1}{\cos^2(a)}$:
$$
t^2 + 1 = \frac{1}{\cos^2(a)}
$$Despejando el coseno al cuadrado llegamos a la pieza clave:
$$
\cos^2(a) = \frac{1}{1 + t^2}
$$
**3. Deducción de $\cos(x)$**
Como $x = 2a$, usamos la identidad del coseno del ángulo doble:
$$
\cos(x) = \cos(2a) = \cos^2(a) - \text{sen}^2(a)
$$
Sabemos por la identidad fundamental que $\text{sen}^2(a) = 1 - \cos^2(a)$. Lo sustituimos para que todo quede en términos de coseno:
$$
\cos(x) = \cos^2(a) - (1 - \cos^2(a)) = 2 \cos^2(a) - 1
$$
Reemplazamos con nuestra pieza clave del paso 2:
$$
\cos(x) = 2 \left( \frac{1}{1 + t^2} \right) - 1 = \frac{2 - (1 + t^2)}{1 + t^2} = \frac{1 - t^2}{1 + t^2}
$$**4. Deducción de $\text{sin}(x)$**
Aplicamos la identidad del seno del ángulo doble:$$
\text{sin}(x) = \text{sin}(2a) = 2 \text{sin}(a) \cos(a)
$$Aquí aplicamos un truco algebraico: multiplicamos y dividimos por $\cos(a)$ para forzar la aparición de la tangente:$$
\text{sin}(x) = 2 \left( \frac{\text{sin}(a)}{\cos(a)} \right) \cos^2(a) = 2 \tan(a) \cos^2(a)
$$Sustituimos $t = \tan(a)$ y nuestra pieza clave del paso 2:
$$
\text{sin}(x) = 2t \left( \frac{1}{1 + t^2} \right) = \frac{2t}{1 + t^2}
$$**5. Deducción de $dx$** 
Partimos de la sustitución inicial:$$
t = \tan \left( \frac{x}{2} \right)
$$Aplicamos la función inversa (arcotangente) a ambos lados para "liberar" la $x$:
$$
\text{arctan}(t) = \frac{x}{2}
$$Despejamos $x$ multiplicando por 2:$$
x = 2 \text{ arctan}(t)
$$Derivamos a ambos lados. Por regla de derivación, sabemos que la derivada de $\text{arctan}(t)$ es $\frac{1}{1+t^2}$:
$$
dx = 2 \left( \frac{1}{1 + t^2} \right) dt = \frac{2}{1 + t^2} dt
$$

