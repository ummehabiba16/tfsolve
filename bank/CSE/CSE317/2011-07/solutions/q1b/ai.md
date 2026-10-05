---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Markov blanket: parents, children and children's other parents; given it, a node is independent of the rest of the network. Enumeration is redundant because it evaluates the expression tree depth-first and recomputes the same sub-expressions (e.g. P(j|a) P(m|a) for every value of e in P(B | j, m)); variable elimination stores them as factors."
sources: ["AIMA 3e sec. 14.2.2 (Markov blanket), 14.4.1-14.4.2 (enumeration, variable elimination, Fig. 14.8)"]
---
**Markov blanket** (4). The Markov blanket of a node $X$ consists of its **parents, children, and children's other parents**. $X$ is conditionally independent of all other nodes in the network given its Markov blanket:

$$P(X\mid\text{rest})=P(X\mid MB(X)).$$

*Example:* in the burglary network, $MB(Alarm)=\{Burglary,Earthquake,JohnCalls,MaryCalls\}$.

**Why exact inference by enumeration is computationally redundant** (3). Enumeration evaluates

$$P(B\mid j,m)=\alpha\,P(B)\sum_eP(e)\sum_aP(a\mid B,e)\,P(j\mid a)\,P(m\mid a)$$

by a depth-first walk over the expression tree. The product $P(j\mid a)P(m\mid a)$ (for $a$ and for $\neg a$) does not depend on $e$, yet it is **recomputed for every value of $e$** (and of $B$). In larger networks the same sub-expressions are evaluated an exponential number of times: the time is $O(n\,d^{\,n})$ even when the space is linear.

**Variable elimination** removes this redundancy. It evaluates the expression right to left, stores the intermediate results as **factors** (e.g. $f_{JM}(A)$), reuses them, and drops irrelevant variables. On polytrees it is linear in the network size.
