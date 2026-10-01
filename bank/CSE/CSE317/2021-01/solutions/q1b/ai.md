---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Selection favours individuals whose behaviour better achieves survival and reproduction, so over generations behaviour approaches what maximises expected fitness given the available percepts: rational behaviour. The goal is reproductive fitness (passing on genes); food, safety and mates are sub-goals."
sources: ["AIMA 3e sec. 2.2 and ch. 1 exercises"]
---
**Why evolution produces rational systems.** Natural selection is an optimisation process:

1. Individuals differ in their inherited behaviour, and new variants appear through mutation and recombination.

2. The environment "scores" each behaviour: those that lead to more survival and reproduction leave more offspring.

3. Hence the genes for better-performing behaviour spread, and poorly performing behaviour is eliminated.

Over many generations, behaviour therefore approaches what maximises expected success given the information the organism can perceive, which is exactly the definition of rationality (maximise the expected value of a performance measure given the percept sequence). An organism that systematically chose worse actions would be out-reproduced.

The result is only approximately rational: evolution optimises for past environments, works by small local steps (local optima), and cannot make organisms omniscient.

**What goals are such systems designed to achieve?** The single "performance measure" of evolution is **reproductive fitness**: survive long enough to reproduce and pass on one's genes (including via relatives). All other goals are instrumental sub-goals of this one: obtaining food and water, avoiding predators and injury, finding mates, caring for offspring, cooperating with a group.
