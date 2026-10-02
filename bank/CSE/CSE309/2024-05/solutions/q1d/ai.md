---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Left factoring replaces A -> a b1 | a b2 by A -> a A', A' -> b1 | b2 with A' new; every derivation step A => a bi of the old grammar corresponds to A => a A' => a bi in the new one and vice versa (A' occurs nowhere else), so by induction both grammars derive the same terminal strings."
sources: ["MMA syntax analysis slides 61-69 (Left Factoring)", "Dragon book 2e sec. 4.3.4 (Algorithm 4.21)"]
---
**Transformation.** For the productions

$$A \to \alpha\beta_1 \mid \alpha\beta_2 \mid \ldots \mid \alpha\beta_n \mid \gamma$$

left factoring gives, with a **new** nonterminal $A'$,

$$A \to \alpha A' \mid \gamma$$

$$A' \to \beta_1 \mid \beta_2 \mid \ldots \mid \beta_n$$

All other productions are unchanged. Call the original grammar $G$ and the new one $G'$.

**Claim:** $L(G) = L(G')$.

**$L(G) \subseteq L(G')$.** Take any derivation in $G$. Every step that uses $A \to \alpha\beta_i$ can be replaced by the two steps

$$A \Rightarrow \alpha A' \Rightarrow \alpha\beta_i$$

in $G'$. Every other step uses a production present in both grammars. So every sentential form, and in particular every terminal string, derivable in $G$ is derivable in $G'$.

**$L(G') \subseteq L(G)$.** $A'$ is new: it appears only in the body of $A \to \alpha A'$. So in any derivation of a terminal string in $G'$, every occurrence of $A'$ was introduced by a step $A \Rightarrow \alpha A'$ and is later rewritten by some $A' \to \beta_i$. Derivation steps on different nonterminals are independent, so the two steps can be reordered to be adjacent and merged into one step $A \Rightarrow \alpha\beta_i$ of $G$. Doing this for every occurrence (induction on the number of $A'$ steps) turns the $G'$ derivation into a $G$ derivation of the same string.

Hence both grammars generate the same language. Only the *shape* of the parse trees changes: the choice among the $\beta_i$ is postponed until after $\alpha$ is read, which is exactly what a predictive parser needs.

**Example:** $S \to iEtS \mid iEtSeS \mid a$ becomes $S \to iEtSS' \mid a$, $S' \to eS \mid \epsilon$. The string $iEtSeS$ is derived as $S \Rightarrow iEtSS' \Rightarrow iEtSeS$ in the new grammar.
