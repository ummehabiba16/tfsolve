---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "No. Arc consistency only removes values without support on each single arc; it does not consider several constraints together. Example: 3 mutually adjacent regions (a triangle), each with domain {red, green}: every arc is consistent (each value has a different value in the neighbour) and no domain is empty, but there is no solution. If AC leaves every domain with exactly one value, those values do form a solution; with several values left, search is still needed."
sources: ["AIMA 3e sec. 6.2.2-6.2.3 (arc consistency, path consistency)"]
---
**No, a solution is not guaranteed.** Arc consistency (AC-3) checks constraints **one arc (two variables) at a time**: each value of $X_i$ must have *some* support in $X_j$. A set of locally consistent pairs can still be globally inconsistent, because no single assignment satisfies all the constraints together.

**Counter-example.** Three regions $A$, $B$, $C$, all adjacent to each other (a triangle), each with the domain {red, green}, and constraints $A\neq B$, $B\neq C$, $A\neq C$.

- Every arc is consistent. For example, $A=$ red has the support $B=$ green, and $A=$ green has the support $B=$ red. AC-3 deletes nothing, and no domain is empty, with 2 values in each domain.
- But three mutually adjacent regions need **three** colours, so **there is no solution**.

(Another example: $X\neq Y$, $Y\neq Z$, $X=Z$, each over $\{0,1\}$, gives a solution, while $X\neq Y$, $Y\neq Z$, $X\neq Z$ over $\{0,1\}$ gives none, yet both are arc-consistent.)

**What arc consistency does tell us.**

- If some domain becomes **empty**, there is no solution.
- If every domain is reduced to **exactly one** value, that assignment is a solution.
- Otherwise (as in this question: several values remain, none empty), the problem may or may not have a solution. **Backtracking search is still needed**, possibly combined with stronger consistency (path consistency, $k$-consistency) or with maintaining arc consistency (MAC) during search.
