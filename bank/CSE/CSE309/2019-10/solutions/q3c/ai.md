---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) For LL(3): for distinct A -> alpha | beta, FIRST\\_3(alpha FOLLOW\\_3(A)) and FIRST\\_3(beta FOLLOW\\_3(A)) must be disjoint, i.e. no string of 3 terminals (or shorter, ending in end) can begin derivations from both; the alternatives may share prefixes of length 1 or 2. (ii) If beta =>\\* eps the parser picks A -> beta when the lookahead is in FOLLOW(A); if alpha could also start with that terminal, M[A,a] gets two entries, so FIRST(alpha) and FOLLOW(A) must be disjoint."
sources: ["MMA syntax analysis slides 103-111 (LL(1) Grammars)", "Dragon book 2e sec. 4.4.3"]
---
**(i) Condition for LL(3) (7 marks)**

For LL(1), the parser chooses between $A \to \alpha$ and $A \to \beta$ by **one** lookahead symbol, so no terminal $a$ may begin strings from both $\alpha$ and $\beta$.

For LL(3), the parser looks at the next **three** input symbols, so the condition is on strings of length 3: whenever $A \to \alpha \mid \beta$ are distinct productions,

$$\text{FIRST}_3(\alpha\,\text{FOLLOW}_3(A)) \cap \text{FIRST}_3(\beta\,\text{FOLLOW}_3(A)) = \emptyset$$

$\text{FIRST}_3(\gamma)$ is the set of first-3-terminal prefixes (or whole strings if shorter, padded with \$) of the strings derived from $\gamma$. In words: **for no string $x$ of three terminals do both $\alpha$ and $\beta$ (followed by what may follow $A$) derive strings beginning with $x$.**

The FOLLOW part is needed because when $\alpha$ derives fewer than 3 symbols, the remaining lookahead comes from what follows $A$ (for strong LL($k$), FOLLOW$_3(A)$).

**Example:** $S \to abc \mid abd$. The alternatives agree in the first two symbols, so the grammar is not LL(1) or LL(2). FIRST$_3$ = {abc} vs {abd} are disjoint, so it is LL(3).

**(ii) The FOLLOW condition (8 marks)**

**Statement:** if $\beta \overset{*}{\Rightarrow} \epsilon$, then $\alpha$ must not derive any string beginning with a terminal in FOLLOW($A$) (and symmetrically).

**Justification.** Suppose $A$ is on top of the stack (or the procedure for $A$ is called) and the lookahead is $a$.

- The parser may use $A \to \beta$ and let $\beta$ vanish. Then $a$ must be the symbol that **follows** $A$, so this choice is correct exactly when $a \in$ FOLLOW($A$). That is why $A \to \beta$ is entered in $M[A, a]$ for all $a \in$ FOLLOW($A$).
- The parser uses $A \to \alpha$ when $a \in$ FIRST($\alpha$).
- If some terminal $a$ is in both FIRST($\alpha$) and FOLLOW($A$), then on lookahead $a$ both choices are possible: $a$ could be the start of $\alpha$, or $A$ could be empty and $a$ comes after it. $M[A, a]$ gets two entries, and one symbol of lookahead cannot decide, so the grammar is not LL(1).

Together with the first condition (FIRST($\alpha$) $\cap$ FIRST($\beta$) $= \emptyset$, so at most one of them derives $\epsilon$), this guarantees that every cell of the table has at most one production.

**Example (dangling else):** $S' \to eS \mid \epsilon$ with $e \in$ FOLLOW($S'$). On `e`, either "this `else` belongs here" ($S' \to eS$) or "$S'$ is empty and the `else` belongs to an outer `if`" ($S' \to \epsilon$). The condition is violated, and the grammar is not LL(1).
