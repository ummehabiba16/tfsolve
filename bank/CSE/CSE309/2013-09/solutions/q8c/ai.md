---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "B.i = f(C.c, A.s) is an inherited attribute of B that depends on C.c (a right sibling) and on A.s (a synthesized attribute of the head), neither of which an L-attributed SDD allows; it is not S-attributed because it has an inherited attribute at all. Moreover A.s = B.b and B.i = f(C.c, A.s) can create the cycle B.i -> B.b -> A.s -> B.i."
sources: ["KMS Chapter 5 slides 23-40 (S-attributed and L-attributed SDDs)", "Dragon book 2e sec. 5.2.3-5.2.4"]
---
Production $A \to B\ C$ with the rules $A.s = B.b$ (synthesized, defined from the child $B$) and $B.i = f(C.c, A.s)$ ($B.i$ is an **inherited** attribute of $B$). Here $s$ is synthesized and $i$ inherited.

**Not S-attributed.** An S-attributed definition may contain **only synthesized** attributes (Dragon book sec. 5.2.3). This SDD defines the inherited attribute $B.i$, so it is not S-attributed.

**Not L-attributed.** L-attributed means every inherited attribute of $X_i$ in $A \to X_1 \cdots X_n$ depends only on (a) inherited attributes of the head $A$, (b) attributes of $X_1, \ldots, X_{i-1}$, i.e. **symbols to the left** of $X_i$, and (c) attributes of $X_i$ itself without cycles (sec. 5.2.4). For $B.i$ ($B$ is the leftmost symbol, so there is nothing to its left) the rule uses:

- $C.c$: an attribute of $C$, a **right sibling** of $B$; this violates (b);
- $A.s$: a **synthesized** attribute of the head; allowed are only the *inherited* attributes of the head; this violates (a).

**Evaluation order problem (cycle).** $A.s$ is computed from $B.b$, and $B.i$ from $A.s$; if, as is usual, $B.b$ depends on $B.i$ (inherited values are the input for the synthesized ones of the same symbol), the dependency graph has the cycle

$$B.i \to B.b \to A.s \to B.i$$

so no evaluation order exists at all. Even without the cycle, a single left-to-right pass cannot compute $B.i$ when it visits $B$, because $C.c$ and $A.s$ are not yet known.

Hence such an SDD can be **neither S-attributed nor L-attributed**.
