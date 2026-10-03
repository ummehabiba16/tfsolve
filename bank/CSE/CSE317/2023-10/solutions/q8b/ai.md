---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) No examples: a leaf with the plurality class of the parent's examples. (ii) No attributes but mixed labels: a leaf with the plurality class of the remaining examples (noise or missing attributes). (iii) Missing values: fill with the most common value (or most common within the class), or split the example fractionally by the observed value frequencies (C4.5)."
sources: ["AIMA 4e sec. 19.3.1, Fig. 19.5 (LEARN-DECISION-TREE, PLURALITY-VALUE)", "AIMA 4e sec. 19.3.5 (missing data)"]
---
**(i) No examples left at a child node.** No training example has that combination of attribute values. Return a leaf labeled with the **plurality (majority) class of the parent node's examples**: `PLURALITY-VALUE(parent_examples)` in AIMA's algorithm. It is the best guess available from the most similar examples.

**(ii) No attributes left, but both positive and negative examples remain.** These examples have identical descriptions but different classes. That happens with noise in the data, a nondeterministic domain, or because an important attribute was not observed. Make a leaf labeled with the **plurality class of these examples**, `PLURALITY-VALUE(examples)`. Alternatively, store the class proportions and output a probability.

**(iii) Missing values in an attribute.**

- *While learning:* give the example the **most common value** of that attribute among the examples at the node (or among examples of the same class). Better: split the example into **fractional examples**, one per value, weighted by how often each value occurs at the node (C4.5). Information gain is computed with these weights.
- *While classifying:* if a test attribute is missing, follow **all** branches with the same weights and combine the leaf predictions (weighted vote), or use the most common value.
