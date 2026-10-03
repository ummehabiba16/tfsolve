---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Assumptions: the network is a DAG; each node has a CPT P(X | Parents(X)); each node is conditionally independent of its non-descendants given its parents (local Markov property), which gives the factorization P(x_1..x_n) = prod_i P(x_i | parents(X_i)); nodes are ordered consistently with this. Markov blanket = parents, children and children's other parents; given it, a node is independent of all others."
sources: ["AIMA 3e sec. 14.1-14.2 (semantics of Bayesian networks, Markov blanket)"]
---
**Underlying assumptions of a Bayesian network** (4).

1. **Structure:** a **directed acyclic graph** whose nodes are random variables and whose arcs represent direct influences (parent to child).
2. **Local parametrization:** each node $X_i$ has a conditional probability distribution $P(X_i\mid Parents(X_i))$, a CPT for discrete variables.
3. **Conditional independence (local Markov property):** **each node is conditionally independent of its non-descendants, given its parents.** This is the key assumption. It gives the chain-rule factorization of the full joint distribution:

$$P(x_1,\dots,x_n)=\prod_{i=1}^{n}P(x_i\mid parents(X_i)).$$

(Equivalently, ordering the nodes so that parents come before children, $P(X_i\mid X_{i-1},\dots,X_1)=P(X_i\mid Parents(X_i))$.)

**Markov blanket of a node** (3). The **parents**, **children** and **children's other parents** of the node. A node is **conditionally independent of all other nodes in the network given its Markov blanket.** For example, in the burglary network, $MB(Burglary)=\{Alarm, Earthquake\}$.
