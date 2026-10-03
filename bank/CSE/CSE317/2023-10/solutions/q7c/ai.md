---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Hidden state: coin in {Fair, HH, TT}; observation: seen side in {H, T}. Initial 1/3 each; T: from Fair -> HH 1/2, TT 1/2, Fair 0; from HH or TT -> 1/3 each. Sensor with 10% misreading: P(see H | Fair) = 0.5, | HH = 0.9, | TT = 0.1."
sources: ["MNM slides Lecture 6 - Hidden Markov Model", "AIMA 4e sec. 14.3", "Berkeley CS188 HMM exercises"]
---
**Hidden state.** $X_t\in\{F,\ HH,\ TT\}$: the coin picked at step $t$ (fair, two-headed, two-tailed). You never see which coin it is.

**Observation.** $E_t\in\{H,\ T\}$: the side you *believe* you saw.

**Initial distribution.** At the first step the coin is picked at random: $P(X_1)=(\frac13,\frac13,\frac13)$.

**Transition model $P(X_t\mid X_{t-1})$.** The fair coin is never picked twice in a row (then the other two are equally likely). Otherwise the pick is uniform:

| $X_{t-1}$ | $\to F$ | $\to HH$ | $\to TT$ |
|:-:|:-:|:-:|:-:|
| $F$ | 0 | 1/2 | 1/2 |
| $HH$ | 1/3 | 1/3 | 1/3 |
| $TT$ | 1/3 | 1/3 | 1/3 |

**Observation model $P(E_t\mid X_t)$.** The true side is H with probability 0.5 (fair), 1 (HH) or 0 (TT). You misread it 10% of the time:

$$P(E_t=H\mid x)=0.9\,P(\text{true }H\mid x)+0.1\,P(\text{true }T\mid x)$$

| $X_t$ | $P(E_t=H\mid X_t)$ | $P(E_t=T\mid X_t)$ |
|:-:|:-:|:-:|
| $F$ | $0.9(0.5)+0.1(0.5)=0.5$ | 0.5 |
| $HH$ | $0.9(1)+0.1(0)=0.9$ | 0.1 |
| $TT$ | $0.9(0)+0.1(1)=0.1$ | 0.9 |

```text
 X1 --> X2 --> X3 --> ...      X = coin picked (F, HH, TT)
 |      |      |
 v      v      v
 E1     E2     E3              E = side seen (H, T)
```

This is a valid HMM: the next coin depends only on the current coin (first-order Markov), and what you see depends only on the current coin.

*Note:* the true side of the toss can be summed out, which is why the hidden state needs only the coin. An equivalent, larger model uses hidden states (coin, true side).
