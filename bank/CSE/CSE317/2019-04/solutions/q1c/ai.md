---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Valid (tautology): true in all models; satisfiable: true in some model. alpha is valid iff not alpha is unsatisfiable; alpha is satisfiable iff not alpha is not valid. Hence KB entails alpha iff (KB and not alpha) is unsatisfiable, which is the basis of proof by contradiction and resolution."
sources: ["AIMA 4e sec. 7.5.1 (validity and satisfiability)"]
---
**Validity.** A sentence is **valid** (a tautology) if it is true in **all** models. Examples: $P\lor\neg P$ and $(P\land(P\Rightarrow Q))\Rightarrow Q$.

**Satisfiability.** A sentence is **satisfiable** if it is true in **at least one** model; that model satisfies it. Example: $P\land\neg Q$ is satisfiable (by $P=\text{T}$, $Q=\text{F}$) but not valid. $P\land\neg P$ is **unsatisfiable**: true in no model.

**How they are related.**

- $\alpha$ is valid iff $\neg\alpha$ is unsatisfiable.
- $\alpha$ is satisfiable iff $\neg\alpha$ is not valid.

Both follow because $\neg\alpha$ is true exactly in the models where $\alpha$ is false.

**Connection to inference.**

- *Deduction theorem:* $KB\models\alpha$ iff $(KB\Rightarrow\alpha)$ is valid.
- Combining it with the first relation: $KB\models\alpha$ iff $(KB\land\neg\alpha)$ is **unsatisfiable**.

This is **proof by contradiction (refutation)**: assume $\neg\alpha$ and show that no model satisfies $KB\land\neg\alpha$. Resolution and DPLL work this way. So an algorithm that tests satisfiability (a SAT solver) also decides entailment and validity.
