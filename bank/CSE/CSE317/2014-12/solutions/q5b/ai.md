---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) Markov blanket of X: its parents, children and children's other parents; X is conditionally independent of all other nodes given its Markov blanket (used in Gibbs sampling). (ii) Clustering (join-tree) algorithms: merge nodes of a multiply connected network into cluster meganodes so that the result is a polytree, then run linear-time exact inference (message passing) on it; the cost moves into the size of the cluster CPTs (exponential in the cluster size)."
sources: ["AIMA 3e sec. 14.2.2 (Markov blanket), sec. 14.4.4 (clustering algorithms)"]
---
**(i) Markov blanket** (4). The Markov blanket of a node $X$ is its **parents**, its **children** and its **children's other parents**. Given its Markov blanket, $X$ is conditionally independent of every other variable in the network:

$$P(X\mid\text{everything else})=P(X\mid MB(X))\propto P(X\mid Pa(X))\prod_{Y\in Ch(X)}P(Y\mid Pa(Y)).$$

*Example:* in the burglary network, $MB(Burglary)=\{Alarm, Earthquake\}$. Gibbs sampling resamples each variable from this distribution.

**(ii) Clustering** (3). *Clustering (join-tree) algorithms* make exact inference efficient in **multiply connected** networks. They **merge** individual nodes into **cluster nodes (meganodes)** so that the resulting network is a **polytree** (singly connected).

For example, in the sprinkler network ($Cloudy\to Sprinkler$, $Cloudy\to Rain$, $Sprinkler\to WetGrass\leftarrow Rain$), merging $Sprinkler$ and $Rain$ into one node $Spr{+}Rain$ (4 values) gives a polytree. The meganode's CPT is the joint over the merged variables. Linear-time polytree message passing (belief propagation) then answers all posterior queries at once. The cost: CPT sizes grow exponentially with the number of variables in a cluster, so the method is fast only if the clusters stay small. In the worst case it is still exponential (NP-hard).

(In machine learning, "clustering" means unsupervised grouping of data points by similarity, e.g. k-means.)
