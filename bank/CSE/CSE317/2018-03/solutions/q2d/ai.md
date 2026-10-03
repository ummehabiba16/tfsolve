---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "H(100+, 103-) = 1.000. Gain(A) = 1.000 - (103/203)(0.190) = 0.903; Gain(B) = 1.000 - (150/203)(0.918) = 0.321. Root A: A = 0 -> -; A = 1 (100+, 3-) -> B (gain 0.190): B = 1 -> +, B = 0 -> -. The concept is A AND B."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree", "AIMA 4e sec. 19.3.3"]
---
**Root:** 203 examples, 100 positive and 103 negative. $H(S)=-\frac{100}{203}\log_2\frac{100}{203}-\frac{103}{203}\log_2\frac{103}{203}=0.9998\approx1.000$.

**Attribute A.**

- $A=0$: $50+50=100$ examples, all $-$, so $H=0$.
- $A=1$: $3+100=103$ examples (100+, 3$-$): $H=-\frac{100}{103}\log_2\frac{100}{103}-\frac{3}{103}\log_2\frac{3}{103}=0.190$.

$$\text{Gain}(A)=1.000-\tfrac{103}{203}(0.190)=1.000-0.096=\mathbf{0.903}$$

**Attribute B.**

- $B=0$: $50+3=53$ examples, all $-$, so $H=0$.
- $B=1$: $50+100=150$ examples (100+, 50$-$): $H=0.918$.

$$\text{Gain}(B)=1.000-\tfrac{150}{203}(0.918)=1.000-0.679=0.321$$

**Root = A** (larger gain).

**Node $A=1$** (100+, 3$-$; $H=0.190$): only $B$ remains. $B=0$ gives (0+, 3$-$) and $B=1$ gives (100+, 0$-$), both pure, so $\text{Gain}(B)=0.190$.

```text
A ?
|-- 0 -> -          (100 examples)
|-- 1 -> B ?
         |-- 0 -> -  (3 examples)
         |-- 1 -> +  (100 examples)
```

The tree computes $A\land B$ and fits all 203 examples.
