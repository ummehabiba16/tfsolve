---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Agent 2's beliefs violate the axioms: P(x or y) = 0.8 > P(x) + P(y) = 0.75 >= P(x) + P(y) - P(x and y). Agent 1 bets 40 on x (against 60), 35 on y (against 65) and 20 against x or y (against 80); Agent 1 nets +105 if x and y, and +5 in each of the other three outcomes: a Dutch book."
sources: ["AIMA 3e sec. 13.2.3 (de Finetti, Fig. 13.2)"]
---
**de Finetti's theorem.** If an agent holds degrees of belief that **violate the axioms of probability**, there exists a set of bets, each fair according to its beliefs, that guarantees it **loses in every outcome** (a Dutch book).

**Agent 2's beliefs.** $P(x)=0.4$, $P(y)=0.35$, $P(x\lor y)=0.8$. Any coherent belief must satisfy $P(x\lor y)=P(x)+P(y)-P(x\land y)\le0.75$, but $0.8>0.75$, so the beliefs are incoherent.

**Bets offered by Agent 1** (stakes proportional to Agent 2's probabilities, which Agent 2 accepts as fair):

| Bet | Agent 1 stakes | Agent 2 stakes | Agent 1 wins if |
|:--|:-:|:-:|:--|
| on $x$ | 40 | 60 | $x$ |
| on $y$ | 35 | 65 | $y$ |
| against $x\lor y$ | 20 | 80 | $\neg(x\lor y)$ |

**Agent 1's net payoff.**

| Outcome | On $x$ | On $y$ | Against $x\lor y$ | Total |
|:--|:-:|:-:|:-:|:-:|
| $x,\ y$ | +60 | +65 | $-20$ | **+105** |
| $x,\ \neg y$ | +60 | $-35$ | $-20$ | **+5** |
| $\neg x,\ y$ | $-40$ | +65 | $-20$ | **+5** |
| $\neg x,\ \neg y$ | $-40$ | $-35$ | +80 | **+5** |

Every outcome is in favour of Agent 1. This shows that Agent 2's beliefs are irrational in de Finetti's sense.
