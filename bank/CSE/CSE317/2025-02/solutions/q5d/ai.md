---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Forward message f_{1:t}(x_t) = P(x_t, e_{1:t}) = P(e_t|x_t) sum_{x_{t-1}} P(x_t|x_{t-1}) f_{1:t-1}(x_{t-1}), with f_{1:0} = P(X_0); then P(e_{1:t}) = sum_{x_t} f_{1:t}(x_t)."
sources: ["MNM slides Lecture 6 - Hidden Markov Model (forward algorithm)", "AIMA 4e sec. 14.2.1 (filtering, likelihood of the evidence sequence)"]
---
**Model.** Hidden states $X_t$, evidence $E_t$, initial distribution $P(X_0)$, transition model $P(X_t\mid X_{t-1})$ and sensor model $P(E_t\mid X_t)$, with

$$P(X_{0:t},e_{1:t})=P(X_0)\prod_{i=1}^{t}P(X_i\mid X_{i-1})\,P(e_i\mid X_i).$$

**Idea.** Summing this joint over all hidden sequences is exponential ($|X|^{t}$ terms). The forward algorithm does the sums one step at a time. Use the *unnormalized* forward message

$$\ell_{1:t}(x_t)=P(x_t,\,e_{1:t}).$$

**Recursion.** Start with $\ell_{1:0}(x_0)=P(x_0)$. For $t\ge1$:

$$\ell_{1:t}(x_t)=P(x_t,e_{1:t})=\sum_{x_{t-1}}P(x_t,x_{t-1},e_{1:t-1},e_t)$$

$$=P(e_t\mid x_t)\sum_{x_{t-1}}P(x_t\mid x_{t-1})\,P(x_{t-1},e_{1:t-1})$$

$$=P(e_t\mid x_t)\sum_{x_{t-1}}P(x_t\mid x_{t-1})\,\ell_{1:t-1}(x_{t-1}).$$

The second line uses the Markov property ($X_t$ depends only on $X_{t-1}$) and the sensor Markov property ($e_t$ depends only on $X_t$).

**Likelihood of the evidence sequence.**

$$\boxed{P(e_{1:t})=\sum_{x_t}\ell_{1:t}(x_t)}$$

In matrix form, with $\mathbf{T}_{ij}=P(X_t=j\mid X_{t-1}=i)$ and $\mathbf{O}_t=\text{diag}\big(P(e_t\mid X_t)\big)$: $\boldsymbol{\ell}_{1:t}=\mathbf{O}_t\mathbf{T}^{\top}\boldsymbol{\ell}_{1:t-1}$ and $P(e_{1:t})=\mathbf{1}^{\top}\boldsymbol{\ell}_{1:t}$.

The cost is $O(t\,|X|^2)$. The filtered estimate falls out of the same computation: $P(X_t\mid e_{1:t})=\ell_{1:t}(X_t)/P(e_{1:t})$.

*Note:* if the initial distribution is given for $X_1$ instead (as in the Berkeley slides), start with $\ell_{1:1}(x_1)=P(x_1)P(e_1\mid x_1)$.
