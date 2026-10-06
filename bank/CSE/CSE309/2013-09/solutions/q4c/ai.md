---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Shift-reduce parsing is bottom-up parsing with a stack and an input buffer: it shifts input symbols onto the stack and reduces the handle on top of the stack to the head of its production until the start symbol remains. Example: id + id * id with E -> E + T | T, T -> T * F | F, F -> id takes 5 shifts and 8 reductions (14 steps) and ends in accept."
sources: ["MMA syntax analysis slides 152-226 (shift-reduce parsing)", "Dragon book 2e sec. 4.5.3, Fig. 4.28"]
---
**Shift-reduce parsing** is a bottom-up method that uses a **stack** (initially `$`) and an **input buffer** (the string followed by `$`) and constructs a rightmost derivation in reverse (Dragon book sec. 4.5.3). The four actions:

1. **Shift:** move the next input symbol onto the top of the stack.
2. **Reduce:** the right end of a **handle** (the body of a production) is on top of the stack: pop the body and push the head of the production.
3. **Accept:** the stack holds the start symbol and the input is empty.
4. **Error:** syntax error, call the recovery routine.

The parser shifts until a handle appears on top and then reduces; the key problem is to decide whether to shift or reduce (LR parsers use a table for this). There can be **shift/reduce** and **reduce/reduce conflicts** for grammars that are not LR.

**Example.** Grammar $E \to E + T \mid T$, $T \to T * F \mid F$, $F \to \textbf{id}$; input `id + id * id`:

| Step | Stack | Input | Action |
|:-:|:--|:--|:--|
| 1 | `$` | `id + id * id $` | shift |
| 2 | `$ id` | `+ id * id $` | reduce $F \to \textbf{id}$ |
| 3 | `$ F` | `+ id * id $` | reduce $T \to F$ |
| 4 | `$ T` | `+ id * id $` | reduce $E \to T$ |
| 5 | `$ E` | `+ id * id $` | shift |
| 6 | `$ E +` | `id * id $` | shift |
| 7 | `$ E + id` | `* id $` | reduce $F \to \textbf{id}$ |
| 8 | `$ E + F` | `* id $` | reduce $T \to F$ |
| 9 | `$ E + T` | `* id $` | shift (not reduce $E \to E + T$, since `*` follows) |
| 10 | `$ E + T *` | `id $` | shift |
| 11 | `$ E + T * id` | `$` | reduce $F \to \textbf{id}$ |
| 12 | `$ E + T * F` | `$` | reduce $T \to T * F$ |
| 13 | `$ E + T` | `$` | reduce $E \to E + T$ |
| 14 | `$ E` | `$` | **accept** |

At step 9 the decision to shift is what gives `*` higher precedence than `+`. The reductions, read from the last to the first, give the rightmost derivation:

```text
E => E + T => E + T * F => E + T * id => E + F * id => E + id * id
  => T + id * id => F + id * id => id + id * id
```

*Check:* the trace was generated from the SLR(1) table of the grammar by a script.
