---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "In an L-attributed definition an inherited attribute of a body symbol may use only inherited attributes of the head and attributes of symbols to its left. A synthesized attribute of the head is computed from the body attributes after the body is evaluated, so using it would create a cycle (A.s = B.b, B.b depends on B.i = A.s) and cannot be evaluated in a left-to-right pass."
sources: ["KMS Chapter 5 slides 23-40 (S-attributed and L-attributed SDDs)", "Dragon book 2e sec. 5.2.4"]
---
**L-attributed rule (Dragon book sec. 5.2.4).** For a production $A \to X_1 X_2 \cdots X_n$, an inherited attribute $X_i.a$ may be defined only from

- the **inherited** attributes of the head $A$,
- inherited or synthesized attributes of the symbols $X_1, \ldots, X_{i-1}$ to the **left** of $X_i$,
- attributes of $X_i$ itself, provided there are no cycles in the dependency graph.

Why the head's **synthesized** attributes are excluded:

1. A synthesized attribute of the head, $A.s$, is computed **from the attributes of the body** symbols, after all of them (including $X_i$) have been evaluated. $X_i.i$ is needed *before* the subtree of $X_i$ is evaluated. So an edge from $A.s$ to $X_i.i$ goes against the left-to-right, depth-first evaluation order: when $X_i$ is visited, $A.s$ does not exist yet.
2. Worse, it creates a **cycle** in the dependency graph, so no evaluation order exists.

**Example.** $A \to B\ C$ with

$$A.s = B.b \qquad B.i = A.s \qquad B.b = g(B.i)$$

The dependency graph is

$$B.i \to B.b \to A.s \to B.i$$

since $B.b$ needs $B.i$, $A.s$ needs $B.b$, and $B.i$ needs $A.s$: **a cycle**, so the values cannot be computed. If instead $B.i = A.i$ (an inherited attribute of the head, supplied from above), the order $A.i \to B.i \to B.b \to A.s$ exists. The same argument covers $B.i = f(C.c, A.s)$: it uses both a right sibling and a synthesized head attribute, so such an SDD is neither S-attributed nor L-attributed.
