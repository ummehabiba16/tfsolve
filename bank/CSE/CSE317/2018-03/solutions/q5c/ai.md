---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Mathematics: formal logic, computation and algorithms (incompleteness, computability, tractability, NP-completeness) and probability, the tools for reasoning under uncertainty. Economics: decision theory and utility (rational choice under uncertainty), game theory (multi-agent), operations research and MDPs (sequential decisions), satisficing. Control theory and cybernetics: self-regulating feedback systems that maximize an objective function over time; the basis of the agent-environment loop and of robotics."
sources: ["AIMA 3e sec. 1.2 (The foundations of AI)"]
---
**(i) Mathematics.** AI needs a formal science of logic, computation and probability.

- **Logic:** Boole's propositional logic and Frege's first-order logic give the formal rules for drawing valid conclusions (knowledge representation and reasoning).
- **Computation:** algorithms, Gödel's incompleteness and Turing's computability show what can be computed; **tractability** and **NP-completeness** show what can be computed *efficiently*, which shapes how AI programs are designed (heuristics, approximations).
- **Probability** (Cardano, Bayes, Laplace): the basis for reasoning with uncertain knowledge and noisy data, giving Bayesian networks, HMMs and machine learning.

**(ii) Economics.** The study of how to make decisions that maximize payoff.

- **Decision theory** combines probability and **utility theory**: a formal framework for rational decisions under uncertainty (maximize expected utility). This is the definition of a rational agent.
- **Game theory** (von Neumann and Morgenstern) handles decisions among several interacting agents, the basis of adversarial search and multi-agent systems.
- **Operations research** and **Markov decision processes** (Bellman) handle *sequential* decisions whose payoff comes after several actions.
- Simon's **satisficing** (good-enough decisions) describes bounded rationality.

**(iii) Control theory and cybernetics.** How artifacts can operate under their own control.

- Feedback-controlled machines, from Ktesibios's water clock to Wiener's cybernetics, are self-regulating systems that sense the error between the actual and the desired state and act to reduce it.
- Modern control theory designs systems that **maximize an objective function over time**. This matches AI's view of an agent that maximizes performance in a sense-act loop, and it underlies robotics and continuous control.
- AI differs mainly in its tools (logic, symbolic and discrete reasoning, learning) and in the problems it tackles (language, vision, planning) beyond calculus-based control.
