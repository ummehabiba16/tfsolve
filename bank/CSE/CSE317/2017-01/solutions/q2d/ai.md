---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Ontological commitment (what exists): propositional logic has facts only; FOL has facts, objects and relations. Epistemological commitment (what an agent can believe about facts): both have true / false / unknown (probability theory would add degrees of belief)."
sources: ["AIMA 3e sec. 8.1.2, Fig. 8.1 (formal languages and their ontological and epistemological commitments)"]
---
| | **Ontological commitment** (what exists in the world) | **Epistemological commitment** (states of knowledge about facts) |
|:--|:--|:--|
| Propositional logic | **facts** only (each proposition is true or false) | true / false / unknown |
| First-order logic | **facts, objects and relations** (and functions) | true / false / unknown |

- *Ontological:* propositional logic assumes the world consists only of facts that hold or do not hold, with no internal structure. FOL assumes the world contains **objects** with **relations** among them, so it can say "all squares adjacent to a pit are breezy" in one sentence, with quantifiers. Propositional logic needs one sentence per square.
- *Epistemological:* the two logics are the **same**. The agent can believe a sentence to be true, false, or have no opinion. (Probability theory keeps the ontology of facts but changes the epistemology to degrees of belief in $[0,1]$.)

So FOL differs from propositional logic in its ontology (much more expressive), not in its epistemology.
