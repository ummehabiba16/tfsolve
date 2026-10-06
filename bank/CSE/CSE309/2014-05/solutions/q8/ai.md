---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The grammar is already LL(1): FIRST(AaAb) = {a}, FIRST(BbBa) = {b} are disjoint and the eps-productions of A and B are the only alternatives of A and B, so every table entry holds one production; no processing is needed. M[S,a] = S -> AaAb, M[S,b] = S -> BbBa, M[A,a] = M[A,b] = A -> eps, M[B,a] = M[B,b] = B -> eps. ab and ba are accepted, abb is rejected."
sources: ["MMA syntax analysis slides 103-151 (LL(1), predictive table, parsing)", "Dragon book 2e sec. 4.4.3-4.4.4"]
---
Grammar: $S \to AaAb \mid BbBa$, $A \to \epsilon$, $B \to \epsilon$.

**FIRST and FOLLOW.** $\text{FIRST}(A) = \text{FIRST}(B) = \{\epsilon\}$. $\text{FIRST}(AaAb) = \{a\}$ (as $A$ vanishes) and $\text{FIRST}(BbBa) = \{b\}$, so $\text{FIRST}(S) = \{a, b\}$. $\text{FOLLOW}(S) = \{\$\}$. In $S \to AaAb$ the first $A$ is followed by $a$ and the second by $b$; in $S \to BbBa$ the first $B$ is followed by $b$ and the second by $a$: $\text{FOLLOW}(A) = \text{FOLLOW}(B) = \{a, b\}$.

**Is it LL(1)? Yes.**

- $S$: the two alternatives have *disjoint* FIRST sets, $\{a\}$ and $\{b\}$, and neither is nullable.
- $A$ and $B$ each have **one** production, $\epsilon$, so there can be no choice problem.

Equivalently, the table below has at most one production in every cell. Hence the grammar **is LL(1) and no processing (left factoring, left-recursion removal) is necessary.**

**Predictive parsing table:**

| | $a$ | $b$ | \$ |
|:-:|:-:|:-:|:-:|
| $S$ | $S \to AaAb$ | $S \to BbBa$ | |
| $A$ | $A \to \epsilon$ | $A \to \epsilon$ | |
| $B$ | $B \to \epsilon$ | $B \to \epsilon$ | |

($A \to \epsilon$ is placed under $\text{FOLLOW}(A) = \{a, b\}$, and likewise for $B$.)

**Parsing the strings** (stack top at the left):

*`ab`*

| Stack | Input | Move |
|:--|:--|:--|
| `S $` | `ab$` | $S \to AaAb$ |
| `A a A b $` | `ab$` | $A \to \epsilon$ |
| `a A b $` | `ab$` | match `a` |
| `A b $` | `b$` | $A \to \epsilon$ |
| `b $` | `b$` | match `b` |
| `$` | `$` | **accept** |

*`ba`*

| Stack | Input | Move |
|:--|:--|:--|
| `S $` | `ba$` | $S \to BbBa$ |
| `B b B a $` | `ba$` | $B \to \epsilon$ |
| `b B a $` | `ba$` | match `b` |
| `B a $` | `a$` | $B \to \epsilon$ |
| `a $` | `a$` | match `a` |
| `$` | `$` | **accept** |

*`abb`*

| Stack | Input | Move |
|:--|:--|:--|
| `S $` | `abb$` | $S \to AaAb$ |
| `A a A b $` | `abb$` | $A \to \epsilon$ |
| `a A b $` | `abb$` | match `a` |
| `A b $` | `bb$` | $A \to \epsilon$ |
| `b $` | `bb$` | match `b` |
| `$` | `b$` | **error**: the stack is empty but input remains |

So `ab` and `ba` are in the language and **`abb` is rejected**. (The language is exactly $\{ab, ba\}$.)

*Check:* FIRST, FOLLOW, the table and the three parses were computed by a script.
