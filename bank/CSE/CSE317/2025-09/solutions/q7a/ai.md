---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "P(some bad h is consistent with N examples) <= |H|(1 - eps)^N <= |H| e^{-eps N} <= delta, which gives N >= (1/eps)(ln(1/delta) + ln|H|)."
sources: ["MNM slides Learning Theory (PAC) - 2 (assumptions, H_bad, sample complexity)", "AIMA 4e sec. 19.5", "Shalev-Shwartz & Ben-David, Understanding Machine Learning, Cor. 2.3"]
---
**Notation.** $f$ is the true function and $H$ a finite hypothesis space. For a hypothesis $h$,

$$\text{error}(h)=P_{(x,y)\sim P(X,Y)}\big(h(x)\neq y\big)$$

(expected 0/1 loss). $h$ is *approximately correct* if $\text{error}(h)\le\epsilon$. Let

$$H_{\text{bad}}=\{h\in H:\ \text{error}(h)>\epsilon\}$$

be the hypotheses outside the $\epsilon$-ball around $f$. We look for $N$ such that, with probability at least $1-\delta$, no hypothesis in $H_{\text{bad}}$ is consistent with all $N$ training examples. Then every consistent hypothesis is approximately correct.

**Role of the assumptions.**

- *Stationarity:* the training and future examples are i.i.d. from the same fixed $P(X,Y)$. This lets us multiply probabilities over the examples and use the same error rate for training and test.
- *Noiseless:* $y=f(x)$ is deterministic, so a "wrong" hypothesis is wrong on a fixed set of inputs, of probability $\text{error}(h)$.
- *Realizability:* $f\in H$, so at least one consistent hypothesis exists (the learner can always return one).

**Derivation.**

1. Take any $h_b\in H_{\text{bad}}$. It errs on a random example with probability $>\epsilon$, so

$$P(h_b\text{ agrees with one example})\le 1-\epsilon.$$

2. The $N$ examples are independent (stationarity), so

$$P(h_b\text{ agrees with all }N\text{ examples})\le(1-\epsilon)^N.$$

3. Union bound over all bad hypotheses:

$$P(H_{\text{bad}}\text{ contains a consistent }h)\le|H_{\text{bad}}|(1-\epsilon)^N\le|H|(1-\epsilon)^N.$$

4. Use $1-\epsilon\le e^{-\epsilon}$ and require the bound to be at most $\delta$:

$$|H|\,e^{-\epsilon N}\le\delta\iff \epsilon N\ge\ln|H|+\ln\frac{1}{\delta}.$$

**Result.**

$$\boxed{N\ \ge\ \frac{1}{\epsilon}\left(\ln\frac{1}{\delta}+\ln|H|\right)}$$

With this many examples, with probability at least $1-\delta$, **every** hypothesis consistent with the training set has error at most $\epsilon$ (it is PAC).

**Remarks.** $N$ grows only logarithmically in $|H|$ and $1/\delta$, and linearly in $1/\epsilon$. For example, for all Boolean functions of $n$ attributes, $|H|=2^{2^n}$ and $N\ge\frac{1}{\epsilon}(\ln\frac1\delta+2^n\ln2)$. That is exponential in $n$, so the hypothesis space must be restricted (or prior knowledge used).
