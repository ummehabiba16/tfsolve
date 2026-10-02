---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Backpatching generates jumps with their targets left empty, keeps lists of such jumps (truelist, falselist, nextlist) as attributes, and fills in (backpatches) the targets when they become known, so code is produced in one pass. Scheme: M -> eps { M.instr = nextinstr }; B -> B1 || M B2 { backpatch(B1.falselist, M.instr); B.truelist = merge(B1.truelist, B2.truelist); B.falselist = B2.falselist }; B -> B1 && M B2 { backpatch(B1.truelist, M.instr); B.truelist = B2.truelist; B.falselist = merge(B1.falselist, B2.falselist) }; B -> E1 rel E2 { B.truelist = makelist(nextinstr); B.falselist = makelist(nextinstr + 1); gen(if E1.addr rel.op E2.addr goto \\_); gen(goto \\_) }."
sources: ["KMS Chapter 6 slides 104-109 (Backpatching, Backpatching for Boolean Expression)", "Dragon book 2e sec. 6.7.1-6.7.2 (Fig. 6.43)"]
---
**What is backpatching? (3 marks)** In one-pass code generation for boolean expressions and flow of control, a jump often has to be generated **before its target is known**, e.g. the jump taken when `B` is false. **Backpatching** generates such jumps with the target **left unspecified**, records them in **lists** (synthesized attributes `truelist`, `falselist`, `nextlist`), and later, when the target instruction is known, **fills in** the target of every jump on the list. This avoids a second pass over the code.

Helper functions:

- `makelist(i)`: a new list containing only instruction index `i`;
- `merge(p1, p2)`: the concatenation of two lists;
- `backpatch(p, i)`: insert `i` as the target of each jump on list `p`;
- `nextinstr`: the index of the next instruction to be generated.

**Translation scheme (9 marks).** The marker $M$ records the index of the first instruction of $B_2$:

```text
M -> eps             { M.instr = nextinstr; }

B -> B1 || M B2      { backpatch(B1.falselist, M.instr);
                       B.truelist  = merge(B1.truelist, B2.truelist);
                       B.falselist = B2.falselist; }

B -> B1 && M B2      { backpatch(B1.truelist, M.instr);
                       B.truelist  = B2.truelist;
                       B.falselist = merge(B1.falselist, B2.falselist); }

B -> E1 rel E2       { B.truelist  = makelist(nextinstr);
                       B.falselist = makelist(nextinstr + 1);
                       gen('if' E1.addr rel.op E2.addr 'goto _');
                       gen('goto _'); }
```

- For `||`: if $B_1$ is false, evaluate $B_2$, so $B_1$'s false exits jump to $M$. If either is true, $B$ is true.
- For `&&`: if $B_1$ is true, evaluate $B_2$. If either is false, $B$ is false.
- The relational expression generates one conditional and one unconditional jump, both incomplete, and puts them on the true and false lists.
