---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "M[A,a] = A -> eps means a is in FOLLOW(A): the parser pops A from the stack, pushes nothing (A derives the empty string here), outputs A -> eps, and does not advance the input; then the symbol below A is matched against a."
sources: ["MMA syntax analysis slides 112-151 (Predictive Parsing Table, Nonrecursive Predictive Parsing)", "Dragon book 2e sec. 4.4.3-4.4.4"]
---
**Why the entry is there:** $A \to \epsilon$ is placed in $M[A, a]$ for every $a \in$ FOLLOW($A$) (Algorithm 4.31). So the entry means: "with $A$ on top of the stack and $a$ as the next input, $A$ must derive the empty string, because $a$ is something that can come *after* $A$."

**What the parser does** when $X = A$ is on top of the stack and $M[A, a] = A \to \epsilon$:

1. **Output** the production $A \to \epsilon$ (one step of the leftmost derivation).
2. **Pop** $A$ from the stack.
3. **Push nothing**: the body is empty.
4. **Do not advance** the input; $a$ is still the lookahead.

The next symbol on the stack (which came after $A$ in the sentential form) is now on top. It is then matched against or expanded with $a$.

**Example** ($E \to TE'$, $E' \to +TE' \mid \epsilon$, $T \to \textbf{id}$), input `id $`:

| Matched | Stack | Input | Action |
|:--|:--|--:|:--|
| | $E$ \$ | id \$ | output $E \to TE'$ |
| | $TE'$ \$ | id \$ | output $T \to \textbf{id}$ |
| | id $E'$ \$ | id \$ | match id |
| id | $E'$ \$ | \$ | output $E' \to \epsilon$: pop $E'$, push nothing |
| id | \$ | \$ | accept |

Here \$ $\in$ FOLLOW($E'$), so $M[E', \$] = E' \to \epsilon$ and the parser erases $E'$.
