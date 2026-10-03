---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Knowledge-engineering steps: identify the task; assemble the relevant knowledge; decide on a vocabulary of predicates, functions and constants (the ontology); encode general domain knowledge; encode the specific problem instance; pose queries and get answers; debug the KB. The ontology of the Wumpus world: objects (squares, the agent, the Wumpus, pits, gold, the arrow), relations (Adjacent, At, Pit, Breezy, Stench), functions (Home), time-indexed fluents, and percepts as [Stench, Breeze, Glitter, Bump, Scream]."
sources: ["AIMA 3e sec. 8.4 (knowledge engineering in FOL), sec. 8.3.4 (the Wumpus world)"]
---
**Steps of the knowledge-engineering process.**

1. **Identify the task:** the range of questions the KB must answer, and the facts available per problem instance.
2. **Assemble the relevant knowledge:** work with domain experts (knowledge acquisition) to understand the domain.
3. **Decide on a vocabulary** of predicates, functions and constants. This is the domain's **ontology**: a theory of what kinds of things exist.
4. **Encode general knowledge about the domain:** write the axioms (rules) using the vocabulary.
5. **Encode a description of the specific problem instance:** atomic sentences (facts).
6. **Pose queries** to the inference procedure and get answers.
7. **Debug the knowledge base:** fix missing or wrong axioms when the answers are wrong.

**Ontology of the Wumpus world** (step 3), with examples:

- *Objects / constants:* squares $[x,y]$, the $Agent$, the $Wumpus$, pits, $Gold$, the $Arrow$, time steps $t$.
- *Relations (predicates):* $Adjacent(s,r)$; $Pit(s)$; $Breezy(s)$; $Smelly(s)$ (stench); $At(Agent,s,t)$ (time-indexed fluents); $Alive(Wumpus,t)$; $HaveArrow(t)$; $Safe(s)$.
- *Functions:* $Home(Wumpus)$, the square where the Wumpus lives.
- *Percepts:* $Percept([Stench,Breeze,Glitter,None,None],t)$.
- *Actions:* $Forward$, $Turn(Right)$, $Turn(Left)$, $Shoot$, $Grab$, $Climb$.

*General knowledge (step 4)*, for example:

$$\forall s\ Breezy(s)\Leftrightarrow\exists r\ Adjacent(r,s)\land Pit(r)$$

$$\forall s,t\ At(Agent,s,t)\land Breeze(t)\Rightarrow Breezy(s)$$

$$\forall x,y,a,b\ Adjacent([x,y],[a,b])\Leftrightarrow(x=a\land(y=b-1\lor y=b+1))\lor(y=b\land(x=a-1\lor x=a+1))$$

Choosing the ontology well (for example, one predicate $Pit(s)$ instead of 16 propositions $P_{1,1},\dots$) makes the axioms short and general.
