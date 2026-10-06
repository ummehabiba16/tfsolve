---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) A -> B b q A' | c A'; A' -> a p A' | eps; B -> c A' y q B' | z B'; B' -> x p B' | b q A' y q B' | eps. (ii) T -> P Q; P -> R Q | q; R -> q Q p R'; R' -> Q Q p R' | eps; Q -> q."
sources: ["MMA syntax analysis slides 27-60 (Elimination of left recursion)", "Dragon book 2e Algorithm 4.19"]
---
Use Algorithm 4.19 with the given order of nonterminals.

**(i) $A \to Aap \mid Bbq \mid c$, $B \to Bxp \mid Ayq \mid z$** (order $A, B$).

$A$: immediate recursion with $\alpha = ap$ and $\beta \in \{Bbq, c\}$:

$$A \to Bbq\,A' \mid c\,A'$$

$$A' \to ap\,A' \mid \epsilon$$

$B$: substitute $A$ in $B \to Ayq$:

$$B \to Bxp \mid Bbq\,A'yq \mid c\,A'yq \mid z$$

Immediate recursion with $\alpha_1 = xp$, $\alpha_2 = bq\,A'yq$ and $\beta \in \{c\,A'yq, z\}$:

$$B \to c\,A'yq\,B' \mid z\,B'$$

$$B' \to xp\,B' \mid bq\,A'yq\,B' \mid \epsilon$$

**(ii) $T \to PQ$, $P \to RQ \mid q$, $R \to Tp$, $Q \to q$** (order $T, P, R, Q$).

$T \to PQ$: no recursion yet. $P \to RQ \mid q$: $R$ comes later in the order, nothing to substitute. $R \to Tp$: substitute $T$ ($T \to PQ$), then $P$ ($P \to RQ \mid q$):

$$R \to PQp \;\Rightarrow\; R \to RQQp \mid qQp$$

Immediate recursion with $\alpha = QQp$, $\beta = qQp$:

$$R \to qQp\,R'$$

$$R' \to QQp\,R' \mid \epsilon$$

$Q \to q$ has no recursion.

**Result.**

```text
(i)   A  -> B b q A' | c A'
      A' -> a p A' | eps
      B  -> c A' y q B' | z B'
      B' -> x p B' | b q A' y q B' | eps

(ii)  T  -> P Q
      P  -> R Q | q
      R  -> q Q p R'
      R' -> Q Q p R' | eps
      Q  -> q
```

*Check:* Algorithm 4.19 was run by a script on both grammars and produced exactly these productions.
