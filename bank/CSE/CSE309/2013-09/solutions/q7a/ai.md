---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Nesting depth: 1 for the outermost procedure and one more for each level of nesting. When a procedure p of depth n_p calls q of depth n_q: if n_q = n_p + 1, q's access link points to p's frame; otherwise (n_q <= n_p) follow n_p - n_q + 1 access links from p's frame and use the frame reached, which is the frame of the procedure in which q is declared."
sources: ["KMS Chapter 7 slides 9-29 (nested procedures, access links)", "Dragon book 2e sec. 7.4.3-7.4.6"]
---
**Nesting depth** (Dragon book sec. 7.4.4). In a language with nested procedure declarations (Pascal, ML, nested functions), the **nesting depth** of a procedure is a number that grows with the nesting: the outermost (main) program has depth 1, and a procedure declared inside a procedure of depth $n$ has depth $n + 1$. The nesting depth of a name is the depth of the procedure in which it is declared, and the depth of a use of a name is the depth of the procedure in which it appears.

**Using it for access links.** Each activation record has an **access link** that points to the activation record of the procedure in which the called procedure is *declared* (its static parent). When a procedure $p$ (depth $n_p$) calls a procedure $q$ (depth $n_q$) the access link of the new frame of $q$ is set up using the depths (sec. 7.4.6):

1. **$n_q = n_p + 1$** (the callee is declared inside the caller): $q$'s access link points to the frame of $p$ itself.
2. **$n_q \le n_p$** (the callee is declared in an enclosing procedure of the caller, or is the caller itself or a sibling): follow the access links from the caller's frame **$n_p - n_q + 1$ times**; the frame reached is the frame of the procedure that encloses $q$, so $q$'s access link points to it.
3. **Recursion:** if $q = p$, then $n_q = n_p$ and one link is followed, so the new frame gets the same access link as the old one.

Non-local data is reached the same way: a variable declared at depth $d$ and used at depth $n_u$ is found by following $n_u - d$ access links from the current frame and then using the offset of the variable in that frame.

**Example.** $P$ (depth 1) declares $Q$ and $R$ (depth 2); $R$ declares $S$ and $T$ (depth 3). Call chain $P \to Q \to R \to S \to T$: $Q$: $n_q = n_p + 1$, link to $P$. $R$ called from $Q$ ($2 \le 2$): follow $2 - 2 + 1 = 1$ link from $Q$, giving $P$. $S$ called from $R$ ($3 = 2 + 1$): link to $R$. $T$ called from $S$ ($3 \le 3$): follow 1 link from $S$, giving $R$.
