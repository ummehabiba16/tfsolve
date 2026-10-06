---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "If A -> aBg and eps is in FIRST(g), then g =>* eps, so A =>* aB; any terminal that can follow A in some sentential form can therefore directly follow B, hence FOLLOW(A) is a subset of FOLLOW(B). Example S -> Ac, A -> aBD, B -> b, D -> d | eps gives FOLLOW(A) = {c} inside FOLLOW(B) = {d, c}."
sources: ["MMA syntax analysis slides 76-102 (FIRST and FOLLOW)", "Dragon book 2e sec. 4.4.2 (rule 3 for FOLLOW)"]
---
**Claim.** If $A \to \alpha B\gamma$ is a production and $\epsilon \in \text{FIRST}(\gamma)$, then $\text{FOLLOW}(A) \subseteq \text{FOLLOW}(B)$.

**Justification.** $\epsilon \in \text{FIRST}(\gamma)$ means $\gamma \Rightarrow^* \epsilon$. Take any terminal (or \$) $a \in \text{FOLLOW}(A)$. By definition of FOLLOW there is a derivation

$$S \Rightarrow^* \delta A a \eta$$

Applying $A \to \alpha B \gamma$ and then $\gamma \Rightarrow^* \epsilon$:

$$S \Rightarrow^* \delta A a \eta \Rightarrow \delta \alpha B \gamma\, a \eta \Rightarrow^* \delta \alpha B\, a \eta$$

In the last sentential form $a$ appears **immediately to the right of $B$**, so $a \in \text{FOLLOW}(B)$. Since $a$ was arbitrary, everything in $\text{FOLLOW}(A)$ is in $\text{FOLLOW}(B)$. This is exactly rule 3 of the FOLLOW algorithm: *if $A \to \alpha B$, or $A \to \alpha B \beta$ with $\text{FIRST}(\beta)$ containing $\epsilon$, then everything in FOLLOW($A$) is in FOLLOW($B$)*.

**Example.**

$$S \to A\,c$$

$$A \to a\,B\,D$$

$$B \to b$$

$$D \to d \mid \epsilon$$

Here $A \to aBD$ with $\gamma = D$ and $\epsilon \in \text{FIRST}(D)=\{d,\epsilon\}$. $\text{FOLLOW}(A) = \{c\}$ (from $S \to Ac$). $\text{FOLLOW}(B)$ = $\text{FIRST}(D) \setminus \{\epsilon\}$ $\cup$ $\text{FOLLOW}(A)$ = $\{d\} \cup \{c\} = \{d, c\}$. So $c \in \text{FOLLOW}(A)$ is in $\text{FOLLOW}(B)$.

Concretely, $S \Rightarrow Ac \Rightarrow aBDc \Rightarrow aBc$ (using $D \to \epsilon$): the terminal $c$ appears right after $B$, which is why $M[B, c]$ must receive an $\epsilon$-production of $B$ if $B$ had one. If instead $\epsilon \notin \text{FIRST}(\gamma)$ (say $D \to d$ only), then $c$ could not follow $B$ and $\text{FOLLOW}(B)$ would be just $\{d\}$.
