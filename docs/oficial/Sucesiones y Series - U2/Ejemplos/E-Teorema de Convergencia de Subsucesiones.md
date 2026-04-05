Sea la sucesión original $(a_n)_{n \in \mathbb{N}}$ definida por el término general $a_n = \frac{1}{n}$.

**Teorema a verificar:** Si $\lim_{n \to \infty} a_n = L$, entonces para toda sucesión de índices $(n_k)_{k \in \mathbb{N}} \subset \mathbb{N}$ estrictamente creciente ($n_1 < n_2 < n_3 < \dots$), se cumple que $\lim_{k \to \infty} a_{n_k} = L$.

---
Sea la sucesión de índices $n_k = 2k$.
Se verifica el orden estricto: $2k < 2(k+1) \implies n_k < n_{k+1} \quad \forall k \in \mathbb{N}$.
Definimos la subsucesión $(a_{n_k})_{k \in \mathbb{N}}$:
$$a_{n_k} = \frac{1}{n_k} = \frac{1}{2k}$$
Calculamos su límite:
$$\lim_{k \to \infty} a_{n_k} = \lim_{k \to \infty} \frac{1}{2k} = 0$$
****
Ahora, sea la sucesión de índices $n_k = k^2$.
Se verifica el orden estricto: $k^2 < (k+1)^2 \implies n_k < n_{k+1} \quad \forall k \in \mathbb{N}$.
Definimos la subsucesión $(a_{n_k})_{k \in \mathbb{N}}$:
$$a_{n_k} = \frac{1}{n_k} = \frac{1}{k^2}$$
Calculamos su límite:
$$\lim_{k \to \infty} a_{n_k} = \lim_{k \to \infty} \frac{1}{k^2} = 0$$
---
Por lo tanto...$$\lim_{k \to \infty} a_{n_k} = \lim_{n \to \infty} a_n = 0 < \infty$$