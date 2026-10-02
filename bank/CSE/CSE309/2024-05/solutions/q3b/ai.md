---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "k = 3 (the grammar is LL(3)): S -> Aab begins with aac or bef, S -> aS with aaa, aab, abc or abe, S -> bc with bc; Aab and aS share aa (so k=2 fails) but differ in the 3rd symbol; A -> aacd | bef and B -> bef | eps need only k = 1 (B is unreachable)."
sources: ["MMA syntax analysis slides 103-111 (LL(1) Grammars), 76-102 (FIRST)", "Dragon book 2e sec. 4.4.3"]
---
For LL($k$), the alternatives of each nonterminal must be distinguishable by their first $k$ symbols, i.e. their FIRST$_k$ sets must be disjoint.

**Nonterminal $A$:** $A \to aacd \mid bef$. FIRST$_1$ = {a} vs {b}: disjoint, so $k = 1$ suffices.

**Nonterminal $B$:** $B \to bef \mid \epsilon$. $B$ appears in no production body, so it is unreachable and FOLLOW($B$) = $\emptyset$. FIRST$_1$ = {b} vs {}, so $k = 1$ suffices (and $B$ never takes part in parsing).

**Nonterminal $S$:** compute FIRST$_k$ of the three bodies.

- $Aab$: derives $aacdab$ or $befab$.
- $aS$: $a$ followed by any string of $S$; $S$ begins with $aac$, $bef$, $a\ldots$ or $bc$, so $aS$ begins with $aaa$, $aab$, $abe$ or $abc$.
- $bc$: derives only $bc$.

| $k$ | $Aab$ | $aS$ | $bc$ | Disjoint? |
|:-:|:--|:--|:--|:--|
| 1 | a, b | a | b | No: $a$ is shared by $Aab$/$aS$, and $b$ by $Aab$/$bc$ |
| 2 | aa, be | aa, ab | bc | No: $aa$ is shared by $Aab$ ($aacd\ldots$) and $aS$ ($a\,aS$, $a\,aacd\ldots$) |
| 3 | aac, bef | aaa, aab, abc, abe | bc | **Yes** |

With 3 symbols: if the input starts with $aac$, use $S \to Aab$; with $aaa$, $aab$, $abc$ or $abe$, use $S \to aS$; with $bef$, use $S \to Aab$; with $bc$, use $S \to bc$. ($aS$ can never start with $aac$, because after the first $a$, $S$ starts with $a$ or $b$, and $S \to Aab$ via $A \to aacd$ gives $a\,aac\ldots$.)

**Answer: $k = 3$; the grammar is LL(3) but not LL(2).**
