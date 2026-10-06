---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Three-address code consists of instructions with at most one operator and three addresses: x = y op z, x = op y, x = y, goto L, if x relop y goto L, param/call/return for procedures, indexed copies x = y[i] and x[i] = y, and pointer operations; it is the common intermediate representation, stored as quadruples, triples or indirect triples."
sources: ["KMS Chapter 6 slides 20-36 (three-address code)", "Dragon book 2e sec. 6.2"]
---
**Three-address code** is an intermediate representation in which each instruction has **at most one operator on the right side** and at most **three addresses** (two operands and one result), so the compiler breaks up expressions into simple steps and gives names (temporaries) to intermediate values. For $x + y * z$ it gives $t_1 = y * z$; $t_2 = x + t_1$. It resembles assembly and is easy to optimise and to translate into machine code (Dragon book sec. 6.2).

An *address* can be a name from the source program (via the symbol table), a constant, or a compiler-generated temporary. Common instruction forms:

| Form | Meaning |
|:--|:--|
| `x = y op z` | binary operation |
| `x = op y` | unary operation (`minus`, `!`, conversion) |
| `x = y` | copy |
| `goto L` | unconditional jump |
| `if x goto L`, `ifFalse x goto L` | conditional jump on a boolean value |
| `if x relop y goto L` | conditional jump on a comparison |
| `param x`, `call p, n`, `return y` | procedure call with $n$ parameters |
| `x = y[i]`, `x[i] = y` | indexed copy (array access) |
| `x = &y`, `x = *y`, `*x = y` | address and pointer operations |
| `L:` | label |

**Example.** `a = b * -c + b * -c` becomes

```text
t1 = minus c
t2 = b * t1
t3 = minus c
t4 = b * t3
t5 = t2 + t4
a  = t5
```

**Representations:** *quadruples* (op, arg1, arg2, result), *triples* (op, arg1, arg2; results referred to by position) and *indirect triples* (a pointer list over triples).
