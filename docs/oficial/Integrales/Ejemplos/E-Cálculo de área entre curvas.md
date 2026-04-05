##### **Ejemplo 1**
Determine el área de la región acotada por arriba por $y = e^x$, por abajo por $y = x$ y a los lados por $x = 0$ y $x = 1$.
![[Pasted image 20250829200635.png]]
****
La región se muestra en la figura. La curva que limita la parte superior es $y = e^x$, y la curva del límite inferior es $y = x$. De este modo usamos la fórmula del área con $f(x) = e^x$, $g(x) = x$, $a = 0$ y $b = 1$.
$$A = \int_0^1 (e^x - x) \, dx = e^x - \frac{1}{2} x^2 \big|_0^1$$
$$= e - \frac{1}{2} - 1 = e - 1.5$$
En la figura, vemos se toma un rectángulo representativo de aproximación cuyo ancho es $\Delta{x}$ como recordatorio del procedimiento realizado en el apartado [[docs/oficial/Sucesiones y Series - U2/Ejemplos/1. El problema del área]].
****
##### **Ejemplo 2**. Determinando puntos de encuentro
![[Pasted image 20250829200931.png]]
Calcule el área de la región encerrada por las parábolas $y = x^2$ y $y = 2x - x^2$.
****
Primero determinamos los puntos de intersección de las parábolas resolviendo en forma simultánea sus ecuaciones. El resultado es $x^2 = 2x - x^2$, o $2x^2 - 2x = 0$. Así, $2x(x - 1) = 0$, de modo que $x = 0$ o $1$. Los puntos de intersección son $(0, 0)$ y $(1, 1)$.
Según la figura, los límites superior e inferior son
$$y_S = 2x - x^2 \quad y \quad y_I = x^2$$
El área de un rectángulo representativo es
$$(y_S - y_I) \Delta x = (2x - x^2 - x^2) \Delta x$$
por lo que la región se sitúa entre $x = 0$ y $x = 1$. De modo que el área total es
$$A = \int_0^1 (2x - 2x^2) \, dx = 2 \int_0^1 (x - x^2) \, dx$$
$$= 2 \left[ \frac{x^2}{2} - \frac{x^3}{3} \right]_0^1 = 2 \left( \frac{1}{2} - \frac{1}{3} \right) = \frac{1}{3}$$
