---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) Special-purpose logics (temporal, modal, fuzzy, probabilistic) add ontological or epistemological commitments, such as time or degrees of belief, for one domain; higher-order logics quantify over relations and functions, not only objects. (ii) Standard semantics allows several names for one object, objects with no name, and open worlds; database semantics assumes unique names, a closed world and domain closure."
sources: ["AIMA 3e sec. 8.1.2 and 8.2.8"]
---
**(i) Special-purpose logics versus higher-order logics** (2).

- **Special-purpose logics** add specific ontological or epistemological commitments to first-order logic for a particular domain. *Temporal logic* assumes facts hold at particular times, which are ordered. *Modal logic* adds operators such as "agent A believes / knows $\phi$". *Fuzzy logic* gives degrees of truth, and *probabilistic logic* degrees of belief. The objects are still first-order.
- **Higher-order logics** are more expressive in what can be **quantified over**. Second-order logic quantifies over relations and functions, not just objects: for example $\forall P\ (P(a)\Leftrightarrow P(b))\Rightarrow a=b$ (Leibniz's law). They can state things FOL cannot, but they have no complete proof procedure.

**(ii) Database semantics versus standard FOL semantics** (4).

| Standard semantics | Database semantics |
|:--|:--|
| Two constants may denote the **same** object | **Unique-names assumption:** different constants denote different objects |
| Sentences not entailed are *unknown* (open world) | **Closed-world assumption:** atomic sentences not known to be true are **false** |
| The domain may contain unnamed objects | **Domain closure:** the domain contains only the objects named by constants |

*Example:* the KB is $Brother(John,Richard)\land Brother(Geoffrey,Richard)$. Under standard semantics, Richard might have 1 brother (if John = Geoffrey) or more (unnamed ones). Under database semantics he has **exactly 2**. Database semantics gives definite answers (as in databases and Prolog), at the cost of having to state all positive facts.
