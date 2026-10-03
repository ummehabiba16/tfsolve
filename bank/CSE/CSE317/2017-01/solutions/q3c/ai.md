---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "FOL entailment is semidecidable (Turing, Church; Goedel's completeness): a complete procedure such as resolution will find a proof whenever KB entails alpha, but with function symbols the Herbrand universe is infinite, so when the sentence is not entailed the search may never terminate; no algorithm says no for every non-entailed sentence. Propositional forward chaining is sound (every step is Modus Ponens) and complete for definite clauses (at the fixed point, the inferred atoms form a model of the KB, so every entailed atom has been inferred)."
sources: ["AIMA 3e sec. 9.4-9.5 (semidecidability), sec. 7.5.4 (forward chaining soundness and completeness)"]
---
**Why first-order entailment is semi-decidable (8).**

- *Positive side:* Goedel's completeness theorem guarantees that every entailed sentence has a finite proof, and resolution is refutation-complete (Herbrand's theorem plus the lifting lemma). Enumerating all proofs in a fair order therefore **will find a proof whenever $KB\models\alpha$**.
- *Negative side:* with function symbols (and equality), the Herbrand universe is **infinite**: $John$, $Father(John)$, $Father(Father(John))$, and so on. If $KB\not\models\alpha$, the procedure may keep generating new ground instances and new resolvents forever, never knowing whether one more step would give a proof.
- Turing (1936) and Church (1936) showed that this is unavoidable: there is no algorithm that says **yes** for every entailed sentence and **no** for every non-entailed one (a reduction from the halting problem).

So entailment is **semi-decidable**: there are algorithms that say yes to every entailed sentence, but none that also says no to every non-entailed one. Contrast this with propositional logic, which is decidable (finitely many models), and with Datalog (no function symbols), where forward chaining terminates.

**Propositional forward chaining is sound and complete (9).** Forward chaining for a KB of definite clauses: repeatedly fire every rule $p_1\land\dots\land p_n\Rightarrow q$ whose premises are all known, adding $q$, until the query is added or nothing new can be inferred.

- **Soundness:** each inference step is an application of Modus Ponens, $\frac{p_1,\dots,p_n,\ p_1\land\dots\land p_n\Rightarrow q}{q}$, which is sound: in every model where the premises are true, $q$ is true. By induction, every inferred atom is entailed.
- **Completeness** (every entailed atomic sentence is derived):

1. Forward chaining reaches a **fixed point** after at most $n$ iterations ($n$ = number of symbols), where no new atom can be inferred.
2. Consider the model $m$ that makes every inferred atom true and every other atom false.
3. Every definite clause $p_1\land\dots\land p_k\Rightarrow q$ of the KB is true in $m$. If it were false, its premises would all be true in $m$ (all inferred) and $q$ false (not inferred). But then the rule could fire, contradicting the fixed point.
4. So $m$ is a model of the KB. If $KB\models q$, then $q$ is true in $m$, so $q$ was inferred.

Hence forward chaining derives exactly the atoms entailed by the KB.
