---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A polyhedral (polytope) region is an intersection of half-spaces bounded by hyperplanes (convex). A 2-layer network of threshold units (one hidden layer + output) forms only convex regions (the output ANDs half-spaces), so it cannot classify an arbitrary union of polyhedral regions, e.g. two separate squares; a 3-layer network (half-planes, then AND per polytope, then OR) can. (With sigmoid units and enough hidden nodes, one hidden layer can approximate any region, by the universal approximation theorem.)"
sources: ["Lippmann 1987, An introduction to computing with neural nets (decision regions by number of layers)", "AIMA 3e sec. 18.7.3-18.7.4 (multilayer networks, expressiveness)"]
---
**Polyhedral region.** A region of input space bounded by hyperplanes. It is the **intersection of a finite number of half-spaces** $\{\mathbf{x}:\mathbf{w}_i\cdot\mathbf{x}\ge b_i\}$, which is convex. Unions of polyhedral regions can be non-convex or disconnected.

**What each architecture can represent** (hard-threshold units):

| Network | Decision region |
|:--|:--|
| 1 layer (a single perceptron) | a half-space (one hyperplane) |
| 2 layers (1 hidden layer + output) | **convex** (polyhedral) regions: the hidden units are half-spaces, and the output unit ANDs them (threshold = number of hidden units) |
| 3 layers (2 hidden layers + output) | **arbitrary unions** of polyhedral regions: 1st layer half-spaces, 2nd layer ANDs (one unit per polytope), output ORs |

**Answer: no**, a 2-layer threshold network cannot classify every union of polyhedral regions.

*Example:* let the positive class be the union of two separate squares, $[0,1]^2\cup[3,4]^2$. One hidden layer gives a set of half-planes, and the output unit computes a threshold of their weighted count, which yields a single convex region (or simple combinations). Separating two disjoint squares from everything around and between them needs an AND per square and then an OR. That requires a second hidden layer:

```text
x1, x2 --> 8 half-plane units --> 2 AND units (one per square) --> 1 OR unit (output)
```

*Note:* with continuous (sigmoid) units and enough hidden units, even one hidden layer can **approximate** any decision region arbitrarily well (Cybenko's universal approximation). The "convex only" limitation holds for threshold units with a single AND-type output.
