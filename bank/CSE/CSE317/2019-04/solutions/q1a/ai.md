---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A model assigns true or false to every symbol (a possible world); m satisfies alpha if alpha is true in m. KB entails alpha iff alpha is true in every model of KB (M(KB) is a subset of M(alpha)). A Horn clause is a disjunction with at most one positive literal, e.g. not P or not Q or R, i.e. P and Q => R."
sources: ["AIMA 4e sec. 7.3 (entailment, models), sec. 7.4 and 7.5.3 (Horn clauses)"]
---
**Model.** In propositional logic a *model* is a possible world: an assignment of *true* or *false* to every proposition symbol. With $n$ symbols there are $2^n$ models. A model $m$ **satisfies** a sentence $\alpha$ (written $m$ is a model of $\alpha$) if $\alpha$ is true in $m$. $M(\alpha)$ is the set of all models of $\alpha$.

*Example:* symbols $P$ (it rains) and $Q$ (the road is wet). The model $\{P=\text{T},Q=\text{T}\}$ satisfies $P\Rightarrow Q$; the model $\{P=\text{T},Q=\text{F}\}$ does not.

**Entailment.** $KB\models\alpha$ ("KB entails $\alpha$") iff $\alpha$ is true in **every** model in which $KB$ is true:

$$KB\models\alpha\iff M(KB)\subseteq M(\alpha).$$

*Example:* $KB=\{P,\ P\Rightarrow Q\}$ has the single model $\{P=\text{T},Q=\text{T}\}$, in which $Q$ is true, so $KB\models Q$. But $KB'=\{P\Rightarrow Q\}\not\models Q$, because the model $\{P=\text{F},Q=\text{F}\}$ satisfies $KB'$ but not $Q$.

(In the Wumpus world: after perceiving no breeze in [1,1], $KB\models\neg P_{1,2}$, since in every model consistent with the percepts there is no pit in [1,2].)

**Horn clause.** A disjunction of literals with **at most one positive** literal, for example $\neg P\lor\neg Q\lor R$, equivalent to $(P\land Q)\Rightarrow R$.

- *Definite clause:* exactly one positive literal (a rule or a fact, e.g. $L_{1,1}\land Breeze\Rightarrow B_{1,1}$, or $W$).
- *Goal clause:* no positive literal (e.g. $\neg P\lor\neg Q$).

Horn clauses matter because entailment for them can be decided in **linear time** by forward or backward chaining.
