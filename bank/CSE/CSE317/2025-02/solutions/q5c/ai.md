---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A tree grown until it fits every example overfits noise and irrelevant attributes; pruning removes splits that are not statistically significant (e.g. chi-squared test or validation error), giving a smaller tree that generalizes better."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree", "AIMA 4e sec. 19.3.4 (generalization and overfitting, decision-tree pruning)"]
---
**Why prune.**

- **Overfitting:** the basic algorithm keeps splitting until every leaf is pure. With noisy data or irrelevant attributes it then builds deep branches that fit accidental patterns (for example "students born on Tuesday get A"). These branches have zero training error but high error on new examples.
- **Small leaves are unreliable:** splits near the bottom are based on very few examples, so their information gain is not statistically meaningful.
- **Pruning** removes such nodes and replaces them with a leaf (the majority class). In AIMA's $\chi^2$ pruning, a node whose split is not significantly better than chance (for example at the 5% level) is pruned. Alternatively, prune bottom-up while the error on a validation set does not increase (reduced-error pruning).
- **Result:** a smaller, simpler tree (Ockham's razor) that is easier to interpret, faster, and **generalizes better**, at the cost of a few training errors.
