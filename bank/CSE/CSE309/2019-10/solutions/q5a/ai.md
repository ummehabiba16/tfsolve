---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "An SDD is L-attributed if every attribute is synthesized, or inherited such that for a production A -> X1 X2 ... Xn an inherited attribute of Xi depends only on inherited attributes of A, attributes (inherited or synthesized) of X1 ... X(i-1) to its left, and attributes of Xi itself without cycles. Not L-attributed: A -> B C with B.i = f(C.c) (B's inherited attribute depends on its right sibling C)."
sources: ["KMS Chapter 5 slides 30-40 (Well Behaved SDD classes, L-attributed SDD)", "Dragon book 2e sec. 5.2.4"]
---
**Definition (6 marks).** An SDD is **L-attributed** if, for each production $A \to X_1 X_2 \cdots X_n$, every attribute is either

1. **synthesized**, or
2. **inherited**, with the rule computing an inherited attribute $X_i.a$ using only
- inherited attributes of the head $A$;
- inherited or synthesized attributes of the symbols $X_1, X_2, \ldots, X_{i-1}$ located **to the left** of $X_i$;
- inherited or synthesized attributes of $X_i$ itself, provided there are no cycles in the dependency graph formed by the attributes of this $X_i$.

The name comes from the fact that information flows only **from left to right** (and down and up) in the parse tree. So all attributes can be evaluated in one depth-first, left-to-right traversal, and the SDD can be implemented during LL parsing.

Example (L-attributed): $T \to F\,T'$ with $T'.inh = F.val$ (from the left sibling) and $T'_1.inh = T'.inh \times F.val$ in $T' \to * F\, T'_1$.

**An SDD that is not L-attributed (3 marks):**

| Production | Semantic rules |
|:--|:--|
| $A \to B\ C$ | $A.s = B.b$ |
| | $B.i = f(C.c,\ A.s)$ |

- $A.s = B.b$ is fine (a synthesized attribute).
- $B.i$ is an inherited attribute of $B$ that depends on $C.c$, an attribute of the symbol **to the right** of $B$. It also depends on $A.s$, a **synthesized** attribute of the head, which in turn depends on $B$, a cycle risk.

Either of these violates the L-attributed rules: $B.i$ cannot be computed before $B$ is parsed in a left-to-right traversal.
