---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Top-down: which production to use to expand the leftmost nonterminal (predict, using the lookahead and FIRST/FOLLOW), plus matching terminals. Bottom-up: when to reduce (finding the handle) and which production to reduce by; otherwise shift (shift vs reduce, reduce vs reduce)."
sources: ["MMA basic concepts of parsing slides 2-22 (Top-Down Parsing), syntax analysis slides 152-226 (Bottom-Up Parsing)", "Dragon book 2e sec. 4.4, 4.5"]
---
**Top-down parsing** (builds the tree from the root, leftmost derivation):

- The key decision at each step is **which production to apply** to expand the leftmost nonterminal $A$, given the next input symbol(s).
- After that, terminals in the production body are simply matched with the input.
- A predictive (LL(1)) parser decides with one lookahead symbol using FIRST and FOLLOW (table $M[A, a]$). A general recursive-descent parser may guess and backtrack.

**Bottom-up parsing** (builds the tree from the leaves, rightmost derivation in reverse):

- The key decisions are **when to reduce** and **which production to reduce by**.
- *Shift or reduce?* Is there a handle on top of the stack now? (shift/reduce conflict)
- *Which reduction?* If several bodies match the top of the stack, which one is the handle? (reduce/reduce conflict)
- Identifying the handle correctly is the main problem. LR parsers use the state on top of the stack and the lookahead (ACTION table) to decide.

| | Top-down | Bottom-up |
|:--|:--|:--|
| Decision | which $A$-production to expand with | shift vs reduce; which production to reduce by |
| Made | before seeing what $A$ derives | after seeing the whole body (handle) |
| Information | lookahead, FIRST/FOLLOW | stack state + lookahead (LR items) |

Because a bottom-up parser decides only after it has seen the whole body, it can handle a larger class of grammars (LR $\supset$ LL).
