---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) LL(1); (ii) not LL(1) (A -> B and A -> eps both derive eps, and M[B,b] has B -> b and B -> eps); (iii) not LL(1) (M[B,a] has B -> a and B -> eps); (iv) not LL(1) (C -> C E is left recursive, C has two eps derivations); (v) not LL(1) (S -> S(S) is left recursive)."
sources: ["MMA syntax analysis slides 103-123 (LL(1) grammars)", "Dragon book 2e sec. 4.4.3, Algorithm 4.31"]
---
A grammar is LL(1) iff for every pair of productions $A \to \alpha \mid \beta$: (1) $\text{FIRST}(\alpha) \cap \text{FIRST}(\beta) = \emptyset$; (2) at most one of $\alpha$, $\beta$ derives $\epsilon$; (3) if $\beta \Rightarrow^* \epsilon$ then $\text{FIRST}(\alpha) \cap \text{FOLLOW}(A) = \emptyset$ (and symmetrically). Equivalently, the predictive table has no multiply-defined entry.

**(i) $S \to ABc,\ A \to a \mid \epsilon,\ B \to b \mid \epsilon$ — LL(1).**

$\text{FIRST}(A) = \{a, \epsilon\}$, $\text{FIRST}(B) = \{b, \epsilon\}$, $\text{FIRST}(S) = \{a, b, c\}$. $\text{FOLLOW}(A) = \{b, c\}$, $\text{FOLLOW}(B) = \{c\}$. For $A$: $\text{FIRST}(a) = \{a\}$ and $\text{FOLLOW}(A) = \{b, c\}$ are disjoint. For $B$: $\{b\}$ and $\{c\}$ are disjoint. Every table entry has one production, so the grammar **is LL(1)**.

**(ii) $S \to ACB,\ A \to a \mid B \mid \epsilon,\ B \to b \mid \epsilon,\ C \to c \mid \epsilon$ — not LL(1).**

$A$ has two alternatives that both derive $\epsilon$ ($A \to B \Rightarrow \epsilon$ and $A \to \epsilon$): $\text{FIRST}(B) = \{b, \epsilon\}$ and $\text{FOLLOW}(A) = \{b, c, \$\}$, so $A \to B$ and $A \to \epsilon$ both go into $M[A, c]$ and $M[A, \$]$ (and $M[A, b]$ gets $A \to B$ twice, once through $b \in \text{FIRST}(B)$ and again through $\epsilon$). Also $B \to b$ and $B \to \epsilon$ collide in $M[B, b]$ because $b \in \text{FOLLOW}(B)$ (from $S \to ACB$ with $C \Rightarrow \epsilon$). The grammar is ambiguous (e.g. $b$ can come from $A$ or from $B$ in $S$), hence **not LL(1)**.

**(iii) $S \to X,\ X \to aXBA \mid bAXB \mid c,\ A \to a,\ B \to a \mid \epsilon$ — not LL(1).**

$\text{FOLLOW}(B) = \{a, \$\}$ (in $X \to aXBA$, $B$ is followed by $A$, and $\text{FIRST}(A) = \{a\}$; $B$ also ends $X \to bAXB$, so $\text{FOLLOW}(X) \subseteq \text{FOLLOW}(B)$). Since $a \in \text{FIRST}(B \to a)$ and $a \in \text{FOLLOW}(B)$ with $B \to \epsilon$, $M[B, a]$ contains **both** $B \to a$ and $B \to \epsilon$. **Not LL(1).**

**(iv) $A \to C \mid \epsilon,\ C \to CE,\ C \to \epsilon,\ E \to \epsilon$ — not LL(1).**

$C \to CE$ is **left recursive**, which no LL(1) grammar can contain. All of $A$'s and $C$'s alternatives derive only $\epsilon$: $\text{FIRST}(A) = \text{FIRST}(C) = \text{FIRST}(E) = \{\epsilon\}$ and $\text{FOLLOW}(A) = \text{FOLLOW}(C) = \text{FOLLOW}(E) = \{\$\}$, so $M[A, \$]$ has $A \to C$ and $A \to \epsilon$, and $M[C, \$]$ has $C \to CE$ and $C \to \epsilon$. **Not LL(1)** (the grammar is also ambiguous: $\epsilon$ has infinitely many derivations).

**(v) $S \to S(S) \mid \epsilon$ — not LL(1).**

Left recursion again: $\text{FIRST}(S(S)) = \{(\}$ and $\text{FOLLOW}(S) = \{\$, (, )\}$ both contain `(`, so $M[S, (]$ has $S \to S(S)$ **and** $S \to \epsilon$. **Not LL(1).**

*Check:* FIRST/FOLLOW sets and tables of all five grammars were computed by a script; only (i) has no multiply-defined entries.
