**EJEMPLO 4.** Determine el radio de convergencia y el intervalo de convergencia de la serie$$\sum_{n=0}^{\infty} \frac{(-3)^n x^n}{\sqrt{n+1}}$$**SOLUCIÓN** Sea ($a_n = (-3)^n x^n / \sqrt{n+1}$). Entonces

$$\left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{(-3)^{n+1} x^{n+1}}{\sqrt{n+2}} \cdot \frac{\sqrt{n+1}}{(-3)^n x^n} \right| = \left| -3x \sqrt{\frac{n+1}{n+2}} \right|$$
$$= 3 \sqrt{\frac{1 + (1/n)}{1 + (2/n)}} |x| \to 3|x| \quad \text{cuando } n \to \infty$$
De acuerdo con la prueba de la razón, la serie dada converge si ($3|x| < 1$) y es divergente si ($3|x| > 1$). En estos términos, es convergente si ($|x| < \frac{1}{3}$) y divergente si ($|x| > \frac{1}{3}$). Esto significa que el radio de convergencia es ($R = \frac{1}{3}$).

Sabemos que la serie converge en el intervalo ($(-\frac{1}{3}, \frac{1}{3})$), pero ahora es necesario probar si hay convergencia en los extremos de este intervalo. Si ($x = -\frac{1}{3}$), la serie se transforma en
$$\sum_{n=0}^{\infty} \frac{(-3)^n (-\frac{1}{3})^n}{\sqrt{n+1}} = \sum_{n=0}^{\infty} \frac{1}{\sqrt{n+1}} = \frac{1}{\sqrt{1}} + \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{3}} + \frac{1}{\sqrt{4}} + \cdots$$
la cual es divergente. (Aplique la prueba de la integral o simplemente observe que es una serie ($p$) con ($p = \frac{1}{2} < 1$).) Si ($x = \frac{1}{3}$), la serie es
$$\sum_{n=0}^{\infty} \frac{(-3)^n (\frac{1}{3})^n}{\sqrt{n+1}} = \sum_{n=0}^{\infty} \frac{(-1)^n}{\sqrt{n+1}}$$
la cual converge de acuerdo con la prueba de la serie alternante. Por tanto, la serie de potencias dada converge cuando ($-\frac{1}{3} < x \le \frac{1}{3}$), de modo que el intervalo de convergencia es ($(-\frac{1}{3}, \frac{1}{3}]$).
****
**EJEMPLO NOTAS.** $$\sum_{n=1}^{\infty} \frac{(-1)^{n+1} 2^n}{n 3^n} (x-1)^n$$ (notar que $a=1$)
Tenemos que $$\lim_{n \to \infty} \frac{|c_{n+1}|}{|c_n|} = \lim_{n \to \infty} \frac{\frac{2^{n+1}}{(n+1) 3^{n+1}}}{\frac{2^n}{n 3^n}} = \lim_{n \to \infty} \frac{2}{3} \frac{n}{n+1} = \frac{2}{3}$$. Luego $R = \frac{3}{2}$
Veamos qué pasa en ($x = a - R = 1 - \frac{3}{2}$) y en ($x = a + R = 1 + \frac{3}{2}$)
* Si ($x = 1 - \frac{3}{2}$), obtenemos $$\sum_{n=1}^{\infty} \frac{(-1)^{n+1} 2^n}{n 3^n} \left(-\frac{3}{2}\right)^n = \sum_{n=1}^{\infty} \frac{(-1)^{2n+1} 1}{n} \to \text{diverge}$$ (por ser serie armónica)

* Si ($x = 1 + \frac{3}{2}$), obtenemos $$\sum_{n=1}^{\infty} \frac{(-1)^{n+1} 2^n}{n 3^n} \left(\frac{3}{2}\right)^n = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} \to \text{converge}$$ (por criterio para series alternantes)
Por lo tanto, el intervalo de convergencia es ($I = (1 - \frac{3}{2}, 1 + \frac{3}{2}] = (-\frac{1}{2}, \frac{5}{2}]$)
