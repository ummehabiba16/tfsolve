---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The Markov blanket of a node is its parents, children and children's other parents; given it, the node is conditionally independent of all other nodes. Example (burglary network): MB(Burglary) = {Alarm, Earthquake}; MB(Alarm) = {Burglary, Earthquake, JohnCalls, MaryCalls}."
sources: ["AIMA 3e sec. 14.2.2, Fig. 14.4(b)"]
---
**Markov blanket.** For a node $X$ in a Bayesian network, the Markov blanket $MB(X)$ consists of:

- the **parents** of $X$,
- the **children** of $X$,
- the **other parents of $X$'s children** (co-parents).

**Property.** $X$ is **conditionally independent of every other node** in the network given its Markov blanket:

$$P(X\mid\text{all other nodes})=P(X\mid MB(X))\propto P(X\mid Pa(X))\prod_{Y\in Ch(X)}P(Y\mid Pa(Y)).$$

The Markov blanket "shields" $X$ from the rest of the network. It is the basis of Gibbs sampling.

**Example (burglary network).** $Burglary\to Alarm\leftarrow Earthquake$, $Alarm\to JohnCalls$, $Alarm\to MaryCalls$.

- $MB(Burglary)=\{Alarm\ (\text{child}),\ Earthquake\ (\text{co-parent})\}$. Given $Alarm$ and $Earthquake$, $Burglary$ is independent of $JohnCalls$ and $MaryCalls$.
- $MB(Alarm)=\{Burglary,\ Earthquake\ (\text{parents}),\ JohnCalls,\ MaryCalls\ (\text{children})\}$.
- $MB(JohnCalls)=\{Alarm\}$.
