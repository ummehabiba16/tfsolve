---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "M = sum_{i=1..k} C(n,i) 2^i = O((2n)^k) possible clauses, |H| = 2^M, ln|H| = O(n^k), so N >= (1/eps)(M ln 2 + ln(1/delta)) is polynomial; the elimination algorithm on the clauses finds a consistent k-CNF in O(N n^k) time, so k-CNF is efficiently PAC-learnable (k fixed)."
sources: ["MNM slides Learning-Theory-6-PAC-NEG-POS (3-CNF, k-CNF, k-term-DNF)", "AIMA 4e sec. 19.5", "Shalev-Shwartz & Ben-David, Understanding Machine Learning, ch. 3 and 8"]
---
**Size of the hypothesis space (15).** There are $n$ Boolean variables, so $2n$ literals. A clause is a disjunction of at most $k$ literals over **distinct** variables (a clause containing both $x$ and $\neg x$ is always true and adds nothing). Choose $i$ variables and a sign for each:

$$M=\text{number of possible clauses}=\sum_{i=1}^{k}\binom{n}{i}2^{i}\ \le\ (2n)^k=O\big((2n)^k\big).$$

(Checked by enumeration: $n=5$, $k=3$ gives $10+40+80=130$ clauses.)

A $k$-CNF is a conjunction of *any subset* of these $M$ clauses: each clause is either in the conjunction or not. So

$$|H_{k\text{-CNF}}|=2^{M}\le 2^{(2n)^k},\qquad \ln|H|=M\ln 2=O(n^k).$$

**Sample complexity.** Substituting into the PAC bound for a consistent learner:

$$N\ \ge\ \frac{1}{\epsilon}\left(\ln\frac1\delta+\ln|H|\right)=\frac{1}{\epsilon}\left(\ln\frac1\delta+\ln2\sum_{i=1}^{k}\binom{n}{i}2^{i}\right)=O\!\left(\frac{1}{\epsilon}\Big(n^k+\ln\frac1\delta\Big)\right).$$

For fixed $k$, this is **polynomial** in $n$, $1/\epsilon$ and $1/\delta$. (Compare all Boolean functions, where $\ln|H|=2^n\ln2$ is exponential.)

**Efficiency (5).** PAC-learnability also needs a polynomial-time algorithm that returns a consistent hypothesis. Treat each of the $M$ possible clauses $c_j$ as a new Boolean feature. A $k$-CNF is then a *monotone conjunction* of these features, and conjunctions are learned by the **elimination algorithm**:

```text
h <- c_1 AND c_2 AND ... AND c_M        (all possible clauses)
for each positive example x:
    remove from h every clause c_j with c_j(x) = false
return h
```

- *Consistent with the positives:* every remaining clause is true on every positive example.
- *Consistent with the negatives:* by realizability the target $f$ is a conjunction of some clauses. Each of them is true on all positives, so none is ever removed, and $h\Rightarrow f$. On a negative example $f(x)=0$, so some target clause is false, and $h(x)=0$.
- *Time:* $O(N\cdot M\cdot k)=O(N\,k\,(2n)^k)$, polynomial for fixed $k$.

Polynomial sample size plus a polynomial-time consistent learner means **$k$-CNF is efficiently PAC-learnable** (for constant $k$). This is also why $k$-term-DNF, which is NP-hard to learn properly, can be learned by using $k$-CNF as the hypothesis space.

*Note:* $|H|$ counts syntactically different conjunctions, so it is an upper bound on the number of distinct functions. An upper bound is all the PAC bound needs.
