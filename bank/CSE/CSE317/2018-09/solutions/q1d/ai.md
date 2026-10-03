---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Gibbs sampling (MCMC): fix the evidence, start with a random assignment to the other variables, repeatedly choose a non-evidence variable and resample it from P(X_i | Markov blanket(X_i)); count the states visited. The chain's stationary distribution is P(X | e), so the counts converge to the posterior."
sources: ["MNM slides Uncertainty-5-BN-Sampling (Gibbs sampling)", "AIMA 4e sec. 13.4.2 (MCMC, Gibbs sampling)"]
---
**Gibbs sampling** is a Markov chain Monte Carlo (MCMC) method for $P(X\mid\mathbf{e})$ in a Bayesian network.

**Algorithm.**

1. Fix the evidence variables to their observed values $\mathbf{e}$.
2. Initialize every non-evidence variable (query and hidden) to an arbitrary value. This gives the current state $\mathbf{x}$.
3. Repeat $N$ times: choose a non-evidence variable $X_i$ (in turn, or at random) and **resample** it from its distribution given its **Markov blanket** (parents, children, children's other parents):

$$P(x_i\mid mb(X_i))=\alpha\,P(x_i\mid\text{parents}(X_i))\prod_{Y_j\in\text{children}(X_i)}P(y_j\mid\text{parents}(Y_j));$$

Record the new state and count the value of the query variable.

4. Estimate $P(X=x\mid\mathbf{e})\approx\dfrac{\text{count}(x)}{N}$, usually after discarding the first "burn-in" samples.

**Why it works.** Each step is a transition of a Markov chain over the complete assignments. The chain is in *detailed balance* with the true posterior $P(\mathbf{x}\mid\mathbf{e})$, so this posterior is its **stationary distribution**. The fraction of time spent in each state converges to the posterior (if the chain is ergodic: all CPT entries nonzero).

**Example** (sprinkler network, query $P(Rain\mid Sprinkler=t, WetGrass=t)$). Start with $Cloudy=t$, $Rain=f$. Resample $Cloudy$ from $P(C\mid s,\neg r)$, then $Rain$ from $P(R\mid c,s,w)$, and so on. Count how often $Rain=t$ occurs.

**Advantages over rejection sampling and likelihood weighting:** no sample is wasted, and the evidence affects *all* variables, including upstream ones. **Disadvantages:** consecutive samples are correlated, and mixing can be slow when there are near-deterministic CPTs.
