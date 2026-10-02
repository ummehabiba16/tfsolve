---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Because an LR parser traces a rightmost derivation in reverse: if S' =>\\*rm alpha A w => alpha beta1 beta2 w, then with alpha beta1 on the stack the parser is inside a possible handle beta1 beta2 for A; it has seen beta1, expects beta2, and after reducing to A the next input will be FIRST(w) (the lookahead); w is all terminals since everything right of the handle is unread input. Hence the item correctly describes the stack, so it is valid."
sources: ["MMA syntax analysis slides 388-403 (Viable Prefixes), 407-440 (Canonical LR(1) Items)", "Dragon book 2e sec. 4.6.5, 4.7.1"]
---
The definition (with the lookahead written $a$) says $[A \to \beta_1 \cdot \beta_2, a]$ is valid for viable prefix $\alpha\beta_1$ if

$$S' \overset{*}{\underset{rm}{\Rightarrow}} \alpha A w \underset{rm}{\Rightarrow} \alpha\beta_1\beta_2 w$$

and $a$ is the first symbol of $w$ (or \$ if $w = \epsilon$). It is defined this way because of what an LR parser does:

1. **LR parsing is a rightmost derivation in reverse.** The stack plus the remaining input is always a right-sentential form, and reductions undo the derivation steps from last to first. So the item must be tied to a **rightmost** derivation.

2. **$\alpha\beta_1$ is what is on the stack.** In the right-sentential form $\alpha\beta_1\beta_2 w$, the substring $\beta_1\beta_2$ is the **handle** for $A$ (it is the last step of a rightmost derivation). When the parser has $\alpha\beta_1$ on the stack, it has recognised the first part $\beta_1$ of this handle, and $\beta_2$ is still expected. That is exactly what the dot in $A \to \beta_1 \cdot \beta_2$ records. This is why the prefix must be $\alpha\beta_1$ (a viable prefix: it does not go past the right end of the handle).

3. **$w$ consists only of terminals.** In a rightmost derivation, everything to the right of the nonterminal being expanded is already terminals. In parsing terms, $w$ is the part of the input not yet read.

4. **The lookahead is the first symbol of $w$.** After $\beta_2$ is completed and $\beta_1\beta_2$ is reduced to $A$, the next input symbol will be the first symbol of $w$. So:

- if $\beta_2 = \epsilon$ (item $[A \to \beta_1 \cdot, a]$), **reduce** by $A \to \beta_1$ only when the next input is $a$;
- if $\beta_2$ starts with a terminal $b$, **shift** $b$ (the lookahead $a$ is not used for shifting).

So "valid" means: the item correctly describes a situation the parser can really be in with $\alpha\beta_1$ on the stack, and its action is consistent with some rightmost derivation of the input. The set of items valid for a viable prefix $\gamma$ is exactly the state reached from $I_0$ on $\gamma$ in the LR(1) automaton.
