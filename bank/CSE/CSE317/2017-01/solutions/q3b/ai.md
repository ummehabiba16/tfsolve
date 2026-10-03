---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Deduction theorem: for any sentences alpha and beta, alpha entails beta iff (alpha => beta) is valid. Completeness (ground resolution theorem): if a clause set S is unsatisfiable, then the resolution closure RC(S) contains the empty clause; proof by contrapositive, building a model of S from RC(S) when the empty clause is not in it."
sources: ["AIMA 3e sec. 7.5.1 (deduction theorem), sec. 7.5.2 (completeness of resolution)"]
---
**Deduction theorem.** For any sentences $\alpha$ and $\beta$:

$$\alpha\models\beta\quad\text{if and only if}\quad(\alpha\Rightarrow\beta)\text{ is valid}.$$

So entailment can be decided by checking validity, or (equivalently) by checking that $\alpha\land\neg\beta$ is unsatisfiable. Resolution refutation is based on this.

**Completeness of resolution (ground resolution theorem).** *If a set of clauses $S$ is unsatisfiable, then its resolution closure $RC(S)$ contains the empty clause.* $RC(S)$ is the set of all clauses derivable from $S$ by repeated resolution. It is finite, because only finitely many clauses can be built from the symbols $P_1,\dots,P_k$ of $S$, so PL-RESOLUTION always terminates.

*Proof* (by contrapositive): if the empty clause is **not** in $RC(S)$, we construct a model of $S$. Assign values to $P_1,\dots,P_k$ in order. For $i=1..k$:

- if some clause in $RC(S)$ contains $\neg P_i$, and all its other literals are false under the values already given to $P_1..P_{i-1}$, set $P_i=$ false;
- otherwise set $P_i=$ true.

*Claim:* this assignment satisfies every clause in $RC(S)$. Suppose not. At some step $i$, a clause $C$ became false for the first time, so all its literals are false and it contains $P_i$ or $\neg P_i$. If $C$ contained both, it would be true (a tautology), so it contains only one of them:

- If $C=\neg P_i\lor$ (false literals), the rule would have set $P_i=$ false, making $C$ true. Contradiction.
- So $C=P_i\lor$ (false literals), and $P_i$ was set false. That happened because some other clause $C'=\neg P_i\lor$ (false literals) is in $RC(S)$. But then the **resolvent** of $C$ and $C'$, which contains only literals over $P_1..P_{i-1}$ that are false, is also in $RC(S)$ (closure). It would already have been false before step $i$. This contradicts the choice of $i$ as the first step. (If that resolvent were empty, the empty clause would be in $RC(S)$, contrary to the assumption.)

So the assignment is a model of $RC(S)\supseteq S$, and $S$ is satisfiable. Hence **unsatisfiable $S$ implies that the empty clause is in $RC(S)$**. Resolution is refutation-complete: whenever $KB\models\alpha$, it derives the empty clause from $KB\land\neg\alpha$.
