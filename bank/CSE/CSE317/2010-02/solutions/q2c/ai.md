---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Pre-pruning (early stopping): stop growing a branch when the split is not worthwhile (gain below a threshold, too few examples, max depth, chi-squared test not significant). Post-pruning: grow the full tree, then replace sub-trees by leaves bottom-up if this does not increase validation error (reduced-error) or if the split is not statistically significant (chi-squared pruning), or use rule post-pruning."
sources: ["AIMA 3e sec. 18.3.5 (decision-tree pruning, early stopping)", "Mitchell, Machine Learning, sec. 3.7"]
---
**Pre-pruning (early stopping).** Stop growing a branch during construction when splitting further does not seem worthwhile:

- the information gain of the best attribute is below a threshold;
- the node has fewer than a minimum number of examples;
- a maximum depth is reached;
- a $\chi^2$ significance test says the split is not significantly better than chance.

The node becomes a leaf labeled with the majority class. It is cheap, but it can stop too early: no single attribute may look useful even when a combination is (e.g. XOR).

**Post-pruning.** Grow the **full** tree first, then remove parts bottom-up:

- **Reduced-error pruning:** replace a sub-tree by a leaf if this does not increase the error on a validation set;
- **$\chi^2$ pruning:** remove a test node whose children are all leaves if its split is not statistically significant;
- **Rule post-pruning:** convert the tree into rules and drop conditions that do not hurt accuracy.

It is more reliable, because it judges each split after seeing the full sub-tree, at the cost of growing the whole tree. Both methods reduce **overfitting** and give smaller trees that generalize better.
