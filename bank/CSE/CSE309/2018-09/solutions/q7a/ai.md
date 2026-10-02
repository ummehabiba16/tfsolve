---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Leaders 1, 2, 3, 10, 12, 13 give B1 = {1: i = 1}, B2 = {2: j = 1}, B3 = {3-9}, B4 = {10-11}, B5 = {12: i = 1}, B6 = {13-17}; edges B1-B2, B2-B3, B3-B3, B3-B4, B4-B2, B4-B5, B5-B6, B6-B6, B6-exit. Loops: {B3}, {B2, B3, B4}, {B6}."
sources: ["KMS Chapter 8 slides 27-36 (Basic Blocks and Flow Graphs, Constructing Basic Blocks, Loops)", "Dragon book 2e sec. 8.4.1, 8.4.3 (Example 8.6, Figs. 8.7, 8.9)"]
---
This is the textbook code that sets a 10 $\times$ 10 matrix to the identity matrix.

**Leaders** (Algorithm 8.5):

- the first instruction: **1**;
- targets of jumps: `goto (3)` gives **3**, `goto (2)` gives **2**, `goto (13)` gives **13**;
- instructions immediately after a jump: **10** (after 9), **12** (after 11).

Leaders: **1, 2, 3, 10, 12, 13**.

**Basic blocks:**

| Block | Instructions | Contents |
|:-:|:-:|:--|
| B1 | 1 | `i = 1` |
| B2 | 2 | `j = 1` |
| B3 | 3-9 | `t1 = 10 * i` ... `a[t4] = 0.0`; `j = j + 1`; `if j <= 10 goto B3` |
| B4 | 10-11 | `i = i + 1`; `if i <= 10 goto B2` |
| B5 | 12 | `i = 1` |
| B6 | 13-17 | `t5 = i - 1`; `t6 = 88 * t5`; `a[t6] = 1.0`; `i = i + 1`; `if i <= 10 goto B6` |

**Flow graph:**

```text
   ENTRY
     |
     v
    B1   i = 1
     |
     v
 +-> B2   j = 1
 |   |
 |   v
 |   B3   t1 = 10*i ... a[t4] = 0.0; j = j + 1
 |   |  \__ if j <= 10 goto B3   (self loop)
 |   v
 +-- B4   i = i + 1; if i <= 10 goto B2
     |
     v
    B5   i = 1
     |
     v
    B6   t5 = i - 1 ... a[t6] = 1.0; i = i + 1
     |  \__ if i <= 10 goto B6   (self loop)
     v
   EXIT
```

Edges: B1 $\to$ B2; B2 $\to$ B3; B3 $\to$ B3, B3 $\to$ B4; B4 $\to$ B2, B4 $\to$ B5; B5 $\to$ B6; B6 $\to$ B6, B6 $\to$ EXIT.

**Loops:** {B3} (inner loop over `j`), {B2, B3, B4} (outer loop over `i`), and {B6} (the diagonal loop).
