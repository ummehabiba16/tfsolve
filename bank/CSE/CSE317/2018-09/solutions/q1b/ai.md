---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Hidden state = (whose flip, coin outcome): B_H, B_T, S_H, S_T, with deterministic emission of H or T. Transitions: after any Brendan flip, Brendan again 0.6 (0.3 H, 0.3 T) or Selen 0.4 (0.2 H, 0.2 T); after S_H Selen continues (0.5/0.5); after S_T it is Brendan's turn (0.5/0.5). Start B_H/B_T 0.5 each. Decode with Viterbi or smoothing; the winner is the player of the final flip of THT."
sources: ["MNM slides Lecture 6 - Hidden Markov Model", "AIMA 4e sec. 14.3", "CMU 10-601 HMM exercise (coin game)"]
---
**Idea.** We only see the sequence of recorded flips. Who flipped each coin is hidden. Selen's stopping rule depends on the outcome of her flip (she stops after T), so the hidden state must include the **outcome** as well as the **player**. Otherwise the transitions would depend on the observation, which an HMM does not allow.

**Hidden states.** $X_t\in\{B_H,\ B_T,\ S_H,\ S_T\}$: flip $t$ was made by Brendan or Selen and landed H or T. (Brendan's extra biased coin is not recorded. It only decides whether his turn continues, so it is summed out into the transitions.)

**Observations.** $E_t\in\{H,T\}$, with a deterministic sensor model:

| $X_t$ | $P(E_t=H)$ | $P(E_t=T)$ |
|:-:|:-:|:-:|
| $B_H$, $S_H$ | 1 | 0 |
| $B_T$, $S_T$ | 0 | 1 |

**Transition model.**

- After a Brendan flip, his extra coin lands H with probability 0.4 and his turn ends. So the next flip is Brendan's with 0.6 and Selen's with 0.4, and the fair coin splits each 50/50.
- After $S_H$, Selen has not yet seen T, so she flips again.
- After $S_T$, her turn ends and Brendan flips.

| $X_{t-1}$ | $\to B_H$ | $\to B_T$ | $\to S_H$ | $\to S_T$ |
|:-:|:-:|:-:|:-:|:-:|
| $B_H$ or $B_T$ | 0.3 | 0.3 | 0.2 | 0.2 |
| $S_H$ | 0 | 0 | 0.5 | 0.5 |
| $S_T$ | 0.5 | 0.5 | 0 | 0 |

**Initial distribution.** Brendan starts: $P(X_1=B_H)=P(X_1=B_T)=0.5$.

**Termination.** The recording stops when the last three flips are T, H, T. The player of the **last** flip wins.

**Inference.** Given the recorded sequence $e_{1:n}$ (ending in THT):

- **Winner:** compute $P(X_n\mid e_{1:n})$ by the forward algorithm (filtering at the final step). The winner is Brendan if $P(X_n\in\{B_T\})>P(X_n\in\{S_T\})$, otherwise Selen.
- **Who made each flip:** smoothing (forward-backward) gives $P(X_t\mid e_{1:n})$ for each $t$, or **Viterbi** gives the single most likely assignment of flips to players.

*Note:* the "game finishes when THT appears" condition can also be enforced exactly by adding the last two outcomes to the state. With the sequence given, it is simply the end of the evidence.
