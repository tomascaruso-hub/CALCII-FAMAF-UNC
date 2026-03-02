No son elecciones arbitrarias, sino las definiciones que hacen que todo “encaje” perfectamente.
#### **La convención de ($0! = 1$)**
La definición estándar de factorial (($n! = n \cdot (n - 1) \cdot \cdots \cdot 1$)) no funciona para ($n = 0$). Sin embargo, si observamos el patrón de forma recursiva, la elección se vuelve obvia:
* ($4! = 24$)
* ($3! = \frac{4!}{4} = 6$)
* ($2! = \frac{3!}{3} = 2$)
* ($1! = \frac{2!}{2} = 1$)
Si seguimos este patrón, la única conclusión lógica es:
* ($0! = \frac{1!}{1} = 1$)
Además, esta definición es crucial en áreas como la combinatoria. La fórmula para combinaciones es $$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$Si queremos saber de cuántas maneras podemos elegir ($n$) elementos de un conjunto de ($n$) elementos, la respuesta debe ser $1$. La fórmula nos da:
$$\binom{n}{n} = \frac{n!}{n!(n-n)!} = \frac{n!}{n!0!}$$
Para que esto sea igual a 1, es necesario que ($0! = 1$). 
****
##### **La convención de $0^0=1$**
Aclarada un poco en mis notas físicas, pág **3**.

