---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "begin = newlabel(); S1.next = newlabel(); B.true = S.next; B.false = begin; S.code = label(begin) || S1.code || label(S1.next) || B.code, so the body is executed, B is tested, and control exits to S.next when B is true and repeats from begin when false."
sources: ["KMS Chapter 6 slides 72-103 (flow-of-control statements)", "Dragon book 2e sec. 6.6.3, Fig. 6.36"]
---
The question asks for the semantic rules for the (repeat-until) loop in the production

$$S \to \textbf{repeat}\ S_1\ \textbf{until}\ B$$

Attributes: $S.next$ (inherited, the label of the code that follows $S$), $S.code$; $B.true$, $B.false$ (inherited labels), $B.code$ (jumping code that jumps to $B.true$ or $B.false$). The loop body runs first, then the condition is tested; **the loop exits when $B$ is true** and repeats while $B$ is false.

| Production | Semantic rules |
|:--|:--|
| $S \to \textbf{repeat}\ S_1\ \textbf{until}\ B$ | $begin = newlabel()$ |
| | $S_1.next = newlabel()$ |
| | $B.true = S.next$ |
| | $B.false = begin$ |
| | $S.code = label(begin)\ /\!/\ S_1.code\ /\!/\ label(S_1.next)\ /\!/\ B.code$ |

($/\!/$ is concatenation.) The generated code has the shape:

```text
begin:   code of S1
S1.next: code of B  (if B goto S.next  else goto begin)
S.next:  ...
```

$S_1.next$ labels the first instruction after the body, i.e. the beginning of the test, so that any jump out of $S_1$ (such as a `break`-free fall-through or a jump from a nested statement) lands on the test. $B.true = S.next$ leaves the loop; $B.false = begin$ goes round again. No $\textbf{goto}$ is needed at the end because $B.code$ always ends by jumping to one of its two labels.
