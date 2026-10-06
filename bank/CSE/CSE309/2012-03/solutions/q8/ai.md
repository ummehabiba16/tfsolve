---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(a) not LL(1) (C -> CE is left recursive and A, C have several eps derivations); (b) not LL(1) (A and B both start with a; aaA | aa has a common prefix); (c) LL(1); (d) not LL(1) (A -> abc and A -> B -> acb both start with a, needs left factoring); (e) not LL(1) (A -> bcd and A -> B -> b both start with b, and B -> b / B -> eps)."
sources: ["MMA syntax analysis slides 103-123 (LL(1) grammars)", "Dragon book 2e sec. 4.4.3"]
---
Test: for each pair of alternatives $A \to \alpha \mid \beta$: $\text{FIRST}(\alpha) \cap \text{FIRST}(\beta) = \emptyset$; at most one derives $\epsilon$; and if $\beta \Rightarrow^* \epsilon$ then $\text{FIRST}(\alpha) \cap \text{FOLLOW}(A) = \emptyset$. Equivalently, no table entry has two productions.

**(a) $A \to C \mid \epsilon$, $C \to CE$, $C \to \epsilon$, $E \to \epsilon$: not LL(1).** $C \to CE$ is **left recursive**, which makes a grammar non-LL(1). Also every symbol derives only $\epsilon$: $\text{FIRST}(A) = \text{FIRST}(C) = \text{FIRST}(E) = \{\epsilon\}$ and all FOLLOW sets are $\{\$\}$, so $M[A, \$]$ has $A \to C$ and $A \to \epsilon$, and $M[C, \$]$ has $C \to CE$ and $C \to \epsilon$. The grammar is also ambiguous ($\epsilon$ has infinitely many derivations).

**(b) $S \to A \mid B$, $A \to aaA \mid aa$, $B \to aaB \mid a$: not LL(1).** $\text{FIRST}(A) = \text{FIRST}(B) = \{a\}$, so $M[S, a]$ contains $S \to A$ and $S \to B$. Inside $A$ the alternatives $aaA$ and $aa$ share the prefix $aa$ (not left-factored), so $M[A, a]$ has two entries; likewise $M[B, a]$ ($aaB$ and $a$).

**(c) $S \to AaAb \mid BbBa$, $A \to \epsilon$, $B \to \epsilon$: LL(1).** $\text{FIRST}(AaAb) = \{a\}$ and $\text{FIRST}(BbBa) = \{b\}$ are disjoint, and $A$ and $B$ each have a single production, so every table cell has at most one production: $M[S, a] = S \to AaAb$, $M[S, b] = S \to BbBa$, $M[A, a] = M[A, b] = A \to \epsilon$, $M[B, a] = M[B, b] = B \to \epsilon$.

**(d) $A \to abc \mid B$, $B \to acb$: not LL(1).** $\text{FIRST}(abc) = \{a\}$ and $\text{FIRST}(B) = \{a\}$ overlap, so $M[A, a]$ has $A \to abc$ and $A \to B$. (A common prefix $a$ once $B$ is substituted: left factoring, $A \to aA'$, $A' \to bc \mid cb$, would make it LL(1).)

**(e) $A \to bcd \mid B$, $B \to \epsilon$, $C \to DAbd$, $B \to b$, $C \to c$, $D \to d$: not LL(1).** Reading the productions as $A \to bcd \mid B$; $B \to \epsilon \mid b$; $C \to DAbd \mid c$; $D \to d$ (start symbol $A$): $\text{FIRST}(bcd) = \{b\}$ and $\text{FIRST}(B) = \{b, \epsilon\}$ overlap, so $M[A, b]$ has $A \to bcd$ and $A \to B$. Moreover, since $C \to DAbd$ makes $b \in \text{FOLLOW}(A)$ and $\text{FOLLOW}(B)$, $M[B, b]$ has both $B \to b$ and $B \to \epsilon$. ($C$ and $D$ are not reachable from $A$, but the conflict in $A$ exists in any case.)

| | LL(1)? | Reason |
|:-:|:-:|:--|
| (a) | no | left recursion; several $\epsilon$-derivations |
| (b) | no | $\text{FIRST}(A) \cap \text{FIRST}(B) = \{a\}$; common prefixes |
| (c) | **yes** | disjoint FIRST sets, single $\epsilon$-productions |
| (d) | no | $\text{FIRST}(abc) \cap \text{FIRST}(B) = \{a\}$ |
| (e) | no | $\text{FIRST}(bcd) \cap \text{FIRST}(B) = \{b\}$; $B \to b$ / $B \to \epsilon$ |

*Check:* FIRST, FOLLOW and the tables of the five grammars were computed by a script; only (c) has no multiply-defined entries.
