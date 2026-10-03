---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The Markov blanket of X is its parents, its children and its children's other parents; given its Markov blanket, X is conditionally independent of every other node in the network. Example (burglary): MB(Alarm) = {Burglary, Earthquake, JohnCalls, MaryCalls}; MB(Burglary) = {Alarm, Earthquake}."
sources: ["AIMA 3e sec. 14.2.2 (Markov blanket, Fig. 14.4)"]
---
**Definition.** The **Markov blanket** of a node $X$ in a Bayesian network consists of its

- **parents**,
- **children**, and
- **children's other parents** (co-parents, "spouses").

**Property.** A node is **conditionally independent of all other nodes in the network, given its Markov blanket**:

$$P(X\mid \text{all other variables})=P(X\mid MB(X))\propto P(X\mid\text{parents}(X))\prod_{Y\in\text{children}(X)}P(y\mid\text{parents}(Y)).$$

This is the quantity used to resample a variable in **Gibbs sampling**.

**Example** (burglary network: $Burglary\to Alarm\leftarrow Earthquake$, $Alarm\to JohnCalls$, $Alarm\to MaryCalls$).

- $MB(Alarm)=\{Burglary,\ Earthquake\}$ (parents) $\cup\ \{JohnCalls,\ MaryCalls\}$ (children). It has no co-parents.
- $MB(Burglary)=\{Alarm\}$ (child) $\cup\ \{Earthquake\}$ (the alarm's other parent). So given $Alarm$ and $Earthquake$, $Burglary$ is independent of $JohnCalls$ and $MaryCalls$.

Why co-parents are included: given the child $Alarm$, $Burglary$ and $Earthquake$ become dependent (explaining away), so $Earthquake$ must be in $Burglary$'s blanket.
