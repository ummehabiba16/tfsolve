---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Initial centroids 7, 8. Iteration 1: {1,2,3,4,7} and {8,10,12}, new centroids 3.4 and 10. Iteration 2: {1,2,3,4} and {7,8,10,12}, new centroids 2.5 and 9.25. Iteration 3: no change, so converged: clusters {1,2,3,4} (centroid 2.5) and {7,8,10,12} (centroid 9.25)."
sources: ["AIMA 4e sec. 20.3.1 (k-means clustering)"]
---
**K-means** (K = 2, distance $|a-b|$): assign each point to its nearest centroid, recompute each centroid as the mean of its cluster, and repeat until the assignment no longer changes.

**Iteration 1.** Centroids $c_1=7$, $c_2=8$.

| Point | $\lvert p-7\rvert$ | $\lvert p-8\rvert$ | Cluster |
|:-:|:-:|:-:|:-:|
| 1 | 6 | 7 | 1 |
| 2 | 5 | 6 | 1 |
| 3 | 4 | 5 | 1 |
| 4 | 3 | 4 | 1 |
| 7 | 0 | 1 | 1 |
| 8 | 1 | 0 | 2 |
| 10 | 3 | 2 | 2 |
| 12 | 5 | 4 | 2 |

Clusters: $\{1,2,3,4,7\}$ and $\{8,10,12\}$. New centroids: $c_1=\frac{1+2+3+4+7}{5}=\frac{17}{5}=\mathbf{3.4}$ and $c_2=\frac{8+10+12}{3}=\mathbf{10}$.

**Iteration 2.** Centroids $3.4$ and $10$. Point 7: $|7-3.4|=3.6$ and $|7-10|=3$, so it moves to cluster 2. The other points stay.

Clusters: $\{1,2,3,4\}$ and $\{7,8,10,12\}$. New centroids: $c_1=\frac{10}{4}=\mathbf{2.5}$ and $c_2=\frac{37}{4}=\mathbf{9.25}$.

**Iteration 3.** Centroids $2.5$ and $9.25$. Points 1-4 are nearer 2.5; points 7, 8, 10, 12 are nearer 9.25 (for 7: $4.5$ against $2.25$). The assignment is unchanged, so the algorithm has **converged**.

| Iteration | Cluster 1 | Cluster 2 | Centroids after |
|:-:|:--|:--|:-:|
| 1 | {1, 2, 3, 4, 7} | {8, 10, 12} | 3.4, 10 |
| 2 | {1, 2, 3, 4} | {7, 8, 10, 12} | 2.5, 9.25 |
| 3 | {1, 2, 3, 4} | {7, 8, 10, 12} | 2.5, 9.25 (no change) |

**Final clusters:** $\{1,2,3,4\}$ with centroid 2.5, and $\{7,8,10,12\}$ with centroid 9.25.
