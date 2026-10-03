---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Let E_A, E_B, E_C = which prisoner is executed (1/3 each), and G_B = the guard says he told B. If A is executed the guard picks B or C at random: P(G_B | E_A) = 1/2; P(G_B | E_B) = 0; P(G_B | E_C) = 1. P(E_A | G_B) = (1/2)(1/3) / [(1/2)(1/3) + 0 + 1(1/3)] = 1/3. A's chance is unchanged at 1/3, and C's rises to 2/3."
sources: ["Pearl, Probabilistic Reasoning in Intelligent Systems, sec. 2.3.1"]
---
**Events.** $E_A$, $E_B$, $E_C$: prisoner A, B or C will be executed. The prior is $P(E_A)=P(E_B)=P(E_C)=\frac13$. $G_B$: the guard reports that he gave the pardon message to B.

**Likelihoods.** The guard never tells A about A, and never tells a prisoner who will be executed that he is pardoned.

- If A is to be executed, both B and C are pardoned, and the guard picks one at random: $P(G_B\mid E_A)=\frac12$.
- If B is to be executed, the guard cannot tell B he is pardoned: $P(G_B\mid E_B)=0$.
- If C is to be executed, B is the only other pardoned prisoner: $P(G_B\mid E_C)=1$.

**Bayes' rule.**

$$P(E_A\mid G_B)=\frac{P(G_B\mid E_A)P(E_A)}{P(G_B\mid E_A)P(E_A)+P(G_B\mid E_B)P(E_B)+P(G_B\mid E_C)P(E_C)}$$

$$=\frac{\frac12\cdot\frac13}{\frac12\cdot\frac13+0+1\cdot\frac13}=\frac{\frac16}{\frac12}=\mathbf{\frac13}.$$

**A's chance of being executed is still $\frac13$.** The guard's message gives A no information about himself: the guard could always name one of B or C. (By contrast, $P(E_C\mid G_B)=\frac{1/3}{1/2}=\frac23$: C should worry.)

*Note:* if the guard prefers to name B whenever he can (probability $q$ when A is to be executed), then $P(E_A\mid G_B)=\frac{q}{q+1}$. This equals $\frac13$ for a random guard ($q=\frac12$).
