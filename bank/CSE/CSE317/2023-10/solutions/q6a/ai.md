---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Overfitting memorizes noise and accidental patterns: low training error, high test error. In decision trees: pruning (chi-squared or reduced-error), early stopping (max depth, min examples per leaf, min gain), validation or cross-validation, ensembles (random forest)."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree", "AIMA 4e sec. 19.3.4 and 19.4"]
---
**Why overfitting is bad.** An overfitted model learns the training data too closely, including noise, errors and accidental regularities that do not hold in the real distribution.

- Training error is very low (often zero), but the error on new, unseen examples is high, so the model **does not generalize**. Generalization is the purpose of learning.
- The model is usually more complex than needed: harder to understand, slower, and it needs more data to estimate reliably.
- Accuracy measured on the training set is then misleading.

**Preventing overfitting in decision-tree learning.**

1. **Pruning** (post-pruning): grow the full tree, then replace sub-trees by leaves. In *$\chi^2$ pruning* (AIMA), remove a split whose class distribution is not significantly different from chance. In *reduced-error pruning*, prune while accuracy on a validation set does not drop.
2. **Early stopping** (pre-pruning): stop splitting when the information gain is below a threshold, the node has too few examples, or a maximum depth is reached.
3. **Validation / cross-validation** to choose the tree size (depth) that gives the lowest validation error.
4. More training data, removing irrelevant attributes, and **ensembles** (bagging, random forests) that average many trees.
