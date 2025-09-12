Si $f$ es continua sobre $[a,b],$ entonces la función $g$ definida por
$$g(x) = \int_a^x f(t) \, dt \quad a \leq x \leq b$$
es continua sobre $[a, b]$ y **derivable** sobre $(a, b)$, y $g'(x) = f(x)$.
****
**Demostración.** Si $x, y, x + h$ están en $(a, b)$, entonces
$$g(x + h) - g(x) = \int_x^{x+h} f(t) , dt - \int_a^x f(t) , dt$$
$$= \left( \int_a^{x+h} f(t) , dt + \int_x^{x+h} f(t) , dt \right) - \int_a^x f(t) , dt \quad (\text{por la propiedad de aditivdad})$$$$ = \int_x^{x+h} f(t) , dt$$y de este modo, para $h \neq 0$, podemos dividir a ambos lados$$\frac{g(x + h) - g(x)}{h} = \frac{1}{h} \int_x^{x+h} f(t) , dt$$Por ahora supongamos que $h > 0$. Puesto que $f$ es continua sobre $[x, x + h]$, el teorema del valor extremo establece que hay números $u$ y $v$ en $[x, x + h]$ tales que $f(u) = m$ y $f(v) = M$, donde $m$ y $M$ son los valores mínimo y máximo absolutos de $f$ sobre $[x, x + h]$
![[Pasted image 20250829100856.png]]
De acuerdo con una de las propiedades de comparación de las integrales, tenemos $$m h \leq \int_x^{x+h} f(t) \, dt \leq M h$$es decir,
$$f(u) h \leq \int_x^{x+h} f(t) \, dt \leq f(v) h$$
Dado que $h > 0$, podemos dividir esta desigualdad entre $h$:
$$f(u) \leq \frac{1}{h} \int_x^{x+h} f(t) \, dt \leq f(v)$$
Ahora, utilizamos la ecuación anterior para reemplazar la parte de en medio de esta desigualdad:$$f(u) \leq \frac{g(x + h) - g(x)}{h} \leq f(v)$$Ahora sea $h \to 0$. Entonces $u \to x$ y $v \to x$, ya que $u$ y $v$ quedan entre $x$ y $x + h$. Por tanto,
$\lim_{h \to 0} f(u) = \lim_{u \to x} f(u) = f(x) \quad$ y $\quad \lim_{h \to 0} f(v) = \lim_{v \to x} f(v) = f(x)$
porque $f$ es continua en $x$. De acuerdo con el teorema del **sandwich** concluimos que
$$g'(x) = \lim_{h \to 0} \frac{g(x + h) - g(x)}{h} = f(x)$$De acuerdo con la notación de Leibniz para derivadas, podemos expresar al **TFC1** como
$$\frac{d}{dx} \int_a^x f(t) \, dt = f(x)$$
cuando $f$ es continua. En términos generales, la expresión establece que si primero integramos $f$ y luego derivamos el resultado, regresamos a la función original $f$.