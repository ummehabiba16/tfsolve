---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Stationary: P_inf(X) = sum_x P(X | x) P_inf(x). Two states with a = P(x2 | x1), b = P(x1 | x2): P_inf(x1) = b/(a+b), which uses only transition probabilities; and P_t(x1) - b/(a+b) = (1-a-b)^t (P_0(x1) - b/(a+b)) -> 0 for any initial distribution."
sources: ["MNM slides Lecture 5 - Markov Model (stationary distributions, mini-forward algorithm)", "AIMA 4e sec. 14.2.1"]
---
**Conditions for a stationary distribution** (first-order Markov chain). $P_\infty$ is stationary if one more transition leaves it unchanged:

$$P_\infty(X)=P_{\infty+1}(X)=\sum_{x}P(X\mid x)\,P_\infty(x),\qquad \sum_xP_\infty(x)=1,\quad P_\infty(x)\ge0.$$

In matrix form, $\boldsymbol{\pi}^{\top}=\boldsymbol{\pi}^{\top}\mathbf{T}$: $\boldsymbol\pi$ is a left eigenvector of $\mathbf{T}$ with eigenvalue 1. For it to be reached from any start, the chain must be ergodic (irreducible and aperiodic).

**Two states.** Let $a=P(X_{t+1}=x_2\mid X_t=x_1)$ and $b=P(X_{t+1}=x_1\mid X_t=x_2)$, with $0<a+b<2$:

$$\mathbf{T}=\begin{pmatrix}1-a & a\\ b & 1-b\end{pmatrix}$$

Write $p=P_\infty(x_1)$. Stationarity gives

$$p=(1-a)\,p+b\,(1-p)\ \Rightarrow\ ap=b-bp\ \Rightarrow\ \boxed{P_\infty(x_1)=\frac{b}{a+b},\quad P_\infty(x_2)=\frac{a}{a+b}}$$

These depend **only on the transition probabilities $a,b$**. The initial distribution does not appear.

**Convergence from any start.** Let $p_t=P(X_t=x_1)$. The mini-forward update gives

$$p_{t+1}=(1-a)p_t+b(1-p_t)=(1-a-b)\,p_t+b.$$

Subtract $p^*=\frac{b}{a+b}$, which satisfies $p^*=(1-a-b)p^*+b$:

$$p_{t+1}-p^*=(1-a-b)(p_t-p^*)\ \Rightarrow\ p_t-p^*=(1-a-b)^t\,(p_0-p^*).$$

Since $|1-a-b|<1$, $(1-a-b)^t\to0$, so $p_t\to p^*$ **whatever $p_0$ is**. The influence of the initial distribution decays geometrically.

*Example:* $a=0.3$, $b=0.3$ gives $P_\infty=(0.5,0.5)$. $a=0.1$, $b=0.3$ (the sun/rain chain) gives $P_\infty(\text{sun})=0.3/0.4=0.75$.
