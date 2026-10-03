---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "An interpretation maps constant, predicate and function symbols to objects, relations and functions in a model; the intended interpretation is the one the KB designer has in mind. The same sentences have other interpretations (e.g. Richard and John both naming one object). Database semantics: unique-names, closed-world and domain-closure assumptions."
sources: ["AIMA 4e sec. 8.2.2-8.2.8 (models, interpretations, database semantics)"]
---
**Interpretation and intended interpretation.** A model of first-order logic consists of a domain of objects and an **interpretation**. The interpretation maps

- each **constant symbol** to an object,
- each **predicate symbol** to a relation (a set of tuples of objects),
- each **function symbol** to a function on the objects.

The **intended interpretation** is the one the designer of the knowledge base has in mind: the "real" meaning. For example, $Richard$ means Richard the Lionheart, $John$ means King John, $Brother$ means the brotherhood relation, and $LeftLeg$ means the function mapping a person to his left leg.

**Alternative interpretations are possible.** The symbols themselves carry no meaning, so the same KB has many interpretations. For example, take the domain {Richard, John, the crown, two legs} and the sentence $Brother(Richard,John)$.

- Intended: $Richard\mapsto$ Richard, $John\mapsto$ John, $Brother\mapsto\{\langle\text{Richard},\text{John}\rangle,\langle\text{John},\text{Richard}\rangle\}$.
- Alternative 1: $Richard\mapsto$ the crown, $John\mapsto$ the left leg, $Brother\mapsto\{\langle\text{crown},\text{leg}\rangle\}$. The sentence is still true.
- Alternative 2: $Richard$ and $John$ both name the **same** object. In standard FOL that is allowed, since two names may denote one object.

The number of models is unbounded. A sentence is *entailed* only if it is true in **all** of them, not just in the intended one.

**Database semantics.** To make the intended reading the only one, as databases and logic programs do, adopt three assumptions:

1. **Unique-names assumption:** different constant symbols denote different objects. $Richard\neq John$.
2. **Closed-world assumption:** atomic sentences not known to be true are false. If $Brother(Richard,Geoffrey)$ is not in the KB, it is false.
3. **Domain closure:** each model contains no more objects than those named by the constant symbols.

*Example:* "Richard has two brothers, John and Geoffrey" is written $Brother(John,Richard)\land Brother(Geoffrey,Richard)$. Under standard semantics this does **not** imply exactly two brothers. Under database semantics it does.
