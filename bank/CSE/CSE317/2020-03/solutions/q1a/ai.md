---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Natural selection favours organisms whose behaviour better achieves survival and reproduction, so over generations decision mechanisms approach those that maximise expected fitness given the available percepts, which is rational behaviour; the goal they are 'designed' for is reproductive fitness (survival and propagation of genes), with sub-goals like food, safety and mating."
sources: ["AIMA 3e sec. 2.2 (Rationality) and ch. 1 exercises"]
---
**Rationality.** A rational agent chooses, for each percept sequence, the action expected to maximise its performance measure, given its percepts and built-in knowledge.

**Why evolution tends to produce rational systems.**

1. Organisms vary in their behaviour (their "agent programs" are partly encoded in genes), and variation is created by mutation and recombination.

2. The environment acts as a performance measure: behaviours that better achieve survival and reproduction lead to more offspring.

3. Genes for better-performing behaviour therefore spread through the population (natural selection), and worse-performing behaviour disappears.

4. Repeated over many generations, this optimisation process pushes behaviour towards whatever maximises expected success **given the information the organism can perceive**, i.e. towards rationality with respect to the evolutionary performance measure.

Evolution is only an approximate optimiser, so the result is bounded rationality: it is tuned to past environments (behaviour may be irrational in new ones, e.g. craving sugar today), it cannot see the future (no omniscience), and it can be stuck in local optima. Reflexes like flinching from heat are an example: they are not deliberated, but they are rational responses selected by evolution.

**Goals such systems are designed to achieve.** The "designer" (natural selection) has one ultimate goal: **reproductive fitness**, i.e. survival and reproduction, propagating the organism's genes (including through relatives, inclusive fitness). Everything else is an instrumental sub-goal serving it: obtaining food and water, avoiding predators, injury and disease, finding mates, raising and protecting offspring, cooperating with the group. Evolved agents are rational with respect to fitness, not necessarily with respect to individual happiness or long-term well-being.
