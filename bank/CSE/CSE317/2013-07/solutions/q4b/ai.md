---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Unification: finding a substitution theta that makes two atomic sentences identical, UNIFY(p, q) = theta with SUBST(theta, p) = SUBST(theta, q); the most general unifier is unique up to renaming, and the occurs check forbids binding x to a term containing x. Lifting lemma: if two ground instances of clauses have a resolvent, then the original first-order clauses have a resolvent (via the mgu) of which that ground resolvent is an instance; it lifts Herbrand's ground resolution completeness to first-order resolution."
sources: ["AIMA 3e sec. 9.2.2 (unification), 9.5.4 (completeness of resolution, lifting lemma)"]
---
**Unification** (5). The process of finding a **substitution** $\theta$ (variable to term bindings) that makes two logical expressions **identical**:

$$\text{UNIFY}(p,q)=\theta\quad\text{where}\quad\text{SUBST}(\theta,p)=\text{SUBST}(\theta,q).$$

*Examples:*

- $\text{UNIFY}(Knows(John,x),\ Knows(John,Jane))=\{x/Jane\}$
- $\text{UNIFY}(Knows(John,x),\ Knows(y,Mother(y)))=\{y/John,\ x/Mother(John)\}$
- $\text{UNIFY}(Knows(John,x),\ Knows(x,Elizabeth))$ = fail, unless the variables are standardized apart (e.g. $x_{17}$).

The algorithm returns the **most general unifier (MGU)**, which places the fewest restrictions on the variables and is unique up to renaming. The **occurs check** prevents binding a variable to a term that contains it ($x$ with $F(x)$ fails). Unification is the key step of generalized modus ponens and of first-order resolution.

**Lifting lemma** (5). Let $C_1$ and $C_2$ be first-order clauses with no shared variables, and let $C_1'$ and $C_2'$ be **ground instances** of them. If $C'$ is a resolvent of $C_1'$ and $C_2'$, then there is a clause $C$ such that

1. $C$ is a resolvent of $C_1$ and $C_2$ (obtained with their MGU), and
2. $C'$ is a ground instance of $C$.

In other words, any ground-level resolution step can be **"lifted"** to a first-order resolution step. Combined with Herbrand's theorem and the ground resolution theorem, it proves that first-order **resolution is refutation-complete**: if a set of clauses is unsatisfiable, resolution with unification derives the empty clause.
