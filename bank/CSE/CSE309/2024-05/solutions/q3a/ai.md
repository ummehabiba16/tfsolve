---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "M[A,a] holding both A -> alpha and A -> eps means a is in FIRST(alpha) (alpha entry) and a is in FOLLOW(A) (eps entry), i.e. FIRST(alpha) and FOLLOW(A) intersect; the parser cannot decide, the grammar is not LL(1) (e.g. dangling else: M[S', e] = {S' -> eS, S' -> eps})."
sources: ["MMA syntax analysis slides 103-123 (LL(1) Grammars, Predictive Parsing Table)", "Dragon book 2e sec. 4.4.3 (Algorithm 4.31, Example 4.33)"]
---
**How entries are made** (Algorithm 4.31): for each production $A \to \alpha$,

1. for each terminal $a$ in FIRST($\alpha$), add $A \to \alpha$ to $M[A, a]$;
2. if $\epsilon \in$ FIRST($\alpha$), add $A \to \alpha$ to $M[A, b]$ for each $b$ in FOLLOW($A$).

**Meaning of the two entries in $M[A, a]$:**

- $A \to \alpha$ is there because $a \in$ FIRST($\alpha$): $A$ can begin with $a$ by using $\alpha$.
- $A \to \epsilon$ is there because $\epsilon \in$ FIRST($\epsilon$), so it is entered under every terminal of FOLLOW($A$). Hence $a \in$ FOLLOW($A$): $A$ can vanish and $a$ can come right after it.

So **FIRST($\alpha$) $\cap$ FOLLOW($A$) $\ne \emptyset$**. (If $\alpha \overset{*}{\Rightarrow} \epsilon$ as well, both bodies derive $\epsilon$, which also violates LL(1).) Seeing $a$, the parser cannot tell whether to expand $A$ by $\alpha$ or to erase it. The cell has a conflict and the grammar is **not LL(1)**: it is ambiguous or needs more lookahead.

**Example (dangling else):**

$$S \to iEtSS' \mid a, \qquad S' \to eS \mid \epsilon, \qquad E \to b$$

FIRST($eS$) = {e} and FOLLOW($S'$) = { e, \$ }, so $M[S', e] = \{S' \to eS,\ S' \to \epsilon\}$. In practice the conflict is resolved by choosing $S' \to eS$, which matches each `else` with the nearest `then`.
