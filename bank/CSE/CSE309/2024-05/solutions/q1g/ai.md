---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "With one production per nonterminal there are no choices, so an LL(0) predictive parser (no lookahead, no backtracking, no table) is optimal; the grammar derives at most one string (none if it is recursive), so the parser just expands/compares in O(n)."
sources: ["MMA basic concepts of parsing slides 23-49 (Predictive Parsing)", "Dragon book 2e sec. 4.4"]
---
**Suggestion: a predictive top-down parser with no lookahead, i.e. LL(0).**

- A parser normally needs lookahead (LL(1), LR(1)) or backtracking only to **choose** among alternative productions. Here each nonterminal has exactly one production, so there is never a choice.
- A recursive-descent parser with one procedure per nonterminal simply calls the procedures and matches terminals in the order of the single body. It needs no FIRST/FOLLOW sets, no parsing table, no lookahead and no backtracking. Each input symbol is examined once, so time is $O(n)$ and space is the depth of the grammar.
- An LR parser would also work, but it builds item sets and tables for nothing; that is extra cost with no benefit.

**Observation that makes it even simpler:** such a grammar generates **at most one string**.

- If no nonterminal is recursive, the derivation is fixed, e.g. $S \to aAc$, $A \to b$ gives only `abc`. The best "parser" is then to precompute that string (and its parse tree) once and compare the input with it character by character.
- If some nonterminal is recursive (e.g. $S \to aS$), the derivation never ends, the language is empty, and every input is rejected.

So the optimal choice is an LL(0) / string-matching parser.
