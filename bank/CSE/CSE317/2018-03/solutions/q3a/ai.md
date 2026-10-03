---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Smoothing: P(X_k | e_{1:t}) = alpha f_{1:k}(X_k) x b_{k+1:t}(X_k), with forward f_{1:k} = P(X_k | e_{1:k}) (filtering) and backward b_{k+1:t}(x_k) = P(e_{k+1:t} | x_k) = sum_{x_{k+1}} P(e_{k+1} | x_{k+1}) b_{k+2:t}(x_{k+1}) P(x_{k+1} | x_k), b_{t+1:t} = 1."
sources: ["MNM slides Lecture 6 - Hidden Markov Model", "AIMA 4e sec. 14.2.2 (smoothing, forward-backward algorithm)"]
---
**Split the evidence** at $k$ into $e_{1:k}$ (past) and $e_{k+1:t}$ (future). Bayes' rule and the Markov property ($e_{k+1:t}$ is independent of $e_{1:k}$ given $X_k$) give

$$P(X_k\mid e_{1:t})=\alpha\,P(X_k\mid e_{1:k})\,P(e_{k+1:t}\mid X_k)=\alpha\,\mathbf{f}_{1:k}\times\mathbf{b}_{k+1:t}.$$

**Forward message** (filtering), computed from $t=1$ up to $k$:

$$\mathbf{f}_{1:j+1}=\alpha\,P(e_{j+1}\mid X_{j+1})\sum_{x_j}P(X_{j+1}\mid x_j)\,\mathbf{f}_{1:j}(x_j),\quad \mathbf{f}_{1:0}=P(X_0).$$

**Backward message**, computed from $t$ down to $k+1$:

$$\mathbf{b}_{k+1:t}(x_k)=P(e_{k+1:t}\mid x_k)=\sum_{x_{k+1}}P(e_{k+1}\mid x_{k+1})\,\mathbf{b}_{k+2:t}(x_{k+1})\,P(x_{k+1}\mid x_k),$$

starting with $\mathbf{b}_{t+1:t}=\mathbf{1}$ (the empty future has probability 1).

**Result.** Multiply the two messages pointwise and normalize. Doing this for every $k$ at once is the **forward-backward algorithm**: one forward pass storing all $\mathbf{f}$, then one backward pass, in total time $O(t\,|X|^2)$.

*Example* (umbrella world, $e_1=e_2=$ umbrella): $\mathbf{f}_{1:1}=\langle0.818,0.182\rangle$ and $\mathbf{b}_{2:2}=\langle0.69,0.41\rangle$, so $P(R_1\mid u_1,u_2)=\alpha\langle0.818\times0.69,\ 0.182\times0.41\rangle=\langle0.883,0.117\rangle$.
