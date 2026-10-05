---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Polytree (singly connected): at most one undirected path between any two nodes; multiply connected: two or more such paths (a cycle when directions are ignored). On a polytree, eliminating each variable after the subtrees hanging off it never creates a factor larger than that node's own CPT (removing a node disconnects its neighbours, so no new dependencies are created); there are n elimination steps, each costing O(size of a CPT), so the total time is O(sum of CPT sizes), linear in the size of the network."
sources: ["AIMA 3e sec. 14.4.3 (complexity of exact inference) and Exercise 14.17"]
---
**Definitions** (4).

- **Singly connected network (polytree):** a Bayesian network with **at most one undirected path** between any two nodes. With directions ignored, the graph is a tree or forest, although a node may have several parents. Example: the burglary network.
- **Multiply connected network:** at least one pair of nodes is joined by **two or more** undirected paths, so there is an undirected cycle. Example: the sprinkler network, where $Cloudy\to Sprinkler\to WetGrass$ and $Cloudy\to Rain\to WetGrass$.

**Claim** (6). On a polytree, variable elimination runs in time **linear in the size of the network** (the total number of CPT entries), for any elimination order consistent with the structure: each variable is eliminated only after all the subtrees hanging off it, other than the one leading to the query, have been eliminated.

**Proof sketch.**

1. *Key property of polytrees:* removing a node $X$ splits the polytree into separate components, one for each parent and one for each child of $X$, with no other connections between them.
2. Eliminate variables from the outside in, towards the query. When a variable $Z$ is eliminated, every component hanging off $Z$ (except the one towards the query) has already been summed out. So each of them has been reduced to a factor mentioning only $Z$ and, at most, the variables of $Z$'s own family. By property 1, those components share no other variables.
3. The factors that mention $Z$ are therefore its CPT $P(Z\mid Pa(Z))$ (or that of the child linking it towards the query) and factors over $Z$ alone (or over $Z$ and its family). Their product, summed over $Z$, is a factor over variables of **one family only**. Its size is at most the size of an existing CPT. **No factor larger than a CPT is ever created**: there is no "fill-in", because there is no second path to create new dependencies.
4. Each elimination step therefore costs $O(\text{size of a CPT})$, and each variable is eliminated once. So the total time is

$$O\Big(\sum_i|CPT_i|\Big)=O(n\cdot d^{\,k+1}),$$

where $k$ is the maximum number of parents, which is linear in the size of the network.

By contrast, in a multiply connected network, eliminating a variable on a cycle creates a factor that links variables that were not linked before. Factor sizes can then grow exponentially, and exact inference is NP-hard in general.
