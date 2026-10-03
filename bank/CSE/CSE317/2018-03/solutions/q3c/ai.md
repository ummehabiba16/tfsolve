---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Purpose: exact inference is intractable (NP-hard) in large nets, so estimate posteriors from N random samples (the estimate converges as N grows). LW: fix the evidence, sample the other variables from their CPTs, weight each sample by the product of P(e_i | parents). Limitation: evidence affects only its descendants, so with evidence downstream the weights are tiny and few samples dominate. Gibbs (MCMC) resamples each non-evidence variable from P(X_i | Markov blanket), so the evidence influences all variables."
sources: ["MNM slides Uncertainty-5-BN-Sampling", "AIMA 4e sec. 13.4 (approximate inference: likelihood weighting, Gibbs sampling)"]
---
**Purpose of sampling (2).** Exact inference (enumeration, variable elimination) is exponential in the worst case (#P-hard) for large, densely connected networks. Sampling methods (Monte Carlo) **estimate** posteriors $P(X\mid\mathbf{e})$ from $N$ random samples generated with the network. They are simple and anytime, and the estimate converges to the true value as $N\to\infty$.

**Likelihood weighting (3).**

1. Fix the evidence variables $E=\mathbf{e}$.
2. Visit the variables in topological order. For a non-evidence variable, sample $x_i\sim P(X_i\mid\text{parents})$. For an evidence variable, keep its value and multiply the weight: $w\leftarrow w\times P(e_i\mid\text{parents}(E_i))$.
3. Estimate $P(x\mid\mathbf{e})=\dfrac{\sum_{\text{samples with }x}w}{\sum w}$.

No sample is rejected, unlike rejection sampling.

**Limitation and Gibbs sampling (5).** In LW, the evidence only influences the sampling of its **descendants**. The ancestors are sampled from the prior, ignoring the evidence. If the evidence is near the leaves and unlikely, most samples get tiny weights, a few samples dominate, and the estimate is poor: the effective sample size collapses.

**Gibbs sampling** (MCMC) fixes this.

- Start with the evidence fixed and the other variables set to arbitrary values.
- Repeatedly pick a non-evidence variable $X_i$ and resample it from

$$P(X_i\mid mb(X_i))\propto P(X_i\mid\text{parents}(X_i))\prod_{Y\in\text{children}(X_i)}P(y\mid\text{parents}(Y)).$$

- Count the states visited.

Because each variable is resampled given its **Markov blanket**, which includes its children, the evidence affects **every** variable, upstream ones too. No weights are needed, and the chain converges to the true posterior $P(X\mid\mathbf{e})$ as its stationary distribution.
