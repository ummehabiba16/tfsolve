---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Hidden states {C1, C2, C3, Mid}; observations: the 2^3 = 8 binary vectors (m1, m2, m3). Sensor: product of independent microphone probabilities (corner: its own mic 0.6, others 0.1; middle: 0.4 each). Transition: corner stays 0.8, to Mid 0.1, to each other corner 0.05; Mid stays 0.7, to each corner 0.1. Initial 0.25 each."
sources: ["MNM slides Lecture 6 - Hidden Markov Model", "AIMA 4e sec. 14.3", "Berkeley CS188 HMM exercises (animal tracking)"]
---
**Hidden states.** $X_t\in\{C_1, C_2, C_3, Mid\}$: the animal is near corner 1, 2 or 3, or in the middle. Microphone $i$ sits at corner $C_i$.

**Possible observations.** Each microphone reports detected (1) or not detected (0), so $E_t=(m_1,m_2,m_3)\in\{0,1\}^3$. That gives **8 possible observations**: 000, 001, 010, 011, 100, 101, 110, 111.

**Initial distribution.** $P(X_1)=(0.25,\ 0.25,\ 0.25,\ 0.25)$.

**Transition model $P(X_{t+1}\mid X_t)$.**

| $X_t$ | $\to C_1$ | $\to C_2$ | $\to C_3$ | $\to Mid$ |
|:-:|:-:|:-:|:-:|:-:|
| $C_1$ | 0.8 | 0.05 | 0.05 | 0.1 |
| $C_2$ | 0.05 | 0.8 | 0.05 | 0.1 |
| $C_3$ | 0.05 | 0.05 | 0.8 | 0.1 |
| $Mid$ | 0.1 | 0.1 | 0.1 | 0.7 |

**Observation model $P(E_t\mid X_t)$.** Given the state, the microphones detect independently:

$$P(m_1,m_2,m_3\mid x)=\prod_{i=1}^{3}P(m_i\mid x),$$

where $P(m_i=1\mid C_i)=0.6$, $P(m_i=1\mid C_j)=0.1$ for $j\neq i$, and $P(m_i=1\mid Mid)=0.4$. For example, $P(100\mid C_1)=0.6\times0.9\times0.9=0.486$ and $P(100\mid Mid)=0.4\times0.6\times0.6=0.144$.

| $(m_1,m_2,m_3)$ | $C_1$ | $C_2$ | $C_3$ | $Mid$ |
|:-:|:-:|:-:|:-:|:-:|
| 111 | 0.006 | 0.006 | 0.006 | 0.064 |
| 110 | 0.054 | 0.054 | 0.004 | 0.096 |
| 101 | 0.054 | 0.004 | 0.054 | 0.096 |
| 100 | 0.486 | 0.036 | 0.036 | 0.144 |
| 011 | 0.004 | 0.054 | 0.054 | 0.096 |
| 010 | 0.036 | 0.486 | 0.036 | 0.144 |
| 001 | 0.036 | 0.036 | 0.486 | 0.144 |
| 000 | 0.324 | 0.324 | 0.324 | 0.216 |

Each column sums to 1 (checked).

*Note:* the paper does not say that the microphones detect independently in the middle; it is assumed, as for the corners ("independently detected").
