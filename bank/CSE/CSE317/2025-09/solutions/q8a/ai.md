---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Choose (a), the straight line (Ockham's razor: simpler hypothesis, smaller effective H, tighter PAC bound, less overfitting). For neural nets and LLMs, parameter-count simplicity does not explain generalization (overparameterization, double descent); a refined Occam (implicit bias of SGD, low norm or flat minima, regularization, PAC-Bayes/MDL) still applies."
sources: ["MNM slides Learning Theory (PAC) - 2 (implications, Ockham's razor)", "MNM slides Learning-Theory-5-PAC-OCM (Occam's razor)", "AIMA 4e sec. 19.2 and 19.5"]
---
**Which hypothesis?** Both curves pass through every training point, so both have zero training error. Choose **(a), the straight line**, by **Ockham's razor**: among hypotheses consistent with the data, prefer the simplest.

- *Learning-theory reason:* a line comes from a small hypothesis space (2 parameters, VC dimension 2 in one dimension). A high-degree, wiggly curve like (b) comes from a much larger space. The PAC bound $N\ge\frac1\epsilon(\ln\frac1\delta+\ln|H|)$, or its VC version, needs far fewer examples for the small space. With the same data, the simple consistent hypothesis has a much smaller guaranteed generalization error.
- *Overfitting:* (b) bends to pass through every point, so it fits the noise. Between and beyond the points it swings wildly (look at the right end), so it will predict new $x$ badly. (a) captures the underlying trend.
- A simple hypothesis that fits many points is unlikely to do so by coincidence. A complex one can fit almost any data, so fitting this data is weak evidence.

**Does the same reasoning apply to neural networks or LLMs?** Only partly.

- **Not in its naive form.** Modern networks and LLMs have far more parameters than training examples. Their hypothesis spaces (VC dimension) are huge, so the classical bounds are vacuous, and counting parameters predicts that they should overfit. In practice, larger models often generalize *better* ("double descent", benign overfitting), and LLM test loss keeps falling as models grow (scaling laws).
- **But a refined Occam's razor still holds**, with "simplicity" measured differently. SGD has an *implicit bias* towards simple solutions: low weight norm, smooth functions, flat minima.
- Explicit regularization (weight decay, dropout, early stopping, data augmentation) prefers simpler functions among those that fit.
- Generalization bounds based on norms, margins, compression, PAC-Bayes or MDL (description length) depend on how simple the *learned* function is, not on the parameter count.

**Conclusion.** For this regression problem, choose **(a)**. For NNs and LLMs, the principle "prefer the simplest explanation of the data" still applies, but simplicity is not the number of parameters. Huge models generalize because training and regularization pick simple functions inside a very large space.
