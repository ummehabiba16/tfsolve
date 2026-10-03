---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "HMM with P(S0) = 0.7, T: P(s_t | s_{t-1}) = 0.8, P(s_t | not s_{t-1}) = 0.3; sensor P(red | s) = 0.2, P(red | not s) = 0.7. Filtered P(S_t | e_{1:t}) = 0.832, 0.419, 0.229; smoothed P(S_t | e_{1:3}) = 0.683, 0.282, 0.229 (t = 1, 2, 3)."
sources: ["MNM slides Lecture 6 - Hidden Markov Model (filtering, forward algorithm)", "AIMA 4e sec. 14.2, Exercise 14.SLEP (sleepy students)"]
---
**(i) HMM.** The state variable is $X_t=EnoughSleep_t$ ($s$ or $\neg s$), and the evidence is $E_t=RedEyes_t$.

- Prior (no observations, $t=0$): $P(s_0)=0.7$.
- Transition model:

| $X_{t-1}$ | $P(s_t\mid X_{t-1})$ | $P(\neg s_t\mid X_{t-1})$ |
|:-:|:-:|:-:|
| $s$ | 0.8 | 0.2 |
| $\neg s$ | 0.3 | 0.7 |

- Sensor model:

| $X_t$ | $P(red_t\mid X_t)$ | $P(\neg red_t\mid X_t)$ |
|:-:|:-:|:-:|
| $s$ | 0.2 | 0.8 |
| $\neg s$ | 0.7 | 0.3 |

```text
 X0 --> X1 --> X2 --> X3          X = EnoughSleep
        |      |      |
        v      v      v
        E1     E2     E3          E = RedEyes
```

**(ii) Filtering.** Each step predicts, then updates:

$$P(X_t\mid e_{1:t})=\alpha\,P(e_t\mid X_t)\sum_{x_{t-1}}P(X_t\mid x_{t-1})P(x_{t-1}\mid e_{1:t-1}).$$

Evidence: $e_1=\neg red$, $e_2=red$, $e_3=red$. Vectors are $(s,\neg s)$.

| $t$ | Prediction $P(X_t\mid e_{1:t-1})$ | $\times P(e_t\mid X_t)$ | Filtered $P(X_t\mid e_{1:t})$ |
|:-:|:--|:--|:-:|
| 1 | $0.7(0.8)+0.3(0.3)=0.65$; $0.35$ | $0.65(0.8)=0.52$; $0.35(0.3)=0.105$ | (0.832, 0.168) |
| 2 | $0.832(0.8)+0.168(0.3)=0.716$; $0.284$ | $0.716(0.2)=0.143$; $0.284(0.7)=0.199$ | (0.419, 0.581) |
| 3 | $0.419(0.8)+0.581(0.3)=0.509$; $0.491$ | $0.509(0.2)=0.102$; $0.491(0.7)=0.343$ | (0.229, 0.771) |

**Smoothing** with the forward-backward algorithm: $P(X_k\mid e_{1:3})=\alpha\,f_{1:k}\times b_{k+1:3}$, where

$$b_{k+1:3}(x_k)=\sum_{x_{k+1}}P(e_{k+1}\mid x_{k+1})\,b_{k+2:3}(x_{k+1})\,P(x_{k+1}\mid x_k).$$

Backward messages, with $b_{4:3}=(1,1)$:

$$b_{3:3}=\big(0.8(0.2)+0.2(0.7),\ 0.3(0.2)+0.7(0.7)\big)=(0.30,\ 0.55)$$

$$b_{2:3}=\big(0.8(0.2)(0.30)+0.2(0.7)(0.55),\ 0.3(0.2)(0.30)+0.7(0.7)(0.55)\big)=(0.125,\ 0.2875)$$

| $k$ | $f_{1:k}$ | $b_{k+1:3}$ | product | Smoothed $P(X_k\mid e_{1:3})$ |
|:-:|:-:|:-:|:-:|:-:|
| 1 | (0.832, 0.168) | (0.125, 0.2875) | (0.104, 0.0483) | **(0.683, 0.317)** |
| 2 | (0.419, 0.581) | (0.30, 0.55) | (0.126, 0.320) | **(0.282, 0.718)** |
| 3 | (0.229, 0.771) | (1, 1) | (0.229, 0.771) | **(0.229, 0.771)** |

Smoothing lowers the estimate for day 1 (from 0.832 to 0.683): the red eyes on days 2 and 3 suggest that the student was already sleep-deprived. On the last day, smoothing equals filtering.
