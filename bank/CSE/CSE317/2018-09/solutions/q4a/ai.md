---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "With row 14 = + (as read): root O (gain 0.259); O = Overcast -> +; O = Sunny -> H (High -, Normal +); O = Rain (4+, 1-) -> T or W tie (gain 0.322): T = M -> +, T = C -> W (W +, S -). If row 14 is - (as in the 2025-09 copy), the tree is the classic O, then H on Sunny and W on Rain."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree", "AIMA 4e sec. 19.3", "Mitchell, Machine Learning, ch. 3"]
---
**Data** as transcribed: 10 positive, 4 negative (row 14 read as $+$).

$$H(S)=-\tfrac{10}{14}\log_2\tfrac{10}{14}-\tfrac{4}{14}\log_2\tfrac{4}{14}=0.863$$

**Root.**

| Attribute | Values: (+, $-$) | Remainder | Gain |
|:--|:--|:-:|:-:|
| O | S (2,3): 0.971; O (4,0): 0; R (4,1): 0.722 | $\frac5{14}0.971+\frac5{14}0.722=0.605$ | **0.259** |
| T | H (2,2): 1; M (5,1): 0.650; C (3,1): 0.811 | $0.796$ | 0.067 |
| H | H (4,3): 0.985; N (6,1): 0.592 | $0.788$ | 0.075 |
| W | W (6,2): 0.811; S (4,2): 0.918 | $0.857$ | 0.006 |

Split on **O**. $O=\text{O}$ (all $+$) is a leaf **+**.

**$O=\text{S}$** (rows 1, 2, 8, 9, 11; 2+, 3$-$; $H=0.971$): Gain(T) $=0.571$, **Gain(H) $=0.971$**, Gain(W) $=0.020$. Split on H: High $\to -$ (3 rows), Normal $\to +$ (2 rows).

**$O=\text{R}$** (rows 4, 5, 6, 10, 14; 4+, 1$-$; $H=0.722$):

| Attribute | Values: (+, $-$) | Remainder | Gain |
|:--|:--|:-:|:-:|
| T | M (3,0), C (1,1) | $\frac25(1)=0.400$ | **0.322** |
| H | H (2,0), N (2,1) | $\frac35(0.918)=0.551$ | 0.171 |
| W | W (3,0), S (1,1) | $0.400$ | **0.322** |

T and W tie. Taking the first, **T**: $T=\text{M}\to+$; $T=\text{C}$ (rows 5 and 6) $\to$ split on W: Weak $\to+$, Strong $\to-$.

**Decision tree** (row 14 = $+$):

```text
O ?
|-- O (Overcast) -> +
|-- S (Sunny)    -> H ?
|                   |-- H -> -
|                   |-- N -> +
|-- R (Rain)     -> T ?
                    |-- M -> +
                    |-- C -> W ?
                             |-- W -> +
                             |-- S -> -
```

(Breaking the tie with W instead gives the equally valid Rain subtree: W = Weak $\to+$; W = Strong $\to$ T: C $\to-$, M $\to+$.)

*Note:* the table is printed on a dark, noisy background. Row 14's label is read as $+$, but this is the standard PlayTennis data, where row 14 is $-$ (as in the 2025-09 paper). With $-$, the gains are O 0.247, H 0.152, W 0.048, T 0.029, and the tree is

```text
O ?
|-- Overcast -> +
|-- Sunny    -> H ? (High -, Normal +)
|-- Rain     -> W ? (Weak +, Strong -)
```
