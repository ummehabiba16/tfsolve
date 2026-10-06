---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FIRST(S)={a,b,eps}, FIRST(A)={b,c,eps}, FIRST(B)={b}; FOLLOW(S)={\\$}, FOLLOW(A)={a}, FOLLOW(B)={a,b,c}. The table has no multiple entries (LL(1)). On bcba the parser makes the moves S -> BAa, B -> b, match b, A -> cA, match c, A -> bA, match b, A -> eps, match a, accept."
sources: ["MMA syntax analysis slides 76-151 (FIRST/FOLLOW, LL(1) table, predictive parsing)", "Dragon book 2e sec. 4.4.2-4.4.4"]
---
Grammar: $S \to aAa \mid BAa \mid \epsilon$, $A \to cA \mid bA \mid \epsilon$, $B \to b$.

**FIRST and FOLLOW.**

| | FIRST | FOLLOW |
|:-:|:--|:--|
| $S$ | $\{a, b, \epsilon\}$ | $\{\$\}$ |
| $A$ | $\{b, c, \epsilon\}$ | $\{a\}$ |
| $B$ | $\{b\}$ | $\{a, b, c\}$ |

($\text{FOLLOW}(A) = \{a\}$ because $A$ is followed by $a$ in both $S$-productions, and in $A \to cA \mid bA$ it ends the body. $\text{FOLLOW}(B) = \text{FIRST}(Aa) = \{b, c, a\}$.)

**Predictive parsing table** (blank = error):

| | $a$ | $b$ | $c$ | \$ |
|:-:|:-:|:-:|:-:|:-:|
| $S$ | $S \to aAa$ | $S \to BAa$ | | $S \to \epsilon$ |
| $A$ | $A \to \epsilon$ | $A \to bA$ | $A \to cA$ | |
| $B$ | | $B \to b$ | | |

($S \to aAa$ on $a$; $S \to BAa$ on $\text{FIRST}(BAa) = \{b\}$; $S \to \epsilon$ on $\text{FOLLOW}(S) = \{\$\}$; $A \to \epsilon$ on $\text{FOLLOW}(A) = \{a\}$.) No cell has two productions, so the grammar is **LL(1)**.

**Moves on the input `bcba`** (the question prints `"beba"`, which is blurred in the scan; since `e` is not a terminal of the grammar, `bcba` is meant). Stack shown with the **top at the left**, `$` at the bottom:

| Step | Stack | Input | Move |
|:-:|:--|:--|:--|
| 1 | `S $` | `bcba$` | output $S \to BAa$ |
| 2 | `B A a $` | `bcba$` | output $B \to b$ |
| 3 | `b A a $` | `bcba$` | match `b` |
| 4 | `A a $` | `cba$` | output $A \to cA$ |
| 5 | `c A a $` | `cba$` | match `c` |
| 6 | `A a $` | `ba$` | output $A \to bA$ |
| 7 | `b A a $` | `ba$` | match `b` |
| 8 | `A a $` | `a$` | output $A \to \epsilon$ |
| 9 | `a $` | `a$` | match `a` |
| 10 | `$` | `$` | **accept** |

The string is accepted; the leftmost derivation is $S \Rightarrow BAa \Rightarrow bAa \Rightarrow bcAa \Rightarrow bcbAa \Rightarrow bcba$.

*Check:* FIRST, FOLLOW, the table and this parse were computed by a script and agree.
