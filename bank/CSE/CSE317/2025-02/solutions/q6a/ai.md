---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "States {High, Medium, Low}; actions {Spin, NoSpin}; Spin: H->H 0.8, H->M 0.2; M->H 0.7, M->M 0.1, M->L 0.2; L->M 0.7, L->L 0.3; NoSpin: H->M, M->L, L->L (prob 1). Rewards R(H) = 3-1 = +2, R(M) = R(L) = -1; infinite horizon with discount gamma < 1."
sources: ["MNM slides MDP-1-SB (definition of an MDP)", "AIMA 3e sec. 17.1"]
---
An MDP is the tuple $(S, A, P(s'\mid s,a), R(s), \gamma)$, with initial state as given.

**States.** $S=\{\text{High (H)},\ \text{Medium (M)},\ \text{Low (L)}\}$, the rover's position on the slope. There is no terminal state.

**Actions.** $A(s)=\{\text{Spin},\ \text{NoSpin}\}$ in every state.

**Transition model $P(s'\mid s,a)$.**

*Spin:* move up with 0.7 ("stays high" when already High), stay with 0.1 (malfunction), move down with 0.2 ("stays low" when already Low).

| $s$ | $\to$ H | $\to$ M | $\to$ L |
|:-:|:-:|:-:|:-:|
| H | $0.7+0.1=0.8$ | 0.2 | 0 |
| M | 0.7 | 0.1 | 0.2 |
| L | 0 | 0.7 | $0.1+0.2=0.3$ |

*NoSpin:* always slides one step down, or stays Low.

| $s$ | $\to$ H | $\to$ M | $\to$ L |
|:-:|:-:|:-:|:-:|
| H | 0 | 1 | 0 |
| M | 0 | 0 | 1 |
| L | 0 | 0 | 1 |

**Reward model $R(s)$** (energy gained per time step in state $s$). Every time step costs 1 unit; being High gains 3 units from the solar panels.

| $s$ | $R(s)$ |
|:-:|:-:|
| H | $3-1=+2$ |
| M | $-1$ |
| L | $-1$ |

**Objective.** The process never ends (no terminal state), so use discounted rewards with $0<\gamma<1$. Maximize

$$U^\pi(s)=E\Big[\sum_{t=0}^{\infty}\gamma^tR(S_t)\Big],$$

and the optimal utilities satisfy

$$U(s)=R(s)+\gamma\max_{a}\sum_{s'}P(s'\mid s,a)U(s').$$

*Notes:*

- *Assumption:* the reward depends only on the state (spinning itself costs no extra energy), and some discount $\gamma<1$ is used, because the task is infinite-horizon.
- *Check (not asked):* with $\gamma=0.9$, value iteration gives $U(\text{H})=13.12$, $U(\text{M})=9.31$, $U(\text{L})=6.66$, and the optimal policy is **Spin** in every state.
