---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Similar: on a correct input both parsers make exactly the same sequence of shifts and reductions (LALR states are merged LR states with the same cores, same shift/goto structure). Dissimilar: on an erroneous input LALR may do some extra reductions before detecting the error (never extra shifts), while the canonical LR parser detects it immediately; LALR may also have reduce/reduce conflicts LR does not."
sources: ["MMA syntax analysis slides 490-564 (Constructing LALR Parsing Tables)", "Dragon book 2e sec. 4.7.4"]
---
**Similarity: on correct input, identical moves.** An LALR state is the union of canonical LR(1) states with the same core. The shift and GOTO structure depends only on the cores, so it is identical. For a grammar that is LALR(1), when the input is a valid sentence, the LALR parser makes **exactly the same sequence of shifts and reductions** as the canonical LR parser. Only the state names differ (merged state $I_{36}$ instead of $I_3$ or $I_6$).

**Dissimilarity: on erroneous input, later error detection.** Merging unites lookaheads, so an LALR state may contain a reduce action on a symbol where one of the original LR states had **error**. On an incorrect input:

- the canonical LR parser reports the error immediately;
- the LALR parser may first perform **some extra reductions**, but **never an extra shift**, before it detects the same error. The error is still caught before any erroneous input symbol is shifted.

**Textbook example:** $S \to CC$, $C \to cC \mid d$. On input `ccd` followed by \$, the LR parser in state $I_4 = [C \to d\cdot, c/d]$ declares an error on \$. The LALR parser in merged state $I_{47} = [C \to d\cdot, c/d/\$]$ reduces $C \to d$ (and $C \to cC$, ...) first, and then finds the error.

**Other differences:** LALR has far fewer states (the same number as SLR). Merging may introduce reduce/reduce conflicts for some LR(1) grammars (such as the grammar of 4(b)), in which case LALR cannot parse them at all.
