---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "S-attributed example: the desk-calculator SDD (only synthesized val). L-attributed example: T -> F T' with T'.inh = F.val (inherited from the left sibling). Every S-attributed SDD is L-attributed because it has no inherited attributes, so the L-attributed conditions hold vacuously; the L-attributed example is not S-attributed because it uses an inherited attribute."
sources: ["KMS Chapter 5 slides 23-40 (S-attributed and L-attributed SDDs)", "Dragon book 2e sec. 5.2.3-5.2.4"]
---
**S-attributed definition** (all attributes synthesized, Dragon book sec. 5.2.3). Example, the desk-calculator SDD:

| Production | Semantic rule |
|:--|:--|
| $E \to E_1 + T$ | $E.val = E_1.val + T.val$ |
| $E \to T$ | $E.val = T.val$ |
| $T \to T_1 * F$ | $T.val = T_1.val \times F.val$ |
| $T \to F$ | $T.val = F.val$ |
| $F \to \textbf{digit}$ | $F.val = \textbf{digit}.lexval$ |

Every attribute is computed from attributes of the **children** only.

**L-attributed definition** (sec. 5.2.4): each attribute is synthesized, or inherited such that for $A \to X_1 \cdots X_n$ the inherited attribute of $X_i$ depends only on the inherited attributes of $A$ and on attributes of $X_1, \ldots, X_{i-1}$ (symbols to its left). Example (the left-recursion-free expression SDD):

| Production | Semantic rules |
|:--|:--|
| $T \to F\ T'$ | $T'.inh = F.val$ |
| | $T.val = T'.syn$ |
| $T' \to * F\ T_1'$ | $T_1'.inh = T'.inh \times F.val$ |
| | $T'.syn = T_1'.syn$ |
| $T' \to \epsilon$ | $T'.syn = T'.inh$ |
| $F \to \textbf{digit}$ | $F.val = \textbf{digit}.lexval$ |

$T'.inh$ is an **inherited** attribute defined from $F.val$, the attribute of the **left sibling** $F$, which is allowed in an L-attributed SDD.

**Every S-attributed definition is L-attributed.** The L-attributed rule restricts only the *inherited* attributes. An S-attributed definition has **no inherited attributes**, so the condition is satisfied trivially; its synthesized attributes are computed from the children, which is exactly what a left-to-right depth-first (post-order) evaluation does. So the S-attributed class is contained in the L-attributed class.

**Not every L-attributed definition is S-attributed.** The second example is L-attributed, but it contains the inherited attributes $T'.inh$ and $T_1'.inh$, and an S-attributed definition may not have inherited attributes. Such inherited attributes cannot be evaluated by a purely bottom-up pass: $T'.inh$ must be known before the subtree of $T'$ is processed. Hence L-attributed $\supsetneq$ S-attributed.
