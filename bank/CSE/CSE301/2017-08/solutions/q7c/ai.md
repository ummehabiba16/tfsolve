---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'A Markov chain is a process $\{X_n\}$ on a countable state space with $P\{X_{n+1}=j\mid X_n=i,X_{n-1}=i_{n-1},\dots,X_0=i_0\}=P_{ij}$. Conditioning on the state at time $n$: $P^{n+m}_{ij}=\sum_kP^n_{ik}P^m_{kj}$ (Chapman-Kolmogorov), i.e. $P^{(n+m)}=P^{(n)}P^{(m)}$, so $P^{(n)}=P^n$.'
sources: ['CSE301 Markov_Chain slides 3-4 (definition) and 7-10 (Chapman-Kolmogorov equations)', 'Ross, Introduction to Probability Models, Ch. 4']
---
**Definition.** A stochastic process $\{X_n,\ n=0,1,2,\dots\}$ with a finite or countable set of states is a **Markov chain** if, for all states $i,j,i_0,\dots,i_{n-1}$ and all $n\ge0$,

$$P\{X_{n+1}=j\mid X_n=i,\ X_{n-1}=i_{n-1},\ \dots,\ X_0=i_0\}=P_{ij}$$

that is, given the present state, the future is independent of the past, and the one-step transition probabilities $P_{ij}$ do not depend on $n$. They satisfy $P_{ij}\ge0$ and $\sum_jP_{ij}=1$.

**Chapman-Kolmogorov equations.** Let $P^n_{ij}=P\{X_{n+m}=j\mid X_m=i\}$ be the $n$-step transition probabilities. Then for all $n,m\ge0$

$$P^{n+m}_{ij}=\sum_kP^n_{ik}\,P^m_{kj}$$

**Derivation.** Condition on the state at time $n$:

$$P^{n+m}_{ij}=P\{X_{n+m}=j\mid X_0=i\}=\sum_kP\{X_{n+m}=j,\ X_n=k\mid X_0=i\}$$

$$=\sum_kP\{X_{n+m}=j\mid X_n=k,\ X_0=i\}\,P\{X_n=k\mid X_0=i\}$$

By the Markov property (and time homogeneity) the first factor depends only on $X_n=k$ and equals $P^m_{kj}$, and the second factor is $P^n_{ik}$:

$$P^{n+m}_{ij}=\sum_kP^m_{kj}\,P^n_{ik}\qquad\blacksquare$$

**Matrix form.** With $\mathbf P^{(n)}=(P^n_{ij})$, the equations say $\mathbf P^{(n+m)}=\mathbf P^{(n)}\mathbf P^{(m)}$. Hence, by induction, $\mathbf P^{(n)}=\mathbf P^n$: the $n$-step transition probabilities are the entries of the $n$-th power of the one-step matrix. (Example: in the weather chain with $\alpha=0.7$, $\beta=0.4$, $P^4_{00}=0.5749$ is read off from $\mathbf P^4$.)
