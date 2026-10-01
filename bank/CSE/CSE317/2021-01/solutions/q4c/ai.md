---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The knowledge base stores sentences (facts and rules) in a formal language; the inference engine derives new sentences from the KB with sound inference rules (TELL/ASK). Entailment (KB |= alpha: alpha is true in every model where the KB is true) is the correctness criterion that guarantees the agent's conclusions are true whenever its knowledge is, so its decisions are justified."
sources: ["AIMA 3e sec. 7.1-7.3 (Knowledge-based agents, entailment)"]
---
**Knowledge base (KB).** A set of **sentences** in a knowledge representation language (e.g. propositional or first-order logic) describing what the agent knows about the world: background knowledge given by the designer (rules such as "a square adjacent to a pit is breezy") and facts learned from percepts ("[1,2] is breezy"). It is domain-specific content. Operations: **TELL** (add sentences) and **ASK** (query).

**Inference engine.** Domain-independent algorithms that derive new sentences from the KB, answering ASK queries, e.g. model checking, resolution, forward/backward chaining. It also decides what action to take: the generic knowledge-based agent TELLs the KB the percept, ASKs which action is best, and TELLs the KB the action it took.

```text
function KB-AGENT(percept) returns an action
    TELL(KB, MAKE-PERCEPT-SENTENCE(percept, t))
    action <- ASK(KB, MAKE-ACTION-QUERY(t))
    TELL(KB, MAKE-ACTION-SENTENCE(action, t))
    t <- t + 1
    return action
```

Separating them (declarative approach) means the same inference engine works for any domain; we only change the KB.

**Why entailment is necessary.** $KB\models\alpha$ ($KB$ entails $\alpha$) means $\alpha$ is true in **every model** (possible world) in which all sentences of the KB are true. It is the definition of a logically correct conclusion.

- The inference engine must be **sound**: it should only derive sentences that are entailed. Otherwise the agent could "conclude" false things (e.g. that a square is safe when it has a pit) and act on them.

- Ideally it is also **complete**: everything entailed can be derived.

- Entailment lets the agent know facts it has not directly perceived, safely: if the KB is true in the real world, every entailed sentence is also true in the real world. E.g. in the Wumpus world, from "no breeze in [1,1]" the agent can conclude that [1,2] and [2,1] contain no pit, and move there safely.

So entailment is the link between what the agent knows and what is actually true, which makes its decisions rational.
