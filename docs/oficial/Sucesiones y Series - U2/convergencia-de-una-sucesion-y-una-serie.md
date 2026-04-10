### **Convergencia de una Sucesión (la lista)**
Una sucesión $(a_n)$ es simplemente una lista infinita de números ordenados: $a_1, a_2, a_3, \dots, a_n$.
Cuando queremos ver si una **sucesión converge**, nos estamos preguntando: "al recorrer esta lista hacia el infinito, ¿los números se van acercando a un valor específico?".
Calculamos el límite directo del término general:
$$
L = \lim_{n \to \infty} a_n
$$
****
### **Convergencia de una Serie (las sumas parciales)**
Una serie ($\sum a_n$) es la **suma infinita** de todos los elementos de esa lista: $a_1 + a_2 + a_3 + \dots$
Como no podemos sumar infinitos números de golpe, usamos el concepto de **sumas parciales** ($S_n$). Una suma parcial es ir sumando los términos acumulados hasta la posición $n$:
*   $S_1 = a_1$
*   $S_2 = a_1 + a_2$
*   $S_3 = a_1 + a_2 + a_3$
*   $S_n = \sum_{i=1}^n a_i$
Cuando queremos ver si una **serie converge**, nos estamos preguntando: "Si sigo acumulando y sumando estos números para siempre, ¿el resultado total se **estabiliza** en un número o **explota** hacia el infinito?"
Calculamos **límite de la sucesión de sumas parciales**:
$$
S = \lim_{n \to \infty} S_n
$$