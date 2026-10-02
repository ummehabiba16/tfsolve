---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Exams 2 to 10 must all be type 2 or 3: from type 3 that happens w.p. $0.6$, and afterwards (type 2 or 3, equally likely) w.p. $\frac{0.4+0.6}{2}=0.5$ each step, so $P=0.6\times0.5^8=0.00234$.'
sources: ['CSE301 Markov_Chain slides 7-10 (n-step transition probabilities)', 'Ross, Introduction to Probability Models, Ch. 4 (Chapman-Kolmogorov equations)']
---
**Markov chain.** Let $X_n$ be the type of the $n$-th exam. From a type-$i$ exam, the class does well with probability $p_i$ and then the next type is uniform on $\{1,2,3\}$; it does badly with probability $1-p_i$ and then the next exam is type 1:

$$P_{i1}=\frac{p_i}{3}+(1-p_i),\qquad P_{i2}=P_{i3}=\frac{p_i}{3}$$

With $p_1=0.3$, $p_2=0.6$, $p_3=0.9$:

| From \ To | 1 | 2 | 3 |
|:-:|:-:|:-:|:-:|
| 1 | 0.8 | 0.1 | 0.1 |
| 2 | 0.6 | 0.2 | 0.2 |
| 3 | 0.4 | 0.3 | 0.3 |

**No type-1 exam among the first 10.** Exam 1 is type 3, so exams $2,3,\dots,10$ (nine transitions) must all avoid type 1. Restrict the transition matrix to the states $\{2,3\}$:

$$Q=\begin{pmatrix}P_{22}&P_{23}\\P_{32}&P_{33}\end{pmatrix}=\begin{pmatrix}0.2&0.2\\0.3&0.3\end{pmatrix}$$

The required probability is the sum of the entries of row "3" of $Q^9$.

**Step by step.** From type 3, the next exam avoids type 1 with probability $P_{32}+P_{33}=0.6$, and then it is type 2 or 3 with equal probability ($0.3$ each). From such a 50/50 mix, the next exam avoids type 1 with probability $\frac12(0.4)+\frac12(0.6)=0.5$, and it is again type 2 or type 3 with equal probability (each row of $Q$ has equal entries). So every one of the remaining 8 transitions avoids type 1 with probability 0.5:

$$P(\text{no type 1 in exams }1\text{-}10\mid X_1=3)=0.6\times(0.5)^8=\frac{0.6}{256}=0.00234375$$

(Equivalently, $Q$ has rank 1, $Q=\binom{0.2}{0.3}(1\ \ 1)$, so $Q^9=(0.5)^8Q$ and the row-3 sum is $0.5^8\times0.6$.)

**Answer:** $\approx\mathbf{0.0023}$.
