---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "H(S) = H(2,3) = 0.971; gains A1 0.171, A2 0.420, A3 0.020, so the root is A2. A2 = 0 -> 0; A2 = 1 -> split on A1 (gain 0.918): A1 = 1 -> 1, A1 = 0 -> 0. The tree computes y = A1 AND A2."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree", "AIMA 4e sec. 19.3, Exercise 19.DTLR"]
---
**Root** (5 examples: 2 positive $x_4,x_5$; 3 negative):

$$H(S)=-\tfrac25\log_2\tfrac25-\tfrac35\log_2\tfrac35=0.971.$$

| Attribute | $=0$: (pos, neg) | $=1$: (pos, neg) | Remainder | Gain |
|:-:|:-:|:-:|:-:|:-:|
| $A_1$ | (0,1) $\{x_3\}$ | (2,2) $\{x_1,x_2,x_4,x_5\}$ | $\frac15(0)+\frac45(1)=0.800$ | 0.171 |
| $A_2$ | (0,2) $\{x_1,x_2\}$ | (2,1) $\{x_3,x_4,x_5\}$ | $\frac25(0)+\frac35(0.918)=0.551$ | **0.420** |
| $A_3$ | (1,2) $\{x_1,x_3,x_5\}$ | (1,1) $\{x_2,x_4\}$ | $\frac35(0.918)+\frac25(1)=0.951$ | 0.020 |

($H(2,1)=-\frac23\log_2\frac23-\frac13\log_2\frac13=0.918$.)

Choose **$A_2$**. The branch $A_2=0$ is pure, so it is a leaf **0**.

**Node $A_2=1$** ($x_3$: 0, $x_4$: 1, $x_5$: 1; $H=0.918$):

| Attribute | $=0$ | $=1$ | Remainder | Gain |
|:-:|:-:|:-:|:-:|:-:|
| $A_1$ | (0,1) $\{x_3\}$ | (2,0) $\{x_4,x_5\}$ | 0 | **0.918** |
| $A_3$ | (1,1) $\{x_3,x_5\}$ | (1,0) $\{x_4\}$ | $\frac23(1)=0.667$ | 0.252 |

Choose **$A_1$**. Both branches are pure.

**Decision tree.**

```text
A2 ?
|-- 0 -> y = 0
|-- 1 -> A1 ?
         |-- 0 -> y = 0
         |-- 1 -> y = 1
```

The tree represents $y=A_1\land A_2$ and classifies all five examples correctly. $A_3$ is irrelevant.
