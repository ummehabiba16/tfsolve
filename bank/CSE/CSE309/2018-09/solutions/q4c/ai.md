---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "If beta =>\\* eps, A -> beta is put in M[A,a] for every a in FOLLOW(A) (A vanishes and a follows it); if alpha can also begin with such an a, then M[A,a] also gets A -> alpha, so with lookahead a the parser cannot decide whether to expand A by alpha or erase it: two entries, not LL(1). Example: S -> A b, A -> b | eps: FOLLOW(A) = {b} and FIRST(b) = {b}, so M[A,b] = {A -> b, A -> eps}."
sources: ["MMA syntax analysis slides 103-123 (LL(1) Grammars, A Case of a non-LL(1) Grammar)", "Dragon book 2e sec. 4.4.3"]
---
**Why the condition is needed.** An LL(1) parser with nonterminal $A$ on top of the stack and lookahead $a$ must choose **one** of $A$'s productions using only $a$.

- If $\beta \overset{*}{\Rightarrow} \epsilon$, using $A \to \beta$ may make $A$ derive nothing. Then the current input symbol $a$ must be the symbol that **follows** $A$. So $A \to \beta$ is the right choice for every $a \in$ FOLLOW($A$), and Algorithm 4.31 enters it in $M[A, a]$ for all $a \in$ FOLLOW($A$).
- $A \to \alpha$ is the right choice for every $a \in$ FIRST($\alpha$).
- If some terminal $a$ is in both FOLLOW($A$) and FIRST($\alpha$), then on seeing $a$ the parser cannot tell whether $a$ **starts $\alpha$** or **comes after an empty $A$**. $M[A, a]$ gets both productions. One lookahead symbol is not enough, so the grammar is not LL(1).

The symmetric statement (with $\alpha \overset{*}{\Rightarrow} \epsilon$) is the same argument with $\alpha$ and $\beta$ exchanged. Together with "FIRST($\alpha$) and FIRST($\beta$) are disjoint" (which also means at most one of them derives $\epsilon$), it ensures each table cell has at most one entry.

**Example 1:**

$$S \to Ab, \qquad A \to b \mid \epsilon$$

FIRST($b$) = {b} and FOLLOW($A$) = {b}. For input `b`: if $A \to b$, the parser then needs another `b` for $S \to Ab$, which fails. The correct choice is $A \to \epsilon$. For input `bb`, the correct choice is $A \to b$. In both cases the lookahead is `b`, so $M[A, b] = \{A \to b,\ A \to \epsilon\}$. Not LL(1).

**Example 2 (dangling else):**

$$S \to iEtSS' \mid a, \qquad S' \to eS \mid \epsilon, \qquad E \to b$$

$e \in$ FIRST($eS$) and $e \in$ FOLLOW($S'$) (an `else` may belong to an outer `if`). So $M[S', e] = \{S' \to eS,\ S' \to \epsilon\}$: the grammar is not LL(1). (The conflict is resolved in practice by choosing $S' \to eS$.)

**Contrast (condition holds):** $E' \to +TE' \mid \epsilon$ with FOLLOW($E'$) = { ), \$ } and FIRST($+TE'$) = {+}: disjoint, so the choice is always clear.
