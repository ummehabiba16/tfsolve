---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Markers M -> eps { M.instr = nextinstr } and N -> eps { N.nextlist = makelist(nextinstr); gen(goto \\_) }. (i) S -> if (B) M1 S1 N else M2 S2 { backpatch(B.truelist, M1.instr); backpatch(B.falselist, M2.instr); temp = merge(S1.nextlist, N.nextlist); S.nextlist = merge(temp, S2.nextlist) }. (ii) S -> while M1 (B) M2 S1 { backpatch(S1.nextlist, M1.instr); backpatch(B.truelist, M2.instr); S.nextlist = B.falselist; gen(goto M1.instr) }."
sources: ["KMS Chapter 6 slides 104-114 (Backpatching for Flow-of-Control Statements)", "Dragon book 2e sec. 6.7.3 (Fig. 6.46)"]
---
**Assumptions.** The head of production (ii) is $S$ (it is missing on the paper). The usual functions are available: `makelist`, `merge`, `backpatch`, `nextinstr`, `gen`. $B$ has `truelist` and `falselist`; statements have `nextlist` (incomplete jumps to the code after the statement).

**Marker nonterminals:**

```text
M -> eps    { M.instr = nextinstr; }
N -> eps    { N.nextlist = makelist(nextinstr);  gen('goto _'); }
```

`M` records the index of the next instruction to be generated. `N` emits a jump whose target is not yet known and keeps it on a list.

**(i) If-else**

```text
S -> if ( B ) M1 S1 N else M2 S2
     { backpatch(B.truelist,  M1.instr);
       backpatch(B.falselist, M2.instr);
       temp = merge(S1.nextlist, N.nextlist);
       S.nextlist = merge(temp, S2.nextlist); }
```

- If $B$ is true, jump to the start of $S_1$ ($M_1$); if false, jump to the start of $S_2$ ($M_2$).
- `N` generates the jump that skips $S_2$ after $S_1$.
- All exits (the end of $S_1$ via $N$, and the ends of $S_1$ and $S_2$) go to the statement after $S$, which is not yet known, so they become $S.nextlist$.

**(ii) While**

```text
S -> while M1 ( B ) M2 S1
     { backpatch(S1.nextlist, M1.instr);
       backpatch(B.truelist,  M2.instr);
       S.nextlist = B.falselist;
       gen('goto' M1.instr); }
```

- $M_1$ marks the start of the test, so after the body ($S_1.nextlist$) and at the end of the loop (the generated `goto`), control returns to the test.
- If $B$ is true, control goes to the body ($M_2$).
- If $B$ is false, the loop is left; these jumps become $S.nextlist$.

**Example** (`while (a < b) a = a + 1;` starting at 100):

```text
100: if a < b goto 102      (B.truelist -> M2 = 102)
101: goto _                 (B.falselist = S.nextlist)
102: t1 = a + 1
103: a = t1
104: goto 100               (back to M1 = 100)
```
