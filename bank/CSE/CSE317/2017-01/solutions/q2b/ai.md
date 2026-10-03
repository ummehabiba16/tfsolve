---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A model of FOL = a non-empty domain of objects plus an interpretation of the constant, predicate and function symbols. (i) exists x,y x = y is valid: every model has at least one object o, and x = y = o makes it true. (ii) forall x,y x = y is satisfiable (true in any model with exactly one object) but not valid (false when the domain has 2 or more objects)."
sources: ["AIMA 3e sec. 8.2.2 (models for FOL), sec. 8.2.7 (equality)"]
---
**Model of a first-order language.** A model is

1. a **non-empty domain** $D$ of objects, and
2. an **interpretation** mapping each constant symbol to an object in $D$, each predicate symbol to a relation on $D$ (a set of tuples), and each function symbol to a (total) function on $D$.

A sentence is *true in a model* according to the usual semantics. $\forall x\,\phi$ is true if $\phi$ holds for every object assigned to $x$, and $\exists x\,\phi$ if for at least one. A sentence is **valid** if it is true in all models, and **satisfiable** if it is true in some model. The equality symbol always means identity.

**(i) $\exists x,y\ x=y$: TRUE (valid).** Every model has at least one object $o$ (the domain is non-empty). Assign $x=o$ and $y=o$; then $x=y$ holds. So the sentence is true in **every** model: it is valid, and hence also satisfiable.

**(ii) $\forall x,y\ x=y$: satisfiable (TRUE), but not valid.** The sentence says the domain contains **exactly one** object. In a model with $D=\{o\}$, every pair $(x,y)$ is $(o,o)$, and $x=y$ holds, so it is satisfiable. In any model with two distinct objects $a\neq b$, the assignment $x=a$, $y=b$ makes $x=y$ false, so it is not valid.
