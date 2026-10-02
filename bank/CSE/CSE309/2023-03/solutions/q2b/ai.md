---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "With stack s0 X1 s1 ... Xm sm and input ai ... an END, reduce A -> beta pops r = |beta| state/symbol pairs (the top r grammar symbols X(m-r+1)...Xm are exactly beta, the handle), then pushes A and s = GOTO[s(m-r), A], giving s0 X1 ... X(m-r) s(m-r) A s; the input is unchanged and the semantic action/production is output."
sources: ["MMA syntax analysis slides 307-353 (The LR-Parsing Algorithm, Behavior of the LR Parser)", "Dragon book 2e sec. 4.6.3"]
---
An LR parser configuration is

$$(s_0 X_1 s_1 X_2 s_2 \ldots X_m s_m,\ \ a_i a_{i+1} \ldots a_n \$)$$

The $X_j$ are grammar symbols; each state $s_j$ summarises the stack below it. (In practice only the states are kept, since each state implies its symbol.)

**Carrying out ACTION$[s_m, a_i]$ = reduce $A \to \beta$:**

1. Let $r = |\beta|$ (the length of the body).
2. **Pop** $r$ symbols and $r$ states (2r entries) from the stack. The state $s_{m-r}$ is now on top.
3. Find $s = \text{GOTO}[s_{m-r}, A]$.
4. **Push** $A$ and then $s$. The new configuration is

$$(s_0 X_1 s_1 \ldots X_{m-r} s_{m-r} A s,\ \ a_i a_{i+1} \ldots a_n \$)$$

5. The **input is not changed**: $a_i$ is still the current input symbol. The parser outputs the production $A \to \beta$ (or executes its semantic action).

**Relationship of $\beta$ with the stack.** The $r$ grammar symbols on top of the stack are exactly the body:

$$X_{m-r+1} \ldots X_m = \beta$$

$\beta$ is the **handle** of the current right-sentential form $X_1 \ldots X_m a_i \ldots a_n$, and it always appears on **top** of the stack, never inside. After the reduction, $X_1 \ldots X_{m-r} A\, a_i \ldots a_n$ is the previous right-sentential form in the rightmost derivation. For $A \to \epsilon$, $r = 0$: nothing is popped, and $A$ and GOTO$[s_m, A]$ are pushed.

**Example:** $T \to T * F$ with stack `0 T 2 * 7 F 10` and input `+ id $`: pop 6 entries to state 0, push $T$ and GOTO[0, T] = 2. The stack becomes `0 T 2`, with the input still `+ id $`.
