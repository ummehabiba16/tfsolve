---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Viterbi is dynamic programming over the trellis: m_{1:1} = P(X_1) P(e_1 | X_1); m_{1:t+1}(x) = P(e_{t+1} | x) max_{x'} P(x | x') m_{1:t}(x'), storing the arg max as a back-pointer; at the end take argmax_x m_{1:T}(x) and follow the back-pointers. O(T |X|^2) time, instead of enumerating |X|^T sequences."
sources: ["MNM slides Lecture 6 - Hidden Markov Model", "AIMA 4e sec. 14.2.3 (finding the most likely sequence, Viterbi)"]
---
**Problem.** Find $\arg\max_{x_{1:T}}P(x_{1:T}\mid e_{1:T})$, the single most likely state sequence. That is not the sequence of individually most likely states. Enumerating all $|X|^T$ sequences is infeasible.

**Key idea.** The most likely path to state $x$ at time $t+1$ consists of the most likely path to some state $x'$ at time $t$, followed by the transition $x'\to x$. Define

$$m_{1:t}(x_t)=\max_{x_{1:t-1}}P(x_{1:t-1},x_t,e_{1:t}).$$

**Algorithm.**

1. *Initialize:* $m_{1:1}(x)=P(x)\,P(e_1\mid x)$ for every state $x$ (or $\sum_{x_0}P(x\mid x_0)P(x_0)$ if the prior is on $X_0$).
2. *Recursion*, for $t=1,\dots,T-1$, for each state $x$:

$$m_{1:t+1}(x)=P(e_{t+1}\mid x)\max_{x'}\big[P(x\mid x')\,m_{1:t}(x')\big],\qquad \text{bp}_{t+1}(x)=\arg\max_{x'}P(x\mid x')\,m_{1:t}(x').$$

This is the forward algorithm with the **sum replaced by max**.

3. *Termination:* $x_T^*=\arg\max_xm_{1:T}(x)$, and the path probability is $\max_xm_{1:T}(x)$.
4. *Backtrack:* $x_t^*=\text{bp}_{t+1}(x_{t+1}^*)$ for $t=T-1,\dots,1$.

**Complexity.** $O(T\,|X|^2)$ time and $O(T\,|X|)$ space for the back-pointers. Logs are used to avoid underflow ($\log$ of products becomes sums). It is used in speech recognition, part-of-speech tagging and decoding.
