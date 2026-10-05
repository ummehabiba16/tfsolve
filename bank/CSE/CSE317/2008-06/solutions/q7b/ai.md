---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "An ensemble combines the predictions of many hypotheses (by voting or weighting). If the members are reasonably accurate and their errors are independent, the majority is wrong far less often than any single member (e.g. 5 classifiers with 10% error each give about 1% majority error); ensembles also enlarge the hypothesis space (e.g. a combination of linear separators forms non-linear regions) and reduce variance (bagging) or bias (boosting)."
sources: ["AIMA 3e sec. 18.10 (ensemble learning, boosting)"]
---
**Ensemble learning** selects a whole collection (ensemble) of hypotheses from the hypothesis space and **combines** their predictions, by majority vote or weighted vote, instead of trusting a single hypothesis.

**Why it outperforms a single hypothesis.**

1. **Errors cancel out (variance reduction).** Suppose we have $M=5$ hypotheses, each with error rate $p=0.1$, whose errors are independent. The majority vote is wrong only if at least 3 of the 5 are wrong:

$$P(\text{majority wrong})=\sum_{k=3}^{5}\binom5kp^k(1-p)^{5-k}\approx0.0086<1\%.$$

That is much better than the 10% of any single member. In practice errors are correlated, but the improvement is still substantial whenever the members disagree on different examples.

2. **A more expressive hypothesis space (bias reduction).** An ensemble can represent functions that no single member can. For example, a vote of three linear separators can carve out a triangular (non-linear) region, while keeping each member simple.
3. **More robustness and stability:** less sensitive to noise and to the particular training sample (bagging, random forests), or concentrating on hard examples (boosting, e.g. AdaBoost, which turns weak learners into a strong one).

So combining many diverse, reasonably accurate hypotheses reduces variance and/or bias, and generalizes better than choosing the single best hypothesis.
