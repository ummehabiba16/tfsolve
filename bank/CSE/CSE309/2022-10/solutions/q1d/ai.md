---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "A postfix SDT is an SDT whose actions are all at the right end of the production bodies, so each action runs when its body is reduced. During LR parsing, the attribute values are kept on the parser stack next to the grammar symbols (states); on reducing A -> X Y Z the action reads the attributes at stack[top-2], stack[top-1], stack[top], computes A's attributes, pops the three entries and pushes A with them."
sources: ["KMS Chapter 5 slides 55-57 (Postfix SDT, Parser-Stack Implementation of Postfix SDT)", "Dragon book 2e sec. 5.4.1-5.4.2 (Figs. 5.19, 5.20)"]
---
**Definition.** A **postfix SDT** is an SDT in which **all actions are at the right ends** of the production bodies. Every S-attributed SDD on an LR grammar can be turned into one by writing each semantic rule as an action at the end of its production.

**Implementation during LR parsing.**

1. Each entry of the LR parser stack holds a state (grammar symbol) together with a field for the **attribute values** of that symbol (one value, or a pointer to a record of several).
2. Shift: push the new state, with the token's attribute from the lexer (e.g. `digit.lexval`).
3. Reduce by $A \to X\,Y\,Z$: the symbols of the body are on top of the stack (Z on top). Their attributes are at `stack[top-2]`, `stack[top-1]` and `stack[top]`. Execute the action, computing $A$'s synthesized attributes from these. Then pop the three entries and push the state for $A$ (from GOTO) with the computed attributes. Since every action is at the end of the body, it can always be executed at that reduction.

**Example** (desk calculator, with `top` the stack top):

| Production | Action on the stack |
|:--|:--|
| $L \to E\ \textbf{n}$ | `print(stack[top-1].val); top = top - 1;` |
| $E \to E_1 + T$ | `stack[top-2].val = stack[top-2].val + stack[top].val; top = top - 2;` |
| $T \to T_1 * F$ | `stack[top-2].val = stack[top-2].val * stack[top].val; top = top - 2;` |
| $F \to (E)$ | `stack[top-2].val = stack[top-1].val; top = top - 2;` |
| $E \to T$, $T \to F$, $F \to \textbf{digit}$ | no action needed: the value is already in place |

For `3 * 5 + 4 n`, the stack values become 3, 15, then 4 is shifted, and $15 + 4 = 19$ is printed.
