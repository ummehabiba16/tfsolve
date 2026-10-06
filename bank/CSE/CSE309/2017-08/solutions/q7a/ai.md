---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "4 conflicts: 2 reduce/reduce (after the first PLUS: a -> PLUS vs b -> PLUS; after the first MINUS: a -> MINUS vs c -> MINUS, both on end of input) and 2 shift/reduce (b -> b MINUS b . vs shifting MINUS; c -> c PLUS c . vs shifting PLUS), the latter because b MINUS b and c PLUS c are ambiguous (no associativity)."
sources: ["MMA syntax analysis slides 565-592 (Yacc / Bison); LALR conflicts slides 490-564", "Dragon book 2e sec. 4.8.1, 4.9.2"]
---
Yacc/Bison builds the **LALR(1)** table. For the grammar (start symbol $a$)

$$a \to b \mid c \mid \text{PLUS} \mid \text{MINUS}$$

$$b \to b\ \text{MINUS}\ b \mid \text{PLUS}$$

$$c \to c\ \text{PLUS}\ c \mid \text{MINUS}$$

the relevant LR(0) states and their conflicts are:

| State | Items | Lookahead | Conflict | Reason |
|:--|:--|:--|:--|:--|
| after `PLUS` at the start | $a \to \text{PLUS}\ \cdot$, $b \to \text{PLUS}\ \cdot$ | `$end` (end of input) | **reduce/reduce** | the single token `PLUS` can be reduced directly to $a$ (production 3) or first to $b$ and then to $a$ via $a \to b$; \$ is in the lookahead set of both reductions, so the grammar is ambiguous for the input `PLUS` |
| after `MINUS` at the start | $a \to \text{MINUS}\ \cdot$, $c \to \text{MINUS}\ \cdot$ | `$end` | **reduce/reduce** | the same ambiguity for the input `MINUS`: $a \to \text{MINUS}$ or $a \to c \to \text{MINUS}$ |
| after $b\ \text{MINUS}\ b$ | $b \to b\ \cdot\ \text{MINUS}\ b$, $b \to b\ \text{MINUS}\ b\ \cdot$ | `MINUS` | **shift/reduce** | $b \to b\ \text{MINUS}\ b$ is ambiguous: `PLUS MINUS PLUS MINUS PLUS` can group as $(b - b) - b$ (reduce first) or $b - (b - b)$ (shift); no associativity is declared |
| after $c\ \text{PLUS}\ c$ | $c \to c\ \cdot\ \text{PLUS}\ c$, $c \to c\ \text{PLUS}\ c\ \cdot$ | `PLUS` | **shift/reduce** | the same for $c \to c\ \text{PLUS}\ c$ |

So the number of conflicts is **4**: **2 reduce/reduce and 2 shift/reduce**.

Default resolution by Yacc (Dragon book sec. 4.9.2): a shift/reduce conflict is resolved in favour of **shift** (so the operators become right associative), and a reduce/reduce conflict in favour of the production listed **first** in the specification ($a \to \text{PLUS}$ and $a \to \text{MINUS}$ are chosen over $b \to \text{PLUS}$ and $c \to \text{MINUS}$). Declaring `%left MINUS` and `%left PLUS` removes the shift/reduce conflicts; the reduce/reduce conflicts need the grammar to be rewritten.

*Check:* the grammar was run through `bison -v`; its report is `2 shift/reduce, 2 reduce/reduce` in exactly the four states above.
