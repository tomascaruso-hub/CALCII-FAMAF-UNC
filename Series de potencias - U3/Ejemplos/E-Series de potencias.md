**EJEMPLO 1** ¿Para qué valores de ($x$) la serie $$\sum_{n=0}^{\infty} n!x^n$$es convergente?
**SOLUCIÓN** Utilizamos la prueba de la razón. Sea ($a_n$), como se acostumbra, el $n$-ésimo término de la serie, entonces ($a_n = n!x^n$). Si ($x \neq 0$), tenemos
$$\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \left| \frac{(n+1)!x^{n+1}}{n!x^n} \right| = \lim_{n \to \infty} (n+1)|x| = \infty$$
Según la prueba de la razón, la serie es divergente cuando ($x \neq 0$). Así, la serie dada converge sólo cuando ($x = 0$).
###### **¿Por qué esto último?**
Si sustituimos ($x = 0$) directamente en la serie original, obtenemos lo siguiente:
$$\sum_{n=0}^{\infty} n! \cdot (0)^n$$
Ahora, analicemos los términos de la serie:
* **Para n = 0**: El primer término es ($0! \cdot (0)^0$). Por convención matemática, ($0! = 1$) y ($0^0 = 1$). Entonces, el primer término es ($1 \cdot 1 = 1$). Esto se profundiza un poco en **[[Convenciones convenientes para el cálculo de series]]**.
* **Para n ≥ 1**: Cualquier término será ($n! \cdot (0)^n$). Como 0 elevado a cualquier potencia positiva es 0, todos estos términos serán ($n! \cdot 0 = 0$).
Por lo tanto, la serie se convierte en:
$$1 + 0 + 0 + 0 + \cdots$$
La suma de esta serie es simplemente 1.
****
**EJEMPLO 2** ¿Para qué valores de $x$ la serie $$\sum_{n=1}^{\infty} \frac{(x-3)^n}{n}$$ es convergente?
**SOLUCIÓN** Sea ($a_n = (x-3)^n/n$). Entonces, usando la prueba de la razón,
$$\left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{(x-3)^{n+1}}{n+1} \cdot \frac{n}{(x-3)^n} \right|$$
$$= \frac{1}{1 + \frac{1}{n}} |x-3| \to |x-3| \quad \text{cuando } n \to \infty$$
De acuerdo con la prueba de la razón, la serie dada es absolutamente convergente y, por tanto, convergente cuando ($|x-3| < 1$) y divergente cuando ($|x-3| > 1$). Ahora
$$|x-3| < 1 \iff -1 < x-3 < 1 \iff 2 < x < 4$$
de modo que la serie converge cuando ($2 < x < 4$) y diverge cuando ($x < 2$) o bien ($x > 4$). La prueba de la razón no proporciona información cuando ($|x-3| = 1$) de modo que debemos considerar ($x=2$) y ($x=4$) por separado. Si ponemos ($x=4$) en la serie, resulta ($\sum 1/n$), la serie armónica, la cual es divergente. Si ($x=2$), la serie es ($\sum (-1)^n/n$), la cual es convergente de acuerdo con la prueba de la serie alternante. Por tanto, la serie de potencias dada converge para ($2 \le x < 4$).
****
**EJEMPLO APUNTE**: Sea ($\{c_n\}_{n=0}^{\infty} = \{1\}_{n=0}^{\infty}$) y ($a=0$), entonces la serie de potencias centrada en 0 tiene la forma
$$\sum_{n=0}^{\infty} x^n \quad (A) \sim \text{serie geométrica}$$
Ya sabemos que la serie (A) converge y vale
$$\frac{1}{1-x} \iff |x| < 1$$
![[Pasted image 20251031202734.png]]