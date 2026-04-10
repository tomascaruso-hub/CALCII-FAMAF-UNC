---
carpeta: oficial
title: aaa
---
Empecemos por suponer que ($f$) es cualquier función que se puede hallar esa representación mediante una serie de potencias
$$1 \qquad f(x) = c_0 + c_1(x-a) + c_2(x-a)^2 + c_3(x-a)^3 + c_4(x-a)^4 + \cdots \quad |x-a| < R$$
Tratemos de determinar qué coeficientes ($c_n$) tienen que estar en función de ($f$). Para empezar, observe que si hacemos ($x=a$) en la ecuación 1, entonces todos los términos después del primero son $0$ y obtenemos $f(a) = c_0$.s
De acuerdo con el teorema anterior, podemos derivar la serie de la ecuación 1 término a término:
$$2 \qquad f'(x) = c_1 + 2c_2(x-a) + 3c_3(x-a)^2 + 4c_4(x-a)^3 + \cdots \quad |x-a| < R$$
y al sustituir ($x=a$) en la ecuación 2 tenemos $f'(a) = c_1$.
En seguida derivemos ambos miembros de la ecuación 2 para obtener
$$3 \qquad f''(x) = 2c_2 + 2 \cdot 3c_3(x-a) + 3 \cdot 4c_4(x-a)^2 + \cdots \quad |x-a| < R$$
Una vez más hacemos ($x = a$) en la ecuación 3. El resultado es
$$f''(a) = 2c_2$$
Apliquemos el procedimiento una vez más. La derivación de la serie de la ecuación 3 nos da
$$4 \qquad f'''(x) = 2 \cdot 3c_3 + 2 \cdot 3 \cdot 4c_4(x-a) + 3 \cdot 4 \cdot 5c_5(x-a)^2 + \cdots \quad |x-a| < R$$
y la sustitución de ($x = a$) en la ecuación 4 da
$$f'''(a) = 2 \cdot 3c_3 = 3!c_3$$
Y si continuamos derivando y sustituyendo ($x = a$), obtenemos
$$f^{(n)}(a) = 2 \cdot 3 \cdot 4 \cdot \cdots \cdot n c_n = n!c_n$$
Al resolver esta ecuación para el $n$-ésimo coeficiente ($c_n$), tenemos
$$c_n = \frac{f^{(n)}(a)}{n!}$$
Esta fórmula sigue siendo válida incluso para ($n = 0$) si adoptamos la convención de que ($0! = 1$) y ($f^{(0)} = f$). En estos términos, hemos demostrado el teorema del inciso \[[11.10 Series de Taylor y Maclaurin]]
