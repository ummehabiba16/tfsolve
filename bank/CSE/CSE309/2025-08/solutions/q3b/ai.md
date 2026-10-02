---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "An LL(0) grammar chooses every production without looking at the input, so each nonterminal must have exactly one production; e.g. S -> a A B, A -> b C, B -> d, C -> c generates only the string abcd. It is LL(0) because there is never a choice to make."
sources: ["MMA syntax analysis slides 103-111 (LL(1) Grammars)", "Dragon book 2e sec. 4.4.3"]
---
**Grammar:**

$$S \to aAB$$

$$A \to bC$$

$$B \to d$$

$$C \to c$$

**Justification.**

- In LL($k$), the parser scans left to right, produces a leftmost derivation, and chooses the production for the leftmost nonterminal by looking at $k$ input symbols.
- With $k = 0$ it looks at **no** input symbol, so the choice must be forced: every nonterminal can have **only one** production. That is true here; each of $S$, $A$, $B$, $C$ has exactly one body.
- The parser simply expands each nonterminal with its only production and matches terminals:

$$S \Rightarrow aAB \Rightarrow abCB \Rightarrow abcB \Rightarrow abcd$$

- The grammar is not left recursive and no derivation can loop, so the parse always terminates.

Hence the grammar is LL(0). As a consequence, an LL(0) grammar generates **at most one string** (here `abcd`), so such grammars are of little practical use.
