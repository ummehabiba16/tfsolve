---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Ockham's razor: prefer the simplest hypothesis consistent with the data. PAC bound: a hypothesis with error > eps agrees with one example with probability <= 1-eps, so with N examples <= (1-eps)^N; by the union bound, P(some bad h is consistent) <= |H|(1-eps)^N <= |H| e^{-eps N}; setting this <= delta gives N >= (1/eps)(ln|H| + ln(1/delta))."
sources: ["AIMA 3e sec. 18.5 (computational learning theory)", "Shalev-Shwartz & Ben-David, Understanding Machine Learning, Cor. 2.3", "MNM slides Learning Theory (PAC) - 2"]
---
**Ockham's razor.** "Entities should not be multiplied beyond necessity": **prefer the simplest hypothesis consistent with the data.** A simple hypothesis that fits the data is unlikely to do so by coincidence, so it is more likely to generalize.

**PAC sample complexity.** $H$ is a finite hypothesis space containing the true function $f$ (realizable); examples are i.i.d. from a fixed distribution (stationary); labels are noiseless. $\text{error}(h)=P(h(x)\neq f(x))$, and $h$ is *bad* if $\text{error}(h)>\epsilon$.

1. A bad $h_b$ agrees with one random example with probability $\le1-\epsilon$.
2. With $N$ independent examples: $P(h_b\text{ consistent with all }N)\le(1-\epsilon)^N$.
3. Union bound over $H_{bad}\subseteq H$:

$$P(H_{bad}\text{ contains a consistent hypothesis})\le|H_{bad}|(1-\epsilon)^N\le|H|(1-\epsilon)^N.$$

4. With $1-\epsilon\le e^{-\epsilon}$: $|H|(1-\epsilon)^N\le|H|e^{-\epsilon N}$. Require this to be $\le\delta$:

$$|H|e^{-\epsilon N}\le\delta\iff N\ge\frac1\epsilon\Big(\ln|H|+\ln\frac1\delta\Big).$$

So with this many examples, with probability at least $1-\delta$, every hypothesis consistent with the data has error at most $\epsilon$:

$$\boxed{N\ge\frac{1}{\epsilon}\Big(\ln|H|+\ln\frac{1}{\delta}\Big)}$$

**Link to Ockham's razor.** The bound grows with $\ln|H|$. A learner that searches a small space of simple hypotheses needs fewer examples, or gets a tighter error guarantee for the same $N$, than one searching all hypotheses (all Boolean functions: $\ln|H|=2^n\ln2$).
