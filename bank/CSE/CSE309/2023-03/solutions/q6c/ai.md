---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Markers: M -> eps { M.instr = nextinstr; } and N -> eps { N.nextlist = makelist(nextinstr); gen('goto \\_'); }. S -> for ( S1 ; M1 B ; M2 S2 N ) M3 S3 { backpatch(S1.nextlist, M1.instr); backpatch(B.truelist, M3.instr); backpatch(S2.nextlist, M1.instr); backpatch(N.nextlist, M1.instr); backpatch(S3.nextlist, M2.instr); gen('goto' M2.instr); S.nextlist = B.falselist; }. Layout: S1; M1: B; M2: S2; goto M1; M3: S3; goto M2."
sources: ["KMS Chapter 6 slides 104-114 (Backpatching, Backpatching for Flow-of-Control Statements)", "Dragon book 2e sec. 6.7.3 (Fig. 6.46)"]
---
**Assumptions.** The usual backpatching functions are used: `makelist(i)`, `merge(p1, p2)`, `backpatch(p, i)` and `nextinstr`. $B$ has `truelist` and `falselist`; statements have `nextlist`. $S_1$ and $S_2$ are statements (e.g. assignments) with their own `nextlist`.

**Code layout to be produced:**

```text
        code for S1                (initialisation)
M1:     code for B                 (test: true -> M3, false -> exit)
M2:     code for S2                (increment)
        goto M1                    (N)
M3:     code for S3                (body)
        goto M2
```

**Marker nonterminals:**

```text
M -> eps   { M.instr = nextinstr; }
N -> eps   { N.nextlist = makelist(nextinstr);  gen('goto _'); }
```

`M` records the index of the next instruction, i.e. the start of the code that follows. `N` emits an unfilled jump and remembers it.

**Production with markers and semantic actions:**

```text
S -> for ( S1 ; M1 B ; M2 S2 N ) M3 S3
     { backpatch(S1.nextlist, M1.instr);   /* after S1, go to the test       */
       backpatch(B.truelist,  M3.instr);   /* test true: start of the body   */
       backpatch(S2.nextlist, M1.instr);   /* after the increment: the test  */
       backpatch(N.nextlist,  M1.instr);   /* the jump emitted by N: test    */
       backpatch(S3.nextlist, M2.instr);   /* after the body: the increment  */
       gen('goto' M2.instr);               /* fall out of the body: increment */
       S.nextlist = B.falselist;           /* test false: leave the loop     */
     }
```

**Why it works.** The instructions are generated in textual order: $S_1$, $B$, $S_2$, the `goto` of $N$, $S_3$, the final `goto`. The jumps whose targets are not yet known when generated (the true and false exits of $B$, the jump of $N$) are left on lists and filled in later by `backpatch`, once the target addresses are known. The false exits of $B$ become the `nextlist` of the whole statement, and they are backpatched later by the enclosing construct.

**Example:** `for (i = 0; i < n; i = i + 1) x = x + i;` with the first instruction at 100:

```text
100: i = 0
101: if i < n goto 106        (B.truelist -> M3 = 106)
102: goto _                   (B.falselist = S.nextlist)
103: t1 = i + 1               (M2 = 103)
104: i = t1
105: goto 101                 (N -> M1 = 101)
106: t2 = x + i               (M3 = 106)
107: x = t2
108: goto 103                 (back to M2)
```
