---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Nodes CB, OP, CA, KN, PC; arcs CB -> OP and OP, CA, KN -> PC. CPTs: P(CB), P(CA), P(KN) (one number each); P(OP | CB) (2 rows); P(PC | OP, CA, KN) (8 rows), possibly deterministic (PC only if all three are true). 1 + 1 + 1 + 2 + 8 = 13 independent numbers."
sources: ["MNM slides Uncertainty-2-BN (constructing Bayesian networks, CPT sizes)", "AIMA 3e sec. 14.1-14.2"]
---
**Nodes:** $CB$ (charged battery), $OP$ (operational phone), $CA$ (in coverage area), $KN$ (knows the number), $PC$ (places a call). All are Boolean.

**Arcs:** $CB\to OP$; $OP\to PC$, $CA\to PC$, $KN\to PC$. There are no other dependencies.

```text
   CB
    |
    v
   OP      CA      KN
     \     |      /
      v    v     v
          PC
```

**Form of each CPT.**

| Node | Parents | CPT |
|:--|:--|:--|
| $CB$ | none | $P(cb)$: 1 number |
| $CA$ | none | $P(ca)$: 1 number |
| $KN$ | none | $P(kn)$: 1 number |
| $OP$ | $CB$ | $P(op\mid cb)$, $P(op\mid\neg cb)$: 2 rows |
| $PC$ | $OP$, $CA$, $KN$ | $P(pc\mid OP,CA,KN)$ for all 8 combinations: 8 rows |

CPT of $PC$:

| $OP$ | $CA$ | $KN$ | $P(pc)$ |
|:-:|:-:|:-:|:-:|
| T | T | T | $p_1$ (high, e.g. 0.99) |
| T | T | F | $p_2$ |
| T | F | T | $p_3$ |
| T | F | F | $p_4$ |
| F | T | T | $p_5$ |
| F | T | F | $p_6$ |
| F | F | T | $p_7$ |
| F | F | F | $p_8$ |

"Enables" suggests that a call is possible only when all three hold, so $p_2..p_8\approx0$. In the deterministic case, $PC\Leftrightarrow OP\land CA\land KN$. Likewise $P(op\mid\neg cb)\approx0$.

**Total:** $1+1+1+2+8=$ **13** independent numbers, against $2^5-1=31$ for the full joint distribution.
