---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Forward: f1 = (0.24, 0.08), f2 = (0.08, 0.024), f3 = (0.0328, 0.00384) for (H, C); P(X3 | M,M,L) = (0.895, 0.105). Backward: b2 = (0.38, 0.26), b1 = (0.122, 0.092); P(X1 | M,M,L) = (0.799, 0.201)."
sources: ["MNM slides Lecture 6 - Hidden Markov Model (forward algorithm)", "AIMA 4e sec. 14.2 (filtering and smoothing, forward-backward)", "Stamp, 'A Revealing Introduction to Hidden Markov Models' (same tree-ring example)"]
---
**Model** (state order $[H, C]$).

- Initial: $P(X_1)=[0.6,\ 0.4]$.
- Transition: $P(H\mid H)=0.7$, $P(C\mid H)=0.3$; $P(H\mid C)=0.4$, $P(C\mid C)=0.6$.
- Sensor:

| $X_t$ | $P(S\mid X_t)$ | $P(M\mid X_t)$ | $P(L\mid X_t)$ |
|:-:|:-:|:-:|:-:|
| H | 0.1 | 0.4 | 0.5 |
| C | 0.7 | 0.2 | 0.1 |

$P(L\mid X_t)=1-P(S\mid X_t)-P(M\mid X_t)$. Evidence: $e_1=M$, $e_2=M$, $e_3=L$.

**(i) Forward algorithm.** $f_t(x)=P(x_t,e_{1:t})$, with $f_1(x)=P(x)P(e_1\mid x)$ and

$$f_{t}(x_t)=P(e_t\mid x_t)\sum_{x_{t-1}}P(x_t\mid x_{t-1})f_{t-1}(x_{t-1}).$$

$t=1$, $e_1=M$: $f_1(H)=0.6(0.4)=0.24$, $f_1(C)=0.4(0.2)=0.08$.

$t=2$, $e_2=M$: predict $0.24(0.7)+0.08(0.4)=0.20$ for $H$ and $0.24(0.3)+0.08(0.6)=0.12$ for $C$. Then $f_2(H)=0.20(0.4)=0.08$ and $f_2(C)=0.12(0.2)=0.024$.

$t=3$, $e_3=L$: predict $0.08(0.7)+0.024(0.4)=0.0656$ for $H$ and $0.08(0.3)+0.024(0.6)=0.0384$ for $C$. Then $f_3(H)=0.0656(0.5)=0.0328$ and $f_3(C)=0.0384(0.1)=0.00384$.

| $t$ | $e_t$ | $f_t(H)$ | $f_t(C)$ | normalized $P(X_t\mid e_{1:t})$ |
|:-:|:-:|:-:|:-:|:-:|
| 1 | M | 0.24 | 0.08 | (0.750, 0.250) |
| 2 | M | 0.08 | 0.024 | (0.769, 0.231) |
| 3 | L | 0.0328 | 0.00384 | (0.895, 0.105) |

$P(e_{1:3})=0.0328+0.00384=0.03664$, so

$$P(X_3\mid e_1,e_2,e_3)=\left(\tfrac{0.0328}{0.03664},\ \tfrac{0.00384}{0.03664}\right)=\mathbf{(H:0.895,\ C:0.105)}.$$

**(ii) Backward algorithm.** $b_k(x)=P(e_{k+1:3}\mid x_k)$, with $b_3=(1,1)$ and

$$b_k(x_k)=\sum_{x_{k+1}}P(e_{k+1}\mid x_{k+1})\,b_{k+1}(x_{k+1})\,P(x_{k+1}\mid x_k).$$

$k=2$, $e_3=L$: $b_2(H)=0.7(0.5)(1)+0.3(0.1)(1)=0.38$ and $b_2(C)=0.4(0.5)+0.6(0.1)=0.26$.

$k=1$, $e_2=M$: $b_1(H)=0.7(0.4)(0.38)+0.3(0.2)(0.26)=0.1064+0.0156=0.122$ and $b_1(C)=0.4(0.4)(0.38)+0.6(0.2)(0.26)=0.0608+0.0312=0.092$.

| $k$ | $b_k(H)$ | $b_k(C)$ |
|:-:|:-:|:-:|
| 3 | 1 | 1 |
| 2 | 0.38 | 0.26 |
| 1 | 0.122 | 0.092 |

**Smoothing.** $P(X_1\mid e_{1:3})=\alpha\,f_1\times b_1$:

$$(0.24\times0.122,\ 0.08\times0.092)=(0.02928,\ 0.00736),$$

whose sum is again $0.03664=P(e_{1:3})$. So

$$P(X_1\mid e_1,e_2,e_3)=\mathbf{(H:0.799,\ C:0.201)}.$$

(For comparison, $P(X_2\mid e_{1:3})=(0.830,\ 0.170)$.)

*Note:* "initial probability" is taken as $P(X_1)$, the distribution at the first observation (as in the Berkeley slides and Stamp's example). If it is $P(X_0)$ instead (AIMA's convention), then $P(X_1)=(0.58,\ 0.42)$, $P(X_3\mid e_{1:3})=(0.895,\ 0.105)$ (unchanged to three decimals) and $P(X_1\mid e_{1:3})=(0.786,\ 0.214)$.
