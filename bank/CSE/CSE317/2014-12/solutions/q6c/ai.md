---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Limitations: FOL entailment is only semi-decidable (resolution may never stop when no proof exists); a combinatorial explosion of resolvents needs search strategies (unit preference, set of support, input resolution, subsumption); conversion to CNF loses structure and makes proofs unnatural; equality needs extra axioms or paramodulation; it cannot handle uncertainty or defaults (monotonic), and needs a complete, consistent KB."
sources: ["AIMA 3e sec. 9.5 (resolution, completeness, strategies, equality)"]
---
1. **Semi-decidability:** resolution is refutation-complete, but if the goal is *not* entailed, the search may run **forever** (infinite Herbrand universe with function symbols). There is no guarantee of termination.
2. **Combinatorial explosion:** the number of possible resolvents grows very fast, and most are useless. Efficiency needs control strategies: unit preference, set of support, input or linear resolution, subsumption.
3. **Clausal form:** converting to CNF (Skolemization, distribution) can blow up the size and destroys the natural structure of the knowledge. Proofs by refutation are hard for humans to follow.
4. **Equality** is not handled by plain resolution; it needs equality axioms, demodulation or paramodulation.
5. **Expressiveness of reasoning:** classical resolution is **monotonic and exact**. It cannot handle uncertainty, defaults or exceptions ("birds fly"). An inconsistent KB entails everything.
6. **Knowledge acquisition:** all relevant facts and rules must be stated explicitly and correctly (for example frame axioms), which is laborious.
