Recomendable leer [[D-Teorema de Taylor]] antes de seguir con este apartado.
****
El objetivo del Polinomio de Taylor de orden ($n$), ($T_n(x)$), es ser la **mejor aproximación polinómica de grado ($n$)** a la función ($f(x)$) cerca del punto ($a$).

¿Cómo logramos la "mejor aproximación"? Forzamos al polinomio ($T_n(x)$) a que, en ese punto exacto ($a$), tenga:
1. El mismo valor que la función.
2. La misma primera derivada que la función.
3. La misma segunda derivada que la función.
4. ...y así sucesivamente, hasta la ($n$)-ésima derivada.
****
#### **Observación 1.  $f^{(j)}(a) = T^{(j)}(a) \quad \forall 0 \le j \le n.$**
Tomemos la fórmula general del Polinomio de Taylor de orden ($n$) centrado en ($a$):
$$T_n(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n$$
Ahora, derivemos este polinomio ($T_n(x)$) varias veces y evaluemos el resultado en ($x = a$).
**1. Valor de la función (Derivada 0):**
Si evaluamos ($T_n(x)$) en ($x = a$):$$T_n(a) = f(a) + f'(a)(a-a) + \frac{f''(a)}{2!}(a-a)^2 + \cdots$$Todos los términos ($(x-a)$) se vuelven cero. ($\implies T_n(a) = f(a)$) 
**2. Primera Derivada:**
Primero derivamos ($T_n(x)$), $f'(a)$ se distribuye y $a'$ es constante. $$T_n'(x) = 0 + f'(a) + \frac{f''(a)}{2!} \cdot 2(x-a) + \frac{f'''(a)}{3!} \cdot 3(x-a)^2 + \cdots$$$$T_n'(x) = f'(a) + f''(a)(x-a) + \frac{f'''(a)}{2!}(x-a)^2 + \cdots$$Ahora, evaluamos ($T_n'(x)$) en ($x = a$):$$T_n'(a) = f'(a) + f''(a)(a-a) + \frac{f'''(a)}{2!}(a-a)^2 + \cdots$$Nuevamente, todos los términos ($(x-a)$) se vuelven cero ($\implies T_n'(a) = f'(a)$)
Esto funciona así sucesivamente. Cuando calculas la ($k$)-ésima derivada ($(k \le n)$) y la evalúas en ($a$), todos los términos desaparecen, excepto el término ($k$)-ésimo, que se convierte exactamente en ($f^{(k)}(a)$).
****
#### **Observación 2.** ($T_{1,a}$) es la recta tangente al gráfico de ($f$) en el pto. $(a, f(a))$.
$$T_{1} = f(a) + f'(a)(x-a)$$Luego recordemos de cálculo diferencial cómo encontrar la ecuación de la recta tangente al gráfico de ($f(x)$) en el punto ($(a, f(a))$).
Usamos la **forma punto-pendiente** de una recta:
$$y - y_1 = m(x - x_1)$$
Para nuestro caso:
* El punto ($(x_1, y_1)$) es ($(a, f(a))$).
* La pendiente ($m$) de la tangente en ese punto es, por definición, la derivada evaluada en ($a$): ($m = f'(a)$).
Sustituimos estos valores en la fórmula:
$$y - f(a) = f'(a)(x - a)$$
Si despejamos ($y$) (que es la función de la recta tangente, llamémosla ($L(x)$)):$$L(x) = f(a) + f'(a)(x - a)=T_{1}$$Tomando como ejemplo el ejemplo 1 de [[E-Serie de Taylor y Maclaurin]]... 
![[Pasted image 20251106100832.png]]


