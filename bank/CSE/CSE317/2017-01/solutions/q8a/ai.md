---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Chronological backtracking returns to the most recently assigned variable on failure, even if that variable did not cause the conflict, so it thrashes repeating the same failure; e.g. Australia with the order Q, NSW, V, T, SA: Q=red, NSW=green, V=blue, T=red, then SA has no value, and backtracking changes T, which is irrelevant. Conflict-directed backjumping goes straight to a variable in SA's conflict set, here V."
sources: ["AIMA 3e sec. 6.3.3 (intelligent backtracking: looking backward)"]
---
**Chronological backtracking.** When a variable has no legal value left, plain backtracking search goes back to the **most recently assigned** variable and tries its next value, whether or not that variable has anything to do with the failure.

**Why it is suboptimal.** The real cause of the failure may be an assignment made much earlier. Changing irrelevant recent variables cannot fix it, so the search **thrashes**: it rediscovers the same dead end again and again, under different values of the irrelevant variables. That wastes exponential time.

**Example** (map of Australia, colours red, green, blue). Fixed variable order Q, NSW, V, T, SA:

1. $Q=$ red, $NSW=$ green, $V=$ blue, $T=$ red.
2. $SA$ is adjacent to Q, NSW and V, which already use all three colours, so $SA$ has **no consistent value**.
3. Chronological backtracking goes back to **T** (the most recent) and tries $T=$ green, then blue. But Tasmania is not connected to SA, so every value of T fails the same way. Only after exhausting T does it go back to V.

**Better: conflict-directed backjumping.** Keep a **conflict set** for each variable: the earlier assignments that removed its values. Here $conf(SA)=\{Q,NSW,V\}$. On failure, **jump back** to the most recent variable in the conflict set, **V**, skipping T. Forward checking plus backjumping (or conflict-directed backjumping with constraint learning) avoids the useless work.
