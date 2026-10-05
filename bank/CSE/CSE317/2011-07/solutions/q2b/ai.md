---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Sound: every resolvent is true in every model of its parent clauses, so only entailed sentences are derived. Complete (refutation-complete): if KB and not alpha is unsatisfiable, resolution derives the empty clause (ground resolution theorem plus the lifting lemma). Set of support: every resolution uses a clause from the set of support (initially the negated query), keeping the proof goal-directed. Unit preference: prefer resolutions with unit clauses, which produce shorter clauses on the way to the empty clause."
sources: ["AIMA 3e sec. 7.5.2 and 9.5.4-9.5.6 (completeness, resolution strategies)"]
---
**Sound and complete** (4).

- **Sound:** take a resolution step with clauses $l_1\lor\dots\lor l_k$ and $m_1\lor\dots\lor m_n$, where $l_i=\neg m_j$. In any model where both parents are true, either $l_i$ is false (so another $l$-literal is true) or $m_j$ is false (so another $m$-literal is true). Either way the resolvent is true. So resolution never derives anything that is not entailed.
- **Complete** (refutation-complete): if $KB\models\alpha$, then $KB\land\neg\alpha$ is unsatisfiable. The **ground resolution theorem** says the resolution closure of an unsatisfiable clause set contains the empty clause. With Herbrand's theorem and the **lifting lemma** this extends to first-order logic. So resolution always finds a refutation when one exists. (It is not complete for *generating* all consequences, and in FOL it may not terminate when $\alpha$ is not entailed.)

**Strategies to speed up resolution** (4).

- **Set of support:** a subset of the clauses, the set of support, initially the **negated query**. Every resolution step must involve at least one clause from it, and resolvents join the set. This keeps the search focused on the goal, avoiding useless resolutions among the KB's own facts. It is complete if the KB itself is satisfiable.
- **Unit preference:** prefer resolutions in which one parent is a **unit clause** (a single literal). The resolvent is then shorter than the other parent, moving towards the empty clause quickly (as in unit propagation).
