---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "An LL(0) grammar has exactly one production per nonterminal (no lookahead is used to choose), e.g. S -> aAB, A -> b, B -> c generating only abc; such a grammar generates at most one string, so it is useless for parsing real languages."
sources: ["MMA syntax analysis slides 103-111 (LL(1) Grammars)", "Dragon book 2e sec. 4.4.3"]
---
**General appearance.** An LL($k$) parser chooses the production for the leftmost nonterminal by looking at $k$ input symbols. With $k = 0$ it looks at **none**, so there can never be a choice: **every nonterminal has exactly one production**. To terminate, the grammar must also have no recursion (otherwise a derivation never ends).

**Examples:**

$$S \to aAB, \quad A \to b, \quad B \to c \qquad L = \{abc\}$$

$$S \to \textbf{int}\ \textbf{id}\ ;\qquad L = \{\textbf{int id ;}\}$$

$$S \to \epsilon \qquad L = \{\epsilon\}$$

The parser expands each nonterminal with its single body and matches terminals, e.g. $S \Rightarrow aAB \Rightarrow abB \Rightarrow abc$.

**Applicability.** Since there is no choice anywhere, an LL(0) grammar generates **at most one string**. Parsing then means comparing the input with that fixed string. Real programming languages have infinitely many programs and need alternatives (and usually recursion), so LL(0) grammars are of no practical use; at least LL(1) is needed.
