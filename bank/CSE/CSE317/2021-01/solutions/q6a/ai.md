---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "H(100+, 85-) = 0.995. Gain(A) = 0.995 - (110/185)(0.440) = 0.734 > Gain(B) = 0.995 - (125/185)(0.722) = 0.508, so the root is A. A = 0 -> -; A = 1 (100+, 10-) split on B (gain 0.440): B = 1 -> +, B = 0 -> -. The tree is A AND B."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree", "AIMA 4e sec. 19.3.3"]
---
**Root:** 185 examples, 100 positive and 85 negative.

$$H(S)=-\tfrac{100}{185}\log_2\tfrac{100}{185}-\tfrac{85}{185}\log_2\tfrac{85}{185}=0.995$$

**Attribute $A$.**

- $A=0$: $50+25=75$ examples, all negative, so $H=0$.
- $A=1$: $10+100=110$ examples (100+, 10$-$):

$$H=-\tfrac{100}{110}\log_2\tfrac{100}{110}-\tfrac{10}{110}\log_2\tfrac{10}{110}=0.440$$

$$\text{Gain}(A)=0.995-\Big(\tfrac{75}{185}(0)+\tfrac{110}{185}(0.440)\Big)=0.995-0.261=\mathbf{0.734}$$

**Attribute $B$.**

- $B=0$: $50+10=60$ examples, all negative, so $H=0$.
- $B=1$: $25+100=125$ examples (100+, 25$-$):

$$H=-\tfrac{100}{125}\log_2\tfrac{100}{125}-\tfrac{25}{125}\log_2\tfrac{25}{125}=0.722$$

$$\text{Gain}(B)=0.995-\tfrac{125}{185}(0.722)=0.995-0.488=0.508$$

$A$ has the larger gain, so **$A$ is the root**.

**Node $A=1$** (100+, 10$-$; $H=0.440$). Only $B$ is left: $B=0\to(0+,10-)$ and $B=1\to(100+,0-)$, both pure, so $\text{Gain}(B)=0.440-0=0.440$. Split on $B$.

**Decision tree.**

```text
A ?
|-- 0 -> -           (75 examples)
|-- 1 -> B ?
         |-- 0 -> -  (10 examples)
         |-- 1 -> +  (100 examples)
```

The learned concept is $A\land B$, and it classifies all 185 examples correctly.
