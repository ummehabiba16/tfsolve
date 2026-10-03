---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Unit clause: one literal. Full resolution: (l1 or ... or lk) and (m1 or ... or mn) with li = not mj gives the clause of all the other literals. Sound: any model satisfying both premises satisfies the resolvent. CNF steps: eliminate <=>, eliminate =>, move not inwards, distribute or over and. Half adder (S = A xor B, C = A and B): (not C or A)(not C or B)(not A or not B or C)(not S or A or B)(not S or not A or not B)(S or not A or B)(S or A or not B)."
sources: ["AIMA 4e sec. 7.5.2 (resolution, conversion to CNF)", "AIMA 4e sec. 7.6 (circuits)"]
---
**Unit clause.** A clause with exactly one literal, e.g. $P$ or $\neg Q$. *Unit resolution*: from $l_1\lor\dots\lor l_k$ and $m$, where $l_i$ and $m$ are complementary, infer $l_1\lor\dots\lor l_{i-1}\lor l_{i+1}\lor\dots\lor l_k$.

**Full resolution rule.** If $l_i$ and $m_j$ are complementary literals:

$$\frac{l_1\lor\dots\lor l_k,\qquad m_1\lor\dots\lor m_n}{l_1\lor\dots\lor l_{i-1}\lor l_{i+1}\lor\dots\lor l_k\lor m_1\lor\dots\lor m_{j-1}\lor m_{j+1}\lor\dots\lor m_n}$$

The resulting clause keeps only one copy of each literal (factoring).

**Soundness.** Take any model $m$ in which both premises are true, and look at $l_i$ (so $m_j=\neg l_i$).

- If $l_i$ is true in $m$, then $m_j$ is false. The second clause is true, so some other $m$-literal is true, and that literal is in the resolvent.
- If $l_i$ is false in $m$, the first clause is true, so some other $l$-literal is true, and it is in the resolvent.

Either way the resolvent is true in $m$. So every model of the premises is a model of the conclusion: the rule is **sound**.

**Converting to CNF.**

1. Eliminate $\Leftrightarrow$: $\alpha\Leftrightarrow\beta\ \to\ (\alpha\Rightarrow\beta)\land(\beta\Rightarrow\alpha)$.
2. Eliminate $\Rightarrow$: $\alpha\Rightarrow\beta\ \to\ \neg\alpha\lor\beta$.
3. Move $\neg$ inwards: $\neg\neg\alpha\to\alpha$; De Morgan: $\neg(\alpha\land\beta)\to\neg\alpha\lor\neg\beta$, and $\neg(\alpha\lor\beta)\to\neg\alpha\land\neg\beta$.
4. Distribute $\lor$ over $\land$: $\alpha\lor(\beta\land\gamma)\to(\alpha\lor\beta)\land(\alpha\lor\gamma)$.

**Half adder.** Inputs $A,B$; outputs Sum $S=A\oplus B$ and Carry $C=A\land B$.

*Carry:* $C\Leftrightarrow(A\land B)$ becomes $(\neg C\lor(A\land B))\land(\neg(A\land B)\lor C)$, which gives

$$(\neg C\lor A)\land(\neg C\lor B)\land(\neg A\lor\neg B\lor C).$$

*Sum:* $S\Leftrightarrow(A\oplus B)$, with $A\oplus B\equiv(A\lor B)\land(\neg A\lor\neg B)$:

- $S\Rightarrow A\oplus B$ gives $(\neg S\lor A\lor B)\land(\neg S\lor\neg A\lor\neg B)$.
- $A\oplus B\Rightarrow S$ gives $\neg((A\lor B)\land(\neg A\lor\neg B))\lor S=(\neg A\land\neg B)\lor(A\land B)\lor S$, which distributes to $(S\lor\neg A\lor B)\land(S\lor A\lor\neg B)$, after dropping the tautological clauses.

**Half adder in CNF:**

$$(\neg C\lor A)\land(\neg C\lor B)\land(\neg A\lor\neg B\lor C)\land(\neg S\lor A\lor B)\land(\neg S\lor\neg A\lor\neg B)\land(S\lor\neg A\lor B)\land(S\lor A\lor\neg B)$$

(Checked by truth table: these 7 clauses are true exactly when $S=A\oplus B$ and $C=A\land B$.)
