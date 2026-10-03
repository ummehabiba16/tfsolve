---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "RBFS expands Root(500): best 551 (limit 565 = alternative); 551: best 558 (limit 562); 558's best child 586 > 562, so it unwinds with f(558) = 586; 562 (limit 565): its best child 592 > 565, so f(562) = 592; then 551's best is 586 > 565, so it unwinds with f(551) = 586; next 565 (limit 578, alternative 578): 568 (limit 571): child 569 is a goal within the limit, so the goal 569 is found (the cheapest of the three goals: 569 < 592 < 593)."
sources: ["AIMA 3e sec. 3.5.3 (RBFS)"]
---
**Notation.** Nodes are named by their $f$ values. Goals (boxed) are **593** (under 578, then 592), **592** (under 551, then 562) and **569** (under 565, then 568). Smaller $f$ is better. RBFS always explores the best child, as long as its $f$ is within the limit set by the best alternative elsewhere.

**Trace.**

| Step | Call | Children ($f$) | Action |
|:-:|:--|:--|:--|
| 1 | RBFS(500, limit $\infty$) | 578, 551, 565 | best **551**, alternative 565 |
| 2 | RBFS(551, limit 565) | 558, 562 | best **558**, alternative 562, so its limit is $\min(565,562)=562$ |
| 3 | RBFS(558, limit 562) | 591, 586, 601 | best child 586 > 562: **fail**, back up $f(558)=586$ |
| 4 | back in 551 | 558 (586), 562 | best **562**, alternative 586, so its limit is $\min(565,586)=565$ |
| 5 | RBFS(562, limit 565) | 592, 604, 820, 819 | best child 592 > 565: **fail**, back up $f(562)=592$ |
| 6 | back in 551 | 558 (586), 562 (592) | best 586 > 565: **fail**, back up $f(551)=586$ |
| 7 | back at root | 578, 551 (586), 565 | best **565**, alternative 578 |
| 8 | RBFS(565, limit 578) | 571, 568, 577 | best **568**, alternative 571, so its limit is 571 |
| 9 | RBFS(568, limit 571) | **569**, 579, 800 | best 569 $\le$ 571, so call RBFS(569) |
| 10 | RBFS(569) | | **goal test succeeds: return the goal 569** |

**Order of expansion:** 500, 551, 558, 562, 565, 568, then the goal 569 is selected.

**Why this order.** RBFS always works on the lowest-$f$ path. It abandons a subtree as soon as the subtree's best $f$ exceeds the best alternative ($f$-limit). It remembers the backed-up values (551's subtree is "worth" 586, more than 565), so it switches to 565's subtree. It never needed to expand 578 (its $f$ of 578 was never the lowest).

**Which goal is found and why.** **Goal 569** is found. It has the smallest $f$ of the three goals (569 < 592 < 593). RBFS, like A\*, explores paths in increasing order of $f$ (within its linear memory), so with admissible values it returns the cheapest goal. Goal 592 was seen (generated) at step 5, but its $f$ exceeded the limit 565, so it was not selected.
