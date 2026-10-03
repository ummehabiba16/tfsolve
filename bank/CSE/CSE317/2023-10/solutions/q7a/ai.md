---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "R(s,a): U(s) = max_a [R(s,a) + gamma sum_{s'} P(s'|s,a) U(s')]. R(s,a,s'): U(s) = max_a sum_{s'} P(s'|s,a) [R(s,a,s') + gamma U(s')]."
sources: ["MNM slides MDP-1-SB (Bellman equation)", "AIMA 3e Exercise 17.5 / AIMA 4e sec. 17.1 (Bellman equation with R(s,a,s'))"]
---
With reward $R(s)$ for being in a state, the Bellman equation is

$$U(s)=R(s)+\gamma\max_{a\in A(s)}\sum_{s'}P(s'\mid s,a)\,U(s').$$

When the reward depends on the action, it can no longer be pulled out of the max. It has to sit inside it, and, if it also depends on the outcome, inside the expectation.

**Reward $R(s,a)$** (depends on the state and the action taken):

$$U(s)=\max_{a\in A(s)}\Big[R(s,a)+\gamma\sum_{s'}P(s'\mid s,a)\,U(s')\Big]$$

The agent receives $R(s,a)$ for sure when it takes $a$ in $s$, then continues from the random next state $s'$.

**Reward $R(s,a,s')$** (also depends on the outcome state):

$$U(s)=\max_{a\in A(s)}\sum_{s'}P(s'\mid s,a)\Big[R(s,a,s')+\gamma\,U(s')\Big]$$

The reward is now random too, so it is averaged with the same transition probabilities.

The optimal policy in each case is the corresponding $\arg\max_a$. For example, for $R(s,a,s')$:

$$\pi^*(s)=\arg\max_a\sum_{s'}P(s'\mid s,a)\,[R(s,a,s')+\gamma U(s')].$$

*Check:* if $R(s,a,s')=R(s)$, the last equation reduces to the original $R(s)$ form, because $\sum_{s'}P(s'\mid s,a)=1$.
