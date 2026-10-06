---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A bottom-up (LR) parser does not commit to a production until it has seen the entire body (the handle) on the stack, so a common prefix is no problem: for S -> abc | abd it shifts a and b with both items alive in the same state and decides at the next input symbol, while a top-down parser must choose a production before seeing the prefix."
sources: ["MMA syntax analysis slides 61-69, 152-226", "Dragon book 2e sec. 4.3.4, 4.5"]
---
**Reason.** A top-down parser must decide *at the beginning* which production of $A$ to apply, using only the lookahead. If two alternatives begin with the same prefix, that decision is impossible (hence left factoring defers the decision). A **bottom-up parser** decides **at the end**: it shifts the symbols of the input onto the stack and reduces only when a complete body (a handle) is on top. All productions that share a prefix are *simultaneously in progress* (they are different items of the same LR state), and the choice between them is made when the parser has seen the different parts, so the common prefix causes no conflict.

**Example.** Take $S \to abc \mid abd$ (common prefix $ab$).

- **Top-down (LL(1)):** on input `a` both $S \to abc$ and $S \to abd$ apply, so $M[S, a]$ has two entries: not LL(1) until the grammar is left-factored ($S \to abS'$, $S' \to c \mid d$).
- **Bottom-up (LR):** the LR(0) item sets are
  - $I_0 = \{S' \to \cdot S,\ S \to \cdot abc,\ S \to \cdot abd\}$;
  - after `a`: $I_2 = \{S \to a \cdot bc,\ S \to a \cdot bd\}$;
  - after `b`: $I_3 = \{S \to ab \cdot c,\ S \to ab \cdot d\}$;
  - after `c`: $I_4 = \{S \to abc \cdot\}$; after `d`: $I_5 = \{S \to abd \cdot\}$.

  The parser just shifts `a` and `b`; both productions are still possible in $I_3$; the next input symbol, `c` or `d`, selects the item, and it then reduces by the right production. The table has **no conflict**; for `abd` the parser makes: shift `a`, shift `b`, shift `d`, reduce $S \to abd$, accept.

So the grammar need not be left-factored for bottom-up parsing.

*Check:* the LL(1) table (two entries in $M[S, a]$) and the SLR table (no conflict, `abd` accepted) were computed by a script.
