---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'From $Q^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}$: $F_{2k}=F_k(2F_{k+1}-F_k)$ and $F_{2k+1}=F_k^2+F_{k+1}^2$; processing the bits of $n$ (repeated squaring) needs $O(\log n)$ arithmetic operations.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (Fibonacci numbers)', 'Cormen et al., Introduction to Algorithms (matrix power by repeated squaring)']
---
The recurrence $F_{n+1}=F_n+F_{n-1}$ ($F_0=0$, $F_1=1$) takes $n$ steps if applied directly. Write it in matrix form:

$$\begin{pmatrix}F_{n+1}\\F_n\end{pmatrix}=\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}F_n\\F_{n-1}\end{pmatrix}$$

With $Q=\begin{pmatrix}1&1\\1&0\end{pmatrix}$, induction on $n$ gives

$$Q^n=\begin{pmatrix}F_{n+1}&F_n\\F_n&F_{n-1}\end{pmatrix}\qquad(n\ge1)$$

**Repeated squaring.** $Q^n$ can be computed with $O(\log n)$ $2\times2$ matrix multiplications: $Q^{2k}=(Q^k)^2$ and $Q^{2k+1}=(Q^k)^2Q$, so each bit of $n$ costs at most two multiplications.

**Doubling formulas.** Comparing the entries of $Q^{2k}=Q^kQ^k$:

$$F_{2k}=F_k(F_{k+1}+F_{k-1})=F_k\,(2F_{k+1}-F_k)$$

$$F_{2k+1}=F_{k+1}^2+F_k^2$$

**Algorithm.**

```python
def fib_pair(n):            # returns (F(n), F(n+1))
    if n == 0:
        return (0, 1)
    a, b = fib_pair(n // 2)  # a = F(k), b = F(k+1), k = n // 2
    c = a * (2 * b - a)      # F(2k)
    d = a * a + b * b        # F(2k+1)
    if n % 2 == 0:
        return (c, d)
    return (d, c + d)        # (F(2k+1), F(2k+2))
```

Each call halves $n$, so there are $\lfloor\log_2n\rfloor+1$ levels, each with a constant number of multiplications: **$O(\log n)$ arithmetic operations** (the numbers themselves have $O(n)$ bits, so with big integers the cost is dominated by the last few multiplications).

**Example: $F_{10}$.** $10=1010_2$; the calls go $n=1,2,5,10$:

| $n$ | $(F_n,F_{n+1})$ | how |
|:-:|:-:|:--|
| 1 | $(1,1)$ | from $k=0$: $(0,1)$ doubled to $(0,1)$, odd: $(1,1)$ |
| 2 | $(1,2)$ | $F_2=1(2\cdot1-1)=1$, $F_3=1+1=2$ |
| 5 | $(5,8)$ | $F_4=1(2\cdot2-1)=3$, $F_5=1+4=5$; odd: $(5,8)$ |
| 10 | $(55,89)$ | $F_{10}=5(2\cdot8-5)=55$, $F_{11}=25+64=89$ |

(Binet's formula $F_n=(\phi^n-\hat\phi^n)/\sqrt5$ is also $O(\log n)$ with fast powering, but it needs high-precision real arithmetic; the integer method above is exact.)
