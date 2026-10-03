---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Restrict S = summer, sum out T: f(sun) = 0.20 + 0.10 = 0.30, f(rain) = 0.15 + 0.05 = 0.20; normalize: P(W | summer) = (sun 0.6, rain 0.4)."
sources: ["MNM slides Uncertainty-4-BN-INF (variable elimination: restrict, sum out, normalize)", "Berkeley CS188 lecture on inference (same S, T, W table)"]
---
**Query.** $P(W\mid S=\text{summer})$; evidence $S=\text{summer}$, hidden variable $T$. Here the model is a single factor, the full joint $f(S,T,W)=P(S,T,W)$.

**Step 1: restrict (select the evidence).** Keep the rows with $S=\text{summer}$, giving the factor $f_1(T,W)$:

| $T$ | $W$ | $f_1(T,W)$ |
|:-:|:-:|:-:|
| hot | sun | 0.20 |
| hot | rain | 0.15 |
| cold | sun | 0.10 |
| cold | rain | 0.05 |

**Step 2: sum out (eliminate) $T$.** $f_2(W)=\sum_tf_1(t,W)$:

$$f_2(\text{sun})=0.20+0.10=0.30,\qquad f_2(\text{rain})=0.15+0.05=0.20$$

(This is $P(\text{summer},W)$; the total $0.50=P(\text{summer})$.)

**Step 3: normalize.**

$$P(W\mid\text{summer})=\frac{f_2(W)}{0.30+0.20}=\left(\text{sun}: \frac{0.30}{0.50},\ \text{rain}: \frac{0.20}{0.50}\right)=\mathbf{(0.6,\ 0.4)}$$
