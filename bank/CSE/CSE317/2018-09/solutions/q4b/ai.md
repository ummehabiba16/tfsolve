---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "k-NN: store all training examples; to classify x, find the k training points closest to x (Euclidean or other distance on normalized features) and output the majority class (or the average, for regression). No training phase; the choice of k and distance matter; prediction is slow and suffers in high dimensions."
sources: ["AIMA 4e sec. 19.7.1 (nearest-neighbor models)"]
---
**Nearest-neighbour (k-NN) classifier.** A *nonparametric*, instance-based method: the training set itself is the model.

**Algorithm.**

1. *Training:* store all labeled examples $(\mathbf{x}_j,y_j)$. Nothing else is done.
2. *Prediction* for a query $\mathbf{x}_q$: compute the distance from $\mathbf{x}_q$ to every training example, usually Euclidean $\sqrt{\sum_i(x_{q,i}-x_{j,i})^2}$, or Manhattan, or Hamming for Boolean features. Normalize the features first (for example by z-scores), so that no feature dominates because of its scale. Take the $k$ nearest neighbours, $NN(k,\mathbf{x}_q)$.
3. **Classification:** output the majority class among them (optionally weighted by $1/\text{distance}$). **Regression:** output the mean (or a weighted mean) of their $y$ values.

**Choosing $k$.** $k=1$ follows the data exactly. It has zero training error but overfits noise (the decision boundary is a Voronoi diagram). A larger $k$ smooths the boundary but can underfit. Choose $k$ by cross-validation; an odd $k$ avoids ties in binary problems.

**Properties.**

- *Advantages:* simple, no training time, and arbitrarily complex boundaries. With enough data the 1-NN error is at most twice the Bayes-optimal error.
- *Disadvantages:* prediction is slow ($O(N)$ per query, unless k-d trees or locality-sensitive hashing are used) and needs all the data in memory. It is sensitive to irrelevant features and to scaling, and suffers from the **curse of dimensionality**: in high dimensions all points are far apart, so the "nearest" neighbours are not really near.
