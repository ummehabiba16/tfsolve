---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Chronological backtracking always returns to the most recently assigned variable, even if it has nothing to do with the failure, so it repeats the same failure many times (thrashing). Example: Australia colouring Q, NSW, V, T, SA: SA fails because of Q, NSW, V, but backtracking first tries all colours of T. Backjumping/conflict-directed backjumping fixes this."
sources: ["AIMA 3e sec. 6.3.3 (Intelligent backtracking: looking backward)"]
---
**Chronological backtracking.** When a variable has no consistent value, plain backtracking search goes back to the **most recently assigned** variable and tries its next value.

**Why it can be sub-optimal.** The most recent variable may have nothing to do with the failure. Changing it cannot fix the conflict, so the search tries all its values (and those of other irrelevant variables), re-discovering the same failure each time. This wasted work is called **thrashing**.

**Example (map colouring of Australia).** Variables are assigned in the fixed order Q, NSW, V, T, SA with colours {red, green, blue}:

- Q = red, NSW = green, V = blue, T = red.

- Now SA must differ from Q, NSW and V, which use all three colours: SA has no legal value.

- Chronological backtracking goes back to **T** (the last variable) and tries T = green, T = blue. Tasmania is not adjacent to anything, so these changes can never help; SA fails each time.

- Only after exhausting T does it go back to V, the actual culprit.

The relevant set of variables causing the failure (the **conflict set** of SA) is {Q, NSW, V}. **Backjumping** jumps directly back to the most recent variable in the conflict set (V) and skips T, avoiding the useless search. Conflict-directed backjumping and constraint learning (no-good recording) improve this further. In large problems, chronological backtracking can multiply the search time by the size of the irrelevant subtrees.
