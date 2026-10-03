---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Clustering (join-tree) algorithms combine nodes of a multiply connected network into meganodes so that the network becomes a polytree; exact inference on a polytree is linear, so all posteriors can be computed at once (message passing). The cost moves into the meganodes' CPTs, which are exponential in the number of merged variables (it is still NP-hard in the worst case)."
sources: ["AIMA 3e sec. 14.4.4 (the clustering algorithm)"]
---
**Role of clustering in Bayesian networks.** Exact inference is easy (linear time) in **polytrees** (singly connected networks), but NP-hard in **multiply connected** networks, which contain undirected cycles. Clustering algorithms (join-tree or junction-tree algorithms) make exact inference practical:

1. **Merge** groups of nodes into **cluster nodes (meganodes)** so that the resulting network is a **polytree** (no undirected cycles).
2. A meganode's variable ranges over all combinations of its members' values, and its CPT is computed from the original CPTs.
3. Run a **polytree (message-passing) algorithm** on the cluster network. It computes the posterior of **all** variables at once in linear time in the size of the cluster network. Variable elimination would have to be rerun for each query.

*Example:* in the sprinkler network, merging $Sprinkler$ and $Rain$ into one meganode $Spr{+}Rain$, with 4 values, removes the cycle Cloudy, Sprinkler, WetGrass, Rain.

**Trade-off:** the work moves into the meganodes. Their CPTs are exponential in the number of merged variables, so clustering is efficient only when the clusters (the treewidth) stay small.
