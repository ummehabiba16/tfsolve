---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Root A2 (gain 0.420 vs A1 0.171, A3 0.020); A2 = 0 -> 0; A2 = 1 -> A1 (gain 0.918): A1 = 1 -> 1, A1 = 0 -> 0, i.e. y = A1 AND A2. The instance (0, 1, 1) goes A2 = 1, A1 = 0, so y = 0."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree", "AIMA 4e sec. 19.3"]
---
**(i) Tree construction.** Root: 2 positive ($x_4,x_5$), 3 negative, so $H=-\frac25\log_2\frac25-\frac35\log_2\frac35=0.971$.

| Attribute | $=0$ (pos, neg) | $=1$ (pos, neg) | Remainder | Gain |
|:-:|:-:|:-:|:-:|:-:|
| $A_1$ | (0,1) | (2,2) | $\frac45(1)=0.800$ | 0.171 |
| $A_2$ | (0,2) | (2,1) | $\frac35(0.918)=0.551$ | **0.420** |
| $A_3$ | (1,2) | (1,1) | $\frac35(0.918)+\frac25(1)=0.951$ | 0.020 |

Split on **$A_2$**. $A_2=0$ is pure negative, so it is a leaf **0**.

Node $A_2=1$ (rows 3, 4, 5: outputs 0, 1, 1; $H=0.918$):

| Attribute | $=0$ | $=1$ | Remainder | Gain |
|:-:|:-:|:-:|:-:|:-:|
| $A_1$ | (0,1) | (2,0) | 0 | **0.918** |
| $A_3$ | (1,1) | (1,0) | $\frac23=0.667$ | 0.252 |

Split on **$A_1$**; both children are pure.

```text
A2 ?
|-- 0 -> y = 0
|-- 1 -> A1 ?
         |-- 0 -> y = 0
         |-- 1 -> y = 1
```

The learned function is $y=A_1\land A_2$.

**(ii) Classify $(A_1,A_2,A_3)=(0,1,1)$.** $A_2=1$ takes the right branch; then $A_1=0$ gives **$y=0$**.
