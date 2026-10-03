---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(1) Unit preference: prefer resolutions in which one clause is a single literal (unit), so resolvents get shorter towards the empty clause. (2) Set of support: every resolution step uses at least one clause from the set of support (initially the negated query), so the search stays goal-directed. Others: input resolution, subsumption (delete clauses more specific than existing ones)."
sources: ["AIMA 3e sec. 9.5.6 (resolution strategies)"]
---
**1. Unit preference.** Prefer resolution steps in which one of the clauses is a **unit clause** (a single literal). Resolving a unit clause $P$ with a clause of length $k$ gives a clause of length $k-1$, which is **shorter** than either parent. Since we want to reach the empty clause (length 0), this guides the search towards it, as in unit propagation. Trying unit resolutions first dramatically speeds up refutation proofs (Wos et al., 1964).

**2. Set of support.** Choose a subset of the clauses, the **set of support** (initially the **negated query**). **Every resolution must use at least one clause from the set of support**, and the resolvent is added to the set of support. If the rest of the KB is satisfiable (as it usually is), this strategy is still complete. It keeps the search **goal-directed**, avoiding endless resolutions among KB facts that are irrelevant to the query, and it makes proofs easy to understand.

(Other strategies: *input resolution*, in which each step combines an input clause with another clause; and *subsumption*, which deletes any clause that is more specific than an existing one, e.g. $P(A)$ subsumes $P(A)\lor Q(B)$.)
