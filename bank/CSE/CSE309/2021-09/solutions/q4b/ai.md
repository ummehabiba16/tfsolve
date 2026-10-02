---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Use A -> eps as the default when no other production applies: in the procedure for A, if the lookahead is not in FIRST of any other body (and is in FOLLOW(A)), do nothing; in the table, enter A -> eps under every terminal of FOLLOW(A)."
sources: ["MMA basic concepts of parsing slides 38-42 (When to Use eps-Productions)", "Dragon book 2e sec. 2.4.3, 4.4.3"]
---
**Rule:** a predictive parser uses an $\epsilon$-production **as a default when no other production can be used**.

- In a recursive-descent parser: the procedure for $A$ checks the lookahead against FIRST of each non-$\epsilon$ body. If none matches, it takes $A \to \epsilon$ and returns without consuming input.
- In the table-driven form: $A \to \epsilon$ is placed in $M[A, b]$ for every $b \in$ FOLLOW($A$). The $\epsilon$-production is chosen when the next input symbol is something that can **follow** $A$.

**Example:**

```c
void optexpr() {
    if (lookahead == FIRST of expr) expr();
    /* else: optexpr -> eps; nothing is matched */
}
```

In `for ( ; expr ; expr ) other`, the first `optexpr` sees `;` (in FOLLOW(optexpr)) and uses the $\epsilon$-production.

For this to be correct, FOLLOW($A$) must be disjoint from FIRST of the other bodies of $A$ (LL(1) condition).
