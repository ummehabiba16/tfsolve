---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Root O (gain 0.247). O = O: +. O = S: split on H (gain 0.971): H -> -, N -> +. O = R: split on W (gain 0.971): W -> +, S -> -."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree (information gain)", "AIMA 4e sec. 19.3.3", "Mitchell, Machine Learning, ch. 3 (PlayTennis)"]
---
**Entropy and gain.** For a set $S$ with $p$ positive and $n$ negative examples,

$$H(S)=-\tfrac{p}{p+n}\log_2\tfrac{p}{p+n}-\tfrac{n}{p+n}\log_2\tfrac{n}{p+n},$$

$$\text{Gain}(S,A)=H(S)-\sum_{v}\frac{|S_v|}{|S|}H(S_v).$$

Useful values: $H(2,3)=H(3,2)=0.971$, $H(4,2)=0.918$, $H(3,1)=H(6,2)=0.811$, $H(3,4)=0.985$, $H(6,1)=0.592$, $H(k,k)=1$, $H(k,0)=0$.

**Step 1: root (all 14 examples, 9+, 5$-$).** $H(S)=-\frac{9}{14}\log_2\frac{9}{14}-\frac{5}{14}\log_2\frac{5}{14}=0.940$.

| Attribute | Value: (+, $-$) | Remainder | Gain |
|:--|:--|:-:|:-:|
| O | S: (2,3), O: (4,0), R: (3,2) | $\frac{5}{14}0.971+0+\frac{5}{14}0.971=0.694$ | **0.247** |
| T | H: (2,2), M: (4,2), C: (3,1) | $\frac{4}{14}1+\frac{6}{14}0.918+\frac{4}{14}0.811=0.911$ | 0.029 |
| H | H: (3,4), N: (6,1) | $\frac{7}{14}0.985+\frac{7}{14}0.592=0.788$ | 0.152 |
| W | W: (6,2), S: (3,3) | $\frac{8}{14}0.811+\frac{6}{14}1=0.892$ | 0.048 |

**O** has the largest gain and becomes the root. $O=\text{O}$ (examples 3, 7, 12, 13) is all $+$, so it is a leaf **+**.

**Step 2: $O=\text{S}$** (examples 1, 2, 8, 9, 11; 2+, 3$-$; $H=0.971$).

| Attribute | Value: (+, $-$) | Remainder | Gain |
|:--|:--|:-:|:-:|
| T | H: (0,2), M: (1,1), C: (1,0) | $\frac{2}{5}(1)=0.400$ | 0.571 |
| H | H: (0,3), N: (2,0) | 0 | **0.971** |
| W | W: (1,2), S: (1,1) | $\frac{3}{5}0.918+\frac{2}{5}1=0.951$ | 0.020 |

Split on **H**: $H=\text{H}\to -$ and $H=\text{N}\to +$. Both children are pure.

**Step 3: $O=\text{R}$** (examples 4, 5, 6, 10, 14; 3+, 2$-$; $H=0.971$).

| Attribute | Value: (+, $-$) | Remainder | Gain |
|:--|:--|:-:|:-:|
| T | M: (2,1), C: (1,1) | $\frac{3}{5}0.918+\frac{2}{5}1=0.951$ | 0.020 |
| H | H: (1,1), N: (2,1) | $0.951$ | 0.020 |
| W | W: (3,0), S: (0,2) | 0 | **0.971** |

Split on **W**: $W=\text{W}\to +$ and $W=\text{S}\to -$. Both children are pure.

**Final decision tree.**

```text
O ?
|-- S (Sunny)    -> H ?
|                   |-- H (High)   -> Play = -
|                   |-- N (Normal) -> Play = +
|-- O (Overcast) -> Play = +
|-- R (Rain)     -> W ?
                    |-- W (Weak)   -> Play = +
                    |-- S (Strong) -> Play = -
```

All 14 training examples are classified correctly, and $T$ is never used. (This is the classic PlayTennis tree.)
