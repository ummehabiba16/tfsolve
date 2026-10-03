---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Assign in order 1..8, trying R before B, with forward checking. 1:R makes 2, 5 and 8 lose R; 2:B wipes out 3's domain {B}, so backtrack; 2 has no other value, so backtrack to 1. 1:B; 2:R; 3:B; 4:R wipes out 5's domain, so backtrack; 4:B; 5:R; 6:R; 7:B; 8:R. Solution 1B 2R 3B 4B 5R 6R 7B 8R."
sources: ["AIMA 3e sec. 6.3.2 (forward checking)"]
---
**Constraint graph.** Edges 6-4, 4-5, 5-1, 2-3, 6-7, 7-8, 8-1, 1-2; adjacent nodes must differ. Domains are {R, B}, except node 3, which is {B}. Variables are assigned in the order 1, 2, ..., 8, trying R first. **Forward checking** removes the assigned colour from the domains of *unassigned* neighbours, and backtracks if a domain becomes empty. Assigned values are shown in brackets, e.g. (R).

| Step | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | Remark |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| Initial domains | RB | RB | B | RB | RB | RB | RB | RB | |
| 1: R | (R) | B | B | RB | B | RB | RB | B | 2, 5, 8 lose R |
| 2: B | (R) | (B) | **empty** | RB | B | RB | RB | B | 3 loses B, so its domain is empty: **backtrack** |
| 2: no value left | | | | | | | | | **backtrack** to node 1 |
| 1: B | (B) | R | B | RB | R | RB | RB | R | 2, 5, 8 lose B |
| 2: R | (B) | (R) | B | RB | R | RB | RB | R | 3 keeps B |
| 3: B | (B) | (R) | (B) | RB | R | RB | RB | R | |
| 4: R | (B) | (R) | (B) | (R) | **empty** | B | RB | R | 5 loses R, so its domain is empty: **backtrack** |
| 4: B | (B) | (R) | (B) | (B) | R | R | RB | R | 5 and 6 lose B |
| 5: R | (B) | (R) | (B) | (B) | (R) | R | RB | R | |
| 6: R | (B) | (R) | (B) | (B) | (R) | (R) | B | R | 7 loses R |
| 7: B | (B) | (R) | (B) | (B) | (R) | (R) | (B) | R | 8 keeps R |
| 8: R | (B) | (R) | (B) | (B) | (R) | (R) | (B) | (R) | **solution** |

**The algorithm backtracks** (i) after $2=B$ (node 3 is wiped out), and then again to node 1, since node 2 has no other value; and (ii) after $4=R$ (node 5 is wiped out).

**Solution:** 1 = B, 2 = R, 3 = B, 4 = B, 5 = R, 6 = R, 7 = B, 8 = R. (Checked by a script.)
