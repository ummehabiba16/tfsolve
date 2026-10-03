---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The frame problem is representing and reasoning about what does NOT change when actions occur. Representational frame problem: needing an explicit frame axiom for each (action, unaffected fluent) pair, O(AF) axioms; solved by successor-state axioms (O(F) axioms of size O(A)). Inferential frame problem: projecting the state forward through a t-step plan efficiently (time O(Et) rather than O(Ft))."
sources: ["AIMA 3e sec. 7.7.1 (the frame problem), sec. 10.4.2 (situation calculus)"]
---
**The frame problem.** When an agent reasons about actions, it must know not only what an action **changes** but also everything it **does not change**. For example, shooting the arrow does not change the agent's location or whether it has the gold. Logic does not assume persistence: in the sentence "$Forward^t\Rightarrow\dots$", any fluent not mentioned could take any value at $t+1$. The frame problem is how to represent and reason about these non-effects efficiently. The name comes from the "frame of reference" in physics: the background that stays fixed.

**Representational frame problem.** Writing an explicit **frame axiom** for every action-fluent pair that is not affected, for example

$$Forward^t\Rightarrow(HaveArrow^t\Leftrightarrow HaveArrow^{t+1}),$$

needs $O(A\cdot F)$ axioms for $A$ actions and $F$ fluents. In the real world, actions affect only a small number $E$ of fluents, so most of these axioms are about nothing changing. *Solution:* **successor-state axioms**, one per fluent, which list how it can change:

$$F^{t+1}\Leftrightarrow ActionCausesF^t\lor(F^t\land\neg ActionCausesNotF^t).$$

That is $O(F)$ axioms, each of size about $O(E)$.

**Inferential frame problem.** Even with a compact representation, the reasoner must **project** the state through a $t$-step action sequence. Naively, it recomputes every fluent at every step, $O(F\cdot t)$. The inferential problem is to make this efficient, ideally $O(E\cdot t)$, updating only the fluents that actually change (as in STRIPS-style planning, which assumes everything not mentioned in the effects stays the same).

**Difference:** the representational problem concerns the **size of the axioms**; the inferential problem concerns the **time taken to reason** with them.
