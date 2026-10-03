---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Clauses: P or R; not R or Q; not P or T; not S; not T or S; plus the negated query not Q. Iteration 1 adds not R, not T, P or Q, R or T, S or not P. Iteration 2 adds P, R, T, not P, Q or S, Q or T, R or S. Iteration 3 derives Q, S and the empty clause, so the KB entails Q."
sources: ["AIMA 3e sec. 7.5.2 (PL-RESOLUTION, Fig. 7.12)"]
---
**CNF clauses.** $R\Rightarrow Q$ becomes $\neg R\lor Q$; $P\Rightarrow T$ becomes $\neg P\lor T$; $T\Rightarrow S$ becomes $\neg T\lor S$. PL-RESOLUTION adds the **negated query** $\neg Q$:

| # | Clause |
|:-:|:--|
| C1 | $P\lor R$ |
| C2 | $\neg R\lor Q$ |
| C3 | $\neg P\lor T$ |
| C4 | $\neg S$ |
| C5 | $\neg T\lor S$ |
| C6 | $\neg Q$ |

PL-RESOLUTION resolves **every pair** of clauses in the current set. If the empty clause appears, it returns true. If no new clause appears, it returns false. Tautologies are discarded.

**Iteration 1** (new clauses from pairs of C1-C6):

| New clause | From |
|:--|:--|
| $\neg R$ | C2, C6 |
| $\neg T$ | C4, C5 |
| $P\lor Q$ | C1, C2 |
| $R\lor T$ | C1, C3 |
| $\neg P\lor S$ | C3, C5 |

**Iteration 2** (pairs of the enlarged set):

| New clause | From |
|:--|:--|
| $P$ | C1, $\neg R$ |
| $R$ | $R\lor T$, $\neg T$ |
| $T$ | $R\lor T$, $\neg R$ |
| $\neg P$ | C3, $\neg T$ (or C4, $\neg P\lor S$) |
| $Q\lor S$ | $P\lor Q$, $\neg P\lor S$ |
| $Q\lor T$ | $P\lor Q$, C3 |
| $R\lor S$ | $R\lor T$, C5 |

**Iteration 3:**

| New clause | From |
|:--|:--|
| $Q$ | C2, $R$ |
| $S$ | C5, $T$ |
| **$\square$ (empty)** | $P$, $\neg P$ (also $R$, $\neg R$ and others) |

The empty clause is derived, so $KB\land\neg Q$ is unsatisfiable. **The KB entails $Q$.**

(A short proof: from C3, C5 and C4 we get $\neg P$; with C1, $R$; with C2, $Q$; with C6, the empty clause.)
