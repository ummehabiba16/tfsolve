---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Intelligence: ability to apply knowledge to perform well in an environment; rationality: choosing the action that maximises expected performance given percepts and knowledge. Evolution is a selection process: organisms whose behaviour better serves survival and reproduction leave more offspring, exactly as an EA selects fitter individuals, so behaviour drifts toward maximising fitness; the goal is reproductive fitness (survival and reproduction of genes)."
sources: ["AIMA 3e sec. 1.1, 2.2 and ch. 1 exercises", "AIMA 3e sec. 4.1.4"]
---
**Definitions.**

- **Intelligent**: an entity is intelligent if it can acquire and apply knowledge to perform well in its environment, especially in novel situations: perceiving, reasoning, learning and acting effectively.

- **Rationality**: a rational agent, for each possible percept sequence, selects an action that is expected to maximise its performance measure, given the evidence provided by the percept sequence and its built-in knowledge. Rationality depends on (1) the performance measure, (2) prior knowledge, (3) available actions, (4) the percept sequence. It is not omniscience: it maximises *expected*, not actual, performance.

**Why evolution tends to produce rational systems (EA view).** An evolutionary algorithm has a population, a fitness function, selection, and variation (crossover, mutation). Natural evolution is the same process:

1. *Population and variation*: organisms differ, and their behaviours (decision procedures) are partly inherited, with random variation from mutation and recombination.

2. *Fitness evaluation*: the environment "evaluates" each organism; behaviour that better achieves survival and reproduction in that environment gives more offspring.

3. *Selection*: like fitness-proportional selection in an EA, organisms with better-performing behaviour pass their genes on more often.

4. Over many generations the population climbs the fitness landscape, so the behaviour that survives is the one that (approximately) **maximises expected fitness given the percepts available**, which is exactly the definition of rational behaviour with fitness as the performance measure. An agent that systematically chose worse actions would be out-competed and selected out.

Evolution produces *approximately* rational behaviour (bounded rationality): it is a local search, it optimises for past environments, and it may get stuck at local optima, just like an EA.

**Which goals are such systems designed to achieve?** The "performance measure" of natural selection is **reproductive fitness**: survival and successful reproduction, i.e. propagation of the organism's genes into future generations. Sub-goals that serve it: finding food, avoiding predators and danger, finding mates, protecting offspring and kin. In an EA the corresponding goal is maximising the fitness function the designer specified; the evolved individuals act rationally with respect to that function, not necessarily with respect to what the designer "meant".
