---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "The parse tree is a left-leaning chain of N nodes: N(3): cnt 1, max 3, maxi 0, gt 1; N(3,6): cnt 2, max 6, maxi 1, gt 2; N(..1): cnt 3, max 6, maxi 1, gt 2; N(..2): cnt 4, max 6, maxi 1, gt 2; N(..5): cnt 5, max 6, maxi 1, gt 3; L prints 1 and 3."
sources: ["KMS Chapter 5 slides 16-22 (Annotated parse tree, Evaluating an SDD)", "Dragon book 2e sec. 5.1.2"]
---
Using the SDD of 1(a). Each $N$ node is annotated with (cnt, max, maxi, gt); each **num** leaf with its value.

```text
L   [prints maxi = 1, gt = 3]
|-- {
|-- N5  [cnt=5, max=6, maxi=1, gt=3]
|   |-- N4  [cnt=4, max=6, maxi=1, gt=2]
|   |   |-- N3  [cnt=3, max=6, maxi=1, gt=2]
|   |   |   |-- N2  [cnt=2, max=6, maxi=1, gt=2]
|   |   |   |   |-- N1  [cnt=1, max=3, maxi=0, gt=1]
|   |   |   |   |   `-- num [val=3]
|   |   |   |   |-- ,
|   |   |   |   `-- num [val=6]
|   |   |   |-- ,
|   |   |   `-- num [val=1]
|   |   |-- ,
|   |   `-- num [val=2]
|   |-- ,
|   `-- num [val=5]
`-- }
```

**How the values were computed (bottom-up):**

1. $N_1 \to$ num(3): cnt = 1, max = 3, maxi = 0, gt = 1 (3 > 0).
2. $N_2 \to N_1$ , num(6): index 1; 6 > 3, so max = 6, maxi = 1; 6 > 1, so gt = 2; cnt = 2.
3. $N_3 \to N_2$ , num(1): index 2; 1 < 6, max unchanged; 1 > 2 is false, gt = 2; cnt = 3.
4. $N_4 \to N_3$ , num(2): index 3; no change to max; 2 > 3 is false, gt = 2; cnt = 4.
5. $N_5 \to N_4$ , num(5): index 4; 5 < 6; 5 > 4 is true, gt = 3; cnt = 5.
6. $L$: prints `N.maxi = 1` and `N.gt = 3`.
