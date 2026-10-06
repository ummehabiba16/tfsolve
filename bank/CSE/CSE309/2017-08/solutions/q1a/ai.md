---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "No. Left factoring only postpones the choice between productions with a common prefix; the language and the parse trees are unchanged, so an ambiguous grammar stays ambiguous (the left-factored dangling-else grammar still has two entries in M[S', e]). Ambiguity is removed by rewriting the grammar (e.g. matched/unmatched statements), not by left factoring."
sources: ["MMA syntax analysis slides 61-69 (Left Factoring)", "Dragon book 2e sec. 4.3.2 (Example 4.16), 4.3.4, 4.4.3"]
---
**Answer: No.**

**What left factoring does.** If two productions of $A$ start with the same prefix, $A \to \alpha\beta_1 \mid \alpha\beta_2$, left factoring rewrites them as

$$A \to \alpha A'$$

$$A' \to \beta_1 \mid \beta_2$$

so the parser can postpone its decision until it has seen enough input to choose between $\beta_1$ and $\beta_2$. This is useful for **predictive (top-down) parsing**: it removes the need to guess or backtrack on a common prefix.

**Why it does not remove ambiguity.** Left factoring generates the *same language* and every parse tree of the old grammar corresponds one-to-one to a parse tree of the new grammar (only the extra nonterminal $A'$ appears). A string that had two parse trees still has two. Ambiguity has to be removed by changing what the grammar says (precedence, associativity, matching rule), which is a different transformation.

**Example (dangling else, Dragon book sec. 4.3.2).**

$$S \to iEtS \mid iEtSeS \mid a$$

$$E \to b$$

The string $iEtiEtaea$ has two parse trees (the `e` belongs to the inner or the outer `if`). Left factoring the common prefix $iEtS$ gives

$$S \to iEtSS' \mid a$$

$$S' \to eS \mid \epsilon$$

$$E \to b$$

Now $\text{FOLLOW}(S') = \{e, \$\}$, and $e \in \text{FIRST}(eS)$, so the LL(1) table has **two entries in $M[S', e]$**: $S' \to eS$ and $S' \to \epsilon$:

| Nonterminal | $a$ | $b$ | $e$ | $i$ | $t$ | \$ |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| $S$ | $S \to a$ | | | $S \to iEtSS'$ | | |
| $E$ | | $E \to b$ | | | | |
| $S'$ | | | $S' \to eS$, $S' \to \epsilon$ | | | $S' \to \epsilon$ |

The grammar is still ambiguous (and not LL(1)). The conflict is resolved only by an extra rule "match each `else` with the closest unmatched `then`", i.e. by choosing $S' \to eS$, or by rewriting the grammar with *matched* and *unmatched* statements (Dragon book Example 4.16).

**Conclusion.** Left factoring helps make a grammar LL(1) but is not a method for eliminating ambiguity.
