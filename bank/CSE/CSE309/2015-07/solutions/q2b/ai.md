---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Triples refer to results by the position of the triple, so moving an instruction (code optimization) requires changing every reference to it. Solution: indirect triples, a separate list of pointers to triples, so the optimizer reorders the pointer list and the triples (and their references) stay unchanged; quadruples with explicit temporaries also avoid the problem."
sources: ["KMS Chapter 6 slides 20-36 (three-address code representations)", "Dragon book 2e sec. 6.2.4"]
---
**Problem.** In a triple $(op, arg_1, arg_2)$ there is no explicit result name; a later instruction refers to the result by the **position (number) of the triple** that computes it. If the optimizer moves, deletes or inserts an instruction, the triples change position, so **every reference to the moved triples must be found and renumbered**. That is slow and error-prone, so triples are inconvenient for optimizing compilers (quadruples name the result with a temporary, which stays valid when the instruction is moved).

**Example.** For `x = (a + b) - (c * d)`:

| # | op | arg1 | arg2 |
|:-:|:-:|:-:|:-:|
| (0) | `+` | `a` | `b` |
| (1) | `*` | `c` | `d` |
| (2) | `-` | `(0)` | `(1)` |
| (3) | `=` | `x` | `(2)` |

If the optimizer wants to evaluate `c * d` first (for example to schedule a slow multiplication earlier), the triples must be swapped: the multiplication becomes (0), the addition (1), and the references in (2) must be changed to `(1)` and `(0)`: all users of the moved triples must be edited.

**Solution: indirect triples** (Dragon book sec. 6.2.4). Keep the triples in a table, but let the program be a separate **list of pointers** (an instruction array) to the triples:

| Instruction | Pointer to |
|:-:|:-:|
| 35 | (0) |
| 36 | (1) |
| 37 | (2) |
| 38 | (3) |

The triples (0)-(3) keep their numbers and their internal references `(0)`, `(1)` never change. To reorder the code the optimizer only **permutes the instruction list**: swapping entries 35 and 36 executes the multiplication first, and nothing else needs to be updated. Indirect triples take about as much space as quadruples but, as with quadruples, instructions are easy to move; common sub-expressions can also be shared by letting two instruction entries point to the same triple.
