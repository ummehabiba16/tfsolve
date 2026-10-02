---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A predictive parser chooses the production from the lookahead alone: the grammar has no left recursion and is left factored, and for each A the FIRST sets of its bodies are disjoint (and FOLLOW(A) is disjoint from FIRST of the other bodies when one body derives eps), so exactly one production can match the next input symbol and a wrong guess is never made."
sources: ["MMA basic concepts of parsing slides 23-49 (Predictive Parsing, Designing a Predictive Parser)", "Dragon book 2e sec. 2.4.2, 4.4.1, 4.4.3"]
---
**Backtracking** happens in general recursive descent when the parser has to *guess* which production of $A$ to use, tries it, and on failure resets the input pointer and tries another.

A **predictive parser** avoids guessing: it uses the **lookahead symbol** to choose the one production that can succeed. This works because the grammar is restricted:

1. **FIRST sets of alternatives are disjoint.** For $A \to \alpha \mid \beta$, FIRST($\alpha$) $\cap$ FIRST($\beta$) $= \emptyset$. So the lookahead $a$ belongs to at most one alternative, and that is the only production that could derive a string starting with $a$.
2. **$\epsilon$-alternatives are decided with FOLLOW.** If $\beta \overset{*}{\Rightarrow} \epsilon$, then FIRST($\alpha$) $\cap$ FOLLOW($A$) $= \emptyset$. The $\epsilon$-production is chosen only when the lookahead can follow $A$.
3. **No left recursion.** Otherwise $A \to A\alpha$ would make the procedure for $A$ call itself without consuming input.
4. **Left factored.** Alternatives with a common prefix ($A \to \alpha\beta_1 \mid \alpha\beta_2$) are rewritten so that the choice is postponed until it can be made ($A \to \alpha A'$).

These are exactly the conditions for an **LL(1)** grammar. Under them, the parsing table $M[A, a]$ (or the `if/switch` on `lookahead` in each procedure) has at most one entry. The parser therefore never has to undo a choice. If no production matches, the input is in error, and the error is detected immediately rather than after backtracking.

**Example:** `stmt -> expr ; | if ( expr ) stmt | for ( optexpr ; optexpr ; optexpr ) stmt | other`. The lookahead `if`, `for`, `other` or FIRST(expr) selects the production directly.
