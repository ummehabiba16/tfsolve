---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The latter statement is true only at the level of the instructions; it does not imply the former. An evolutionary algorithm is told only how to vary and select candidates, yet the solutions it produces were never written by the programmer and can exceed the programmer's own ability, so programmed computers can show intelligent, novel behaviour."
sources: ["AIMA 3e ch. 1 exercises and sec. 26.1 (Weak AI: can machines act intelligently?)", "AIMA 3e sec. 4.1.4 (Genetic algorithms)"]
---
**Is the latter statement true?** In a narrow sense, yes: a computer executes exactly the instructions of its program. But "what the programmers tell them" is much less than what the computer ends up doing. The programmer specifies a *procedure* (e.g. a learning or search procedure), not the *behaviour* that results from running it on data. Anyone who has debugged a program, or trained a learning program, knows that the program's behaviour is often not what the programmer consciously intended or could predict.

**Does it imply the former?** No. The argument confuses the level of the rules with the level of the behaviour. By the same logic humans could not be intelligent, since neurons only do what the laws of chemistry and physics "tell" them. Intelligence is a property of behaviour (acting rationally, learning, solving novel problems), not of whether the underlying mechanism follows rules.

**Evolutionary-algorithm view.** In an evolutionary algorithm (EA) the programmer writes only:

1. a representation of candidate solutions (chromosomes),

2. a fitness function saying how good a candidate is,

3. generic operators: selection, crossover, mutation.

The programmer does **not** write the solution. Starting from random individuals, the EA repeatedly selects fitter individuals and produces variations; over generations it discovers designs and strategies that nobody programmed and that may be unknown to, or better than anything known by, the programmer. Examples: evolved antenna designs for NASA's ST5 spacecraft, evolved game-playing strategies, Samuel's checkers program (a learning program) which came to play better than Samuel himself.

So the computer only "does what it is told" in the sense that it follows the EA's rules, but the content of the final solution is the product of variation and selection interacting with the environment (fitness), just as biological evolution produced intelligent organisms by following physical laws. The output can be novel, adaptive and better than its creator, which is what we call intelligent behaviour. Hence the latter statement does not imply that computers cannot be intelligent.
