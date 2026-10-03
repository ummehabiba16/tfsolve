---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A bigger H can fit almost anything, so a consistent hypothesis says less about f: sample complexity grows with ln|H| (or the VC dimension), the risk of overfitting rises, and search is costlier. Occam: prefer the simplest consistent hypothesis."
sources: ["MNM slides Learning-Theory-5-PAC-OCM (Occam's razor)", "MNM slides Learning Theory (PAC) - 2", "AIMA 4e sec. 19.5"]
---
**Expressiveness versus generalization.** A richer (more complex) hypothesis space is more likely to contain the true function $f$, but it has costs:

- **More data needed.** For a consistent learner, $N\ge\frac1\epsilon\big(\ln|H|+\ln\frac1\delta\big)$ (for infinite spaces, $N$ grows with $VC(H)$). With a fixed number of examples, a larger $H$ gives a weaker guarantee on the true error.
- **Overfitting.** A very expressive $H$ (for example all Boolean functions, with $|H|=2^{2^n}$) can fit *any* labeling of the training set, including noise. Being consistent with the data then says almost nothing about $f$.
- **Computation.** Finding a consistent or best hypothesis in a large space is harder, and often intractable.

**Occam's razor.** "Prefer the simplest hypothesis consistent with the data." There are few simple hypotheses, so it is unlikely that a *bad* simple hypothesis fits many examples by chance. If a simple $h$ fits $N$ examples, it is probably approximately correct. Formally, choosing from a small set $H'$ of simple hypotheses gives

$$\text{error}(h)\le\frac1N\Big(\ln|H'|+\ln\frac1\delta\Big),$$

which is small when $|H'|$ is small. A complex hypothesis that fits the same data has no such guarantee.

So **the trade-off** is: $H$ should be expressive enough to contain a good approximation of $f$, and no more complex than that (the bias-variance trade-off, solved with regularization and model selection).
