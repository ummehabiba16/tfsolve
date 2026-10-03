---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "BFS over DFS: complete (when b is finite) and optimal for unit step costs, so it finds the shallowest solution; it never gets lost in infinite or deep branches. DFS over BFS: memory O(bm) instead of O(b^d), so it is feasible on large problems, and it can find a deep solution quickly if it is lucky."
sources: ["AIMA 3e sec. 3.4.1, 3.4.3, Fig. 3.21"]
---
**Advantages of BFS over DFS.**

- **Complete:** it finds a solution if one exists (with a finite branching factor), even in infinite state spaces. DFS can follow an infinite or very deep branch forever.
- **Optimal** when all step costs are equal: it finds the **shallowest** goal first. DFS returns the first goal it happens to reach, which may be very deep or costly.
- It is not affected by the order of the successors (no "bad luck").

**Advantages of DFS over BFS.**

- **Memory:** DFS stores only the current path plus the unexpanded siblings, $O(bm)$, which is **linear**. BFS must store the whole frontier, $O(b^d)$, which is **exponential**. Memory is usually BFS's limiting factor (for example $b=10$, $d=12$ needs about 10 TB).
- If there are many solutions, or they are deep, DFS may find one **quickly** without exploring all the shallower levels.
- Backtracking variants need even less memory, $O(m)$.
