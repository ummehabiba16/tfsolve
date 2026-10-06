---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Four strategies: ignore the problem, detect and recover, dynamically avoid, prevent; the ostrich algorithm is the most popular because deadlocks are rare and the other methods are costly or restrictive."
sources: ["Tanenbaum MOS 4e, sec. 6.1-6.7 (deadlock strategies, ostrich algorithm)"]
---
**The four strategies** (Tanenbaum):

1. **Ignore the problem** (the ostrich algorithm).
2. **Detection and recovery:** let deadlocks occur, detect them and recover.
3. **Dynamic avoidance** by careful resource allocation (Banker's algorithm, safe states).
4. **Prevention:** structurally negate one of the four necessary conditions.

**Most popular: the ostrich algorithm** (used by UNIX, Linux, Windows). *Why:*

- Deadlocks are **rare** (compare the frequency of crashes caused by other bugs), so the cost of preventing them is not justified.
- Prevention puts **restrictions on users** (e.g. request everything at once, resource ordering) and lowers resource utilisation; avoidance needs the maximum needs in advance and is expensive; detection costs overhead and recovery is crude.
- There is a trade-off between **convenience and correctness**: most users prefer a rare reboot to constant restrictions.
