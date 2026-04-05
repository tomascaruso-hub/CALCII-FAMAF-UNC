#### **Concepto**
Dada una sucesión $(a_n)$, podemos extraer sucesiones descartando algunos términos. 
Cada nueva sucesión se llama **subsucesión**.
#### **Definición** **formal**
Dada una sucesión de números reales $(a_n)_{n=1}^\infty$, una **subsucesión** es una nueva sucesión $(a_{n_k})_{k=1}^\infty$ que se obtiene seleccionando ciertos términos de la sucesión original, manteniendo estrictamente el orden en el que aparecían.
Para que el orden se mantenga, los índices seleccionados deben formar una sucesión de números naturales estrictamente creciente. Es decir, los índices $n_k$ deben cumplir que:
$$n_1 < n_2 < n_3 < \cdots < n_k < \cdots$$
**[[E-Subsucesiones]]**
****
##### **Teorema de Convergencia de Subsucesiones**
Si $\lim_{n \to \infty} a_n = L$, entonces para cualquier subsucesión $(a_{n_k})$, se cumple que:
$$\lim_{k \to \infty} a_{n_k} = L$$
****
**En otras palabras.** Sea $(a_n)$ una sucesión de números reales. Si la sucesión $(a_n)$ converge a un límite $L$, entonces toda subsucesión $(a_{n_k})$ extraída de ella también es convergente y su límite es exactamente el mismo $L$.
**[[E-Teorema de Convergencia de Subsucesiones]]**
****
##### **En la práctica**
La definición de límite nos dice que, a medida que avanzamos en la sucesión original, todos los términos terminan agrupándose infinitamente cerca del valor $L$. 
Como una subsucesión se forma simplemente tomando términos de esa misma sucesión cada vez más adelante (sin alterar el orden), es inevitable que esos términos seleccionados también queden "atrapados" en esa misma cercanía hacia $L$. 

**Observación.** Este teorema se usa muchísimo más para demostrar que una sucesión diverge. 
- Si logramos encontrar una **subsucesión** que diverge.
- O si logramos encontrar dos **subsucesiones** que convergen a límites distintos.
$$\implies \text{ Entonces podemos afirmar con absoluta seguridad que la sucesión original diverge.}$$