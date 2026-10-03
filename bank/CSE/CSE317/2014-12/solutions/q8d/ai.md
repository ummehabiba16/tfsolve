---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A singly connected network (polytree) has at most one undirected path between any two nodes; exact inference is linear in the network size (e.g. the burglary network). A multiply connected network has some pair of nodes joined by more than one undirected path (e.g. the sprinkler network Cloudy -> Sprinkler -> WetGrass <- Rain <- Cloudy), and exact inference is NP-hard in general (clustering or join trees are used)."
sources: ["AIMA 3e sec. 14.4.3 (complexity of exact inference)"]
---
**Singly connected network (polytree).** A Bayesian network in which there is **at most one undirected path** between any two nodes. Ignoring edge directions, it has no cycles. Nodes may still have several parents.

*Example:* the **burglary network**: $Burglary\to Alarm\leftarrow Earthquake$, $Alarm\to JohnCalls$, $Alarm\to MaryCalls$. Each pair of nodes is connected by exactly one path.

Exact inference (variable elimination, or message passing) is **linear** in the size of the network, i.e. the total number of CPT entries.

**Multiply connected network.** A network in which **some pair of nodes is connected by two or more undirected paths**: there is a cycle when edge directions are ignored.

*Example:* the **sprinkler network**: $Cloudy\to Sprinkler\to WetGrass$ and $Cloudy\to Rain\to WetGrass$. $Cloudy$ and $WetGrass$ are joined by two paths.

```text
        Cloudy
        /    \
   Sprinkler  Rain
        \    /
       WetGrass
```

Exact inference is **NP-hard** in general (#P-hard for computing probabilities). Clustering (join-tree) algorithms merge nodes to obtain a polytree, or approximate sampling methods are used.
