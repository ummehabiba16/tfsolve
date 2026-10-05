---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "If every node has a distinct f, each IDA* iteration raises the bound to the next f value and so adds only one new node. Iteration i expands about i nodes, so IDA* generates about 1 + 2 + ... + K = K(K+1)/2 = O(K^2) nodes, against K for A*."
sources: ["AIMA 3e sec. 3.5.3 (IDA*) and Exercise 3.29"]
---
IDA\* repeats depth-first searches with an $f$-cost bound. After each iteration, the bound becomes the **smallest $f$ that exceeded** the previous bound.

If every node has a **distinct** $f$-value, then each new bound admits **exactly one** more node than the previous iteration. Each iteration re-generates everything the previous one did, plus one new node:

- iteration 1 generates about 1 node,
- iteration 2 about 2 nodes,
- ...
- iteration $K$ about $K$ nodes, by which point it has covered all the nodes A\* would generate.

The total is

$$1+2+\dots+K=\frac{K(K+1)}{2}=O(K^2).$$

So IDA\* generates **about $K^2/2$ nodes**, against $K$ for A\*. This is the main weakness of IDA\* when costs are real-valued. (The remedy is to increase the bound by a fixed $\epsilon$ each time, which gives an $\epsilon$-admissible search.)
