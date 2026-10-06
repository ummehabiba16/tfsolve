---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Popping X and pushing Yk...Y1 (Y1 on top) replaces X in the left-sentential form by the body, with Y1 leftmost; since the stack (top to bottom) after the matched input is always the unexpanded part of the sentential form and X is its leftmost symbol, each output step is exactly one leftmost-derivation step X => Y1...Yk, and the outputs in order form the leftmost derivation."
sources: ["MMA syntax analysis slides 124-151 (Nonrecursive Predictive Parsing)", "Dragon book 2e sec. 4.4.4 (Algorithm 4.34, Fig. 4.21)"]
changes:
  - "2026-10-06: added TikZ figure (figures/model.png) for the parser model; the answer itself is unchanged."
---
**Model of the parser.** The table-driven predictive parser has an input buffer ($w$ followed by \$), a stack (initially $S$ on top of \$), the table $M$, and an output.

![Model of a table-driven predictive parser](figures/model.png)

**Invariant.** At every step,

$$(\text{input matched so far})\ \cdot\ (\text{stack contents, top to bottom, without } \$)$$

is a **left-sentential form**, i.e. a sentential form of a leftmost derivation: $S \underset{lm}{\overset{*}{\Rightarrow}} w_{matched}\,\alpha$.

```text
   matched input        stack (top at left)
   ---------------      ------------------------
       x1 x2 ... xi     X  Z1 Z2 ... Zp  $
   \______________/\___________________/
       terminals        rest of the sentential form
                        (X = leftmost unexpanded symbol)
```

**Why the three actions are one leftmost-derivation step.** Let the left-sentential form be $w_m X \gamma$, with $X$ a nonterminal on top of the stack.

1. **Output $X \to Y_1 Y_2 \ldots Y_k$.** $X$ is the leftmost nonterminal of the form: everything before it ($w_m$) is matched terminals, so $X$ is exactly what a leftmost derivation must expand next. The table entry $M[X, a]$ chooses the production using the lookahead $a$.
2. **Pop $X$.** Removes $X$ from the form.
3. **Push $Y_k, \ldots, Y_1$ with $Y_1$ on top.** The body takes $X$'s place **in the same order**, because the top of the stack represents the left end. The form becomes

$$w_m\, Y_1 Y_2 \ldots Y_k\, \gamma$$

which is precisely the step $w_m X \gamma \underset{lm}{\Rightarrow} w_m Y_1 \ldots Y_k \gamma$.

When a terminal is on top and equals the input symbol, it is matched (moved to the matched part); the sentential form does not change. Pushing in reverse order is essential: $Y_1$ must be expanded or matched first, because it is the leftmost symbol and corresponds to the next input.

**Example** ($E \to TE'$, $E' \to +TE' \mid \epsilon$, $T \to \textbf{id}$, input `id + id`):

| Matched | Stack | Input | Action | Left-sentential form |
|:--|:--|--:|:--|:--|
| | $E$\$ | id+id\$ | output $E \to TE'$ | $E$ |
| | $TE'$\$ | id+id\$ | output $T \to \textbf{id}$ | $TE'$ |
| | id $E'$\$ | id+id\$ | match id | id $E'$ |
| id | $E'$\$ | +id\$ | output $E' \to +TE'$ | id $E'$ |
| id | $+TE'$\$ | +id\$ | match + | id $+TE'$ |
| id+ | $TE'$\$ | id\$ | output $T \to \textbf{id}$ | id $+TE'$ |
| id+ | id $E'$\$ | id\$ | match id | id + id $E'$ |
| id+id | $E'$\$ | \$ | output $E' \to \epsilon$ | id + id $E'$ |
| id+id | \$ | \$ | accept | id + id |

The outputs, in order, are the leftmost derivation

$$E \Rightarrow TE' \Rightarrow \textbf{id}E' \Rightarrow \textbf{id}+TE' \Rightarrow \textbf{id}+\textbf{id}E' \Rightarrow \textbf{id}+\textbf{id}$$
