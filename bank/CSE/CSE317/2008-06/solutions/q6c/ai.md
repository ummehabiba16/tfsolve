---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Go on a bike ride iff (not Summer and Warm) or (Summer and Sunny) or (Summer and not Sunny and Sunday): one disjunct per path to a 'yes' leaf."
sources: ["AIMA 3e sec. 18.3.1 (decision trees are equivalent to propositional DNF)"]
---
A decision tree is equivalent to a propositional sentence in disjunctive normal form, with **one conjunction per path from the root to a "yes" leaf**.

The paths ending in "yes" (Figure 6(c)):

1. Summer = F, then Warm = T: $\neg Summer\land Warm$
2. Summer = T, then Sunny = T: $Summer\land Sunny$
3. Summer = T, Sunny = F, then Sunday = T: $Summer\land\neg Sunny\land Sunday$

**Single sentence:**

$$BikeRide\Leftrightarrow(\neg Summer\land Warm)\lor(Summer\land Sunny)\lor(Summer\land\neg Sunny\land Sunday)$$

(Equivalently, $(\neg Summer\land Warm)\lor(Summer\land(Sunny\lor Sunday))$.)
