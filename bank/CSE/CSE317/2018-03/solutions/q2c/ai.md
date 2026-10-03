---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Laplace (add-k) smoothing: P(x) = (c(x) + k) / (N + k|X|), adding k virtual counts to every outcome so unseen events get non-zero probability. k is a hyperparameter: train with several k values, choose the one with the best accuracy on held-out validation data (or by cross-validation), then test once on the test set."
sources: ["AIMA 4e sec. 20.2.2 (Laplace smoothing), sec. 19.4 (model selection, validation)", "Berkeley CS188 Naive Bayes lecture (tuning k on held-out data)"]
---
**Laplace smoothing.** Maximum-likelihood estimates $P_{ML}(x)=\frac{c(x)}{N}$ give probability 0 to any outcome not seen in training. In naive Bayes, one zero factor makes the whole product 0, which is overfitting to the sample. Laplace smoothing pretends every outcome was seen $k$ extra times:

$$P_{LAP,k}(x)=\frac{c(x)+k}{N+k|X|},\qquad P_{LAP,k}(x\mid y)=\frac{c(x,y)+k}{c(y)+k|X|},$$

where $|X|$ is the number of possible values. $k=1$ is classic add-one smoothing.

- $k=0$: maximum likelihood (overfits).
- Large $k$: estimates are pushed towards uniform (underfits).

*Example:* a coin with 2 heads and 0 tails gives $P_{ML}(T)=0$, but $P_{LAP,1}(T)=\frac{0+1}{2+2}=0.25$.

**Choosing the smoothing parameter $k$.** $k$ is a **hyperparameter**, not learned from the training counts.

1. Split the data into **training**, **held-out (validation)** and **test** sets.
2. For each candidate $k$ (e.g. 0.01, 0.1, 1, 10, 100), estimate the parameters on the training set and measure accuracy (or likelihood) on the held-out set.
3. Choose the $k$ with the best held-out performance (or use $K$-fold cross-validation when data are scarce).
4. Optionally retrain on training + validation with that $k$, and report the final accuracy **once** on the test set.
