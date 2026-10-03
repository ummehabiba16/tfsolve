---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "No. Given M the path T -> M <- P -> C is active (M is an observed common effect), so T and C are dependent given M: P(c | t, m) = 0.843 but P(c | not t, m) = 0.876."
sources: ["MNM slides Uncertainty-3-BN-IND (d-separation, active triples)", "AIMA 4e sec. 13.2.1 (conditional independence in Bayes nets)"]
---
**Structure.** From the figure: $D \to P$, $P \to C$, $P \to M$, $T \to M$, so

$$P(D,T,P,M,C)=P(D)\,P(T)\,P(P\mid D)\,P(M\mid T,P)\,P(C\mid P).$$

**d-separation argument.** The only path between $T$ and $C$ is $T \to M \leftarrow P \to C$.

- $T \to M \leftarrow P$ is a *common-effect* (v-structure) triple. It is **active** when the middle node or one of its descendants is observed. Here $M$ is observed, so it is active.
- $M \leftarrow P \to C$: at $P$ the path is a *common-cause* triple ($M \leftarrow P \to C$). $P$ is not observed, so it is active.

Every triple on the path is active, so the path is active and $T$ and $C$ are **not** d-separated by $\{M\}$. Independence is therefore not guaranteed. The numbers below show that it actually fails.

(Without evidence the same path is blocked at the unobserved collider $M$, so $T \perp C$ marginally. Observing $M$ "explains away": if the terrain is easy but the rover cannot move, power is the likely cause, and power affects communication.)

**Mathematical validation.** First $P(p)=P(d)P(p\mid d)+P(\neg d)P(p\mid\neg d)=0.2(0.4)+0.8(0.9)=0.80$, so $P(\neg p)=0.20$. Summing out $D$ and $P$:

$$P(t,m,c)=P(t)\sum_{p}P(p)\,P(m\mid t,p)\,P(c\mid p)$$

$$=0.5\,[0.8(0.95)(0.9)+0.2(0.4)(0.3)]=0.5(0.684+0.024)=0.354$$

$$P(t,m)=0.5\,[0.8(0.95)+0.2(0.4)]=0.5(0.84)=0.42$$

$$P(\neg t,m,c)=0.5\,[0.8(0.6)(0.9)+0.2(0.1)(0.3)]=0.5(0.438)=0.219$$

$$P(\neg t,m)=0.5\,[0.8(0.6)+0.2(0.1)]=0.5(0.50)=0.25$$

Hence

$$P(c\mid t,m)=\frac{0.354}{0.42}=0.843,\qquad P(c\mid \neg t,m)=\frac{0.219}{0.25}=0.876.$$

With $P(m)=0.42+0.25=0.67$, $P(t\mid m)=0.42/0.67=0.627$ and $P(c\mid m)=0.573/0.67=0.855$:

$$P(t,c\mid m)=\frac{0.354}{0.67}=0.528\;\neq\;P(t\mid m)\,P(c\mid m)=0.627\times0.855=0.536.$$

The same holds for $M=\text{No}$: $P(c\mid t,\neg m)=0.45$ but $P(c\mid\neg t,\neg m)=0.684$.

**Conclusion.** **$T$ and $C$ are not conditionally independent given $M$** ($T \not\perp C \mid M$), although they are marginally independent.

*Note:* $P(P\mid D=\text{No})$ is taken as 0.9, the handwritten correction on the paper.
