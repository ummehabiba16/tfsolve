---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Leaders 1, 3, 4, 5, 6, 24, 26 (line 2 is not a target: goto L4 jumps to line 3). Blocks: B1 = {1-2}, B2 = {3}, B3 = {4}, B4 = {5}, B5 = {6-23}, B6 = {24-25}, B7 = {26}. Edges: B1-B2, B2-B3, B2-B7, B3-B4, B4-B5, B4-B6, B5-B4, B6-B2."
sources: ["KMS Chapter 8 slides 27-36 (Basic Blocks and Flow Graphs, Constructing Basic Blocks)", "Dragon book 2e sec. 8.4.1, 8.4.3 (Algorithm 8.5)"]
---
**Leaders** (Algorithm 8.5):

- the first instruction: **1**;
- targets of jumps: `goto L2` gives **26**, `goto L7` gives **24**, `goto L6` gives **5**, `goto L4` gives **3**;
- instructions immediately after a jump: **4** (after 3), **6** (after 5), **24** (after 23), **26** (after 25).

Leaders: **1, 3, 4, 5, 6, 24, 26**. Labels L1, L3, L5, L8, L9, L10 and L11 are never jumped to, so they do not start blocks.

**Basic blocks:**

| Block | Lines | Contents |
|:-:|:-:|:--|
| B1 | 1-2 | `i = 0`; `d = 4` |
| B2 | 3 | `iffalse i < d goto B7` |
| B3 | 4 | `j = i + 1` |
| B4 | 5 | `iffalse j < d goto B6` |
| B5 | 6-23 | `t1 = i * 16` ... `a[t13] = temp`; `j = j + 1`; `goto B4` |
| B6 | 24-25 | `i = i + 1`; `goto B2` |
| B7 | 26 | (exit) |

**Flow graph:**

```text
       B1  (i = 0; d = 4)
        |
        v
   +--> B2  (iffalse i < d goto B7) ------> B7 (exit)
   |    |
   |    v
   |    B3  (j = i + 1)
   |    |
   |    v
   |    B4  (iffalse j < d goto B6) --+
   |    |   ^                         |
   |    v   |                         v
   |    B5 -+  (body; goto B4)        B6 (i = i + 1; goto B2)
   |                                  |
   +----------------------------------+
```

Edges: B1 $\to$ B2; B2 $\to$ B3 (fall through), B2 $\to$ B7; B3 $\to$ B4; B4 $\to$ B5, B4 $\to$ B6; B5 $\to$ B4; B6 $\to$ B2. The inner loop is {B4, B5} and the outer loop is {B2, B3, B4, B5, B6}.
