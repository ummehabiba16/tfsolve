---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "An eps-production A -> eps is used as the default: the procedure for A tries the non-eps alternatives by their FIRST sets, and if the lookahead matches none it does nothing (returns without consuming input), which is correct when the lookahead is in FOLLOW(A); otherwise the error is caught later."
sources: ["MMA basic concepts of parsing slides 38-42 (When to Use eps-Productions)", "Dragon book 2e sec. 2.4.3"]
---
In a procedure-based predictive parser, each nonterminal $A$ has a procedure that chooses a production by comparing the lookahead with the FIRST sets of the bodies.

**Rule for $\epsilon$-productions:** the parser uses $A \to \epsilon$ **as a default** when no other production can be used. If the lookahead is not in FIRST of any non-$\epsilon$ body, the procedure simply **returns without doing anything** (it consumes no input). This is correct when the lookahead is in FOLLOW($A$): $A$ derives the empty string here, and the caller continues with the symbols after $A$.

**Example** (textbook):

$$optstmts \to stmt\_list \mid \epsilon$$

```c
void optstmts() {
    if (lookahead is in FIRST(stmt_list))
        stmt_list();
    /* else: use optstmts -> eps, do nothing */
}
```

Inside `stmt → begin optstmts end`, when the lookahead is `end`, `optstmts()` does nothing and the caller matches `end`.

**Notes:**

- For the choice to be safe, FIRST of the other bodies must not intersect FOLLOW($A$); otherwise the default hides a real choice (the grammar is not LL(1)).
- If the lookahead is neither in FIRST nor in FOLLOW($A$), the error is not reported in $A$ but at the next `match()` in the caller, slightly later. A stricter parser can test `lookahead in FOLLOW(A)` before taking the $\epsilon$-production.
