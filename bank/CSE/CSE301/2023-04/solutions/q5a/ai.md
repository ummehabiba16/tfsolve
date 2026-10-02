---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P_{i1}=\frac{p_i}{3}+1-p_i$, $P_{i2}=P_{i3}=\frac{p_i}{3}$, i.e. rows $(0.8,0.1,0.1)$, $(0.6,0.2,0.2)$, $(0.4,0.3,0.3)$; balance equations give $\pi_1=5/7$, $\pi_2=\pi_3=1/7$.'
sources: ['CSE301 Markov_Chain slides 3-6 and 19-22 (modelling, limiting probabilities)', 'Ross, Introduction to Probability Models, Ch. 4 (limiting probabilities)']
---
**Markov chain.** Let $X_n$ be the type of the $n$-th exam. From a type-$i$ exam, the class does well with probability $p_i$ and then the next type is uniform on $\{1,2,3\}$; it does badly with probability $1-p_i$ and then the next exam is type 1:

$$P_{i1}=\frac{p_i}{3}+(1-p_i),\qquad P_{i2}=P_{i3}=\frac{p_i}{3}$$

With $p_1=0.3$, $p_2=0.6$, $p_3=0.9$:

| From \ To | 1 | 2 | 3 |
|:-:|:-:|:-:|:-:|
| 1 | 0.8 | 0.1 | 0.1 |
| 2 | 0.6 | 0.2 | 0.2 |
| 3 | 0.4 | 0.3 | 0.3 |

**Limiting probabilities.** The chain is irreducible and aperiodic, so the long-run proportions solve

$$\pi_1=0.8\pi_1+0.6\pi_2+0.4\pi_3$$

$$\pi_2=0.1\pi_1+0.2\pi_2+0.3\pi_3$$

$$\pi_3=0.1\pi_1+0.2\pi_2+0.3\pi_3$$

$$\pi_1+\pi_2+\pi_3=1$$

The second and third equations have the same right-hand side, so $\pi_2=\pi_3$. Then the second equation gives $\pi_2=0.1\pi_1+0.5\pi_2$, so $\pi_2=0.2\pi_1$. Normalising, $\pi_1(1+0.2+0.2)=1$:

$$\pi_1=\frac57,\qquad\pi_2=\frac17,\qquad\pi_3=\frac17$$

**Answer:** in the long run $5/7\approx71.4\%$ of the exams are type 1 and $1/7\approx14.3\%$ each are type 2 and type 3.
