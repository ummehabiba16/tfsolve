---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "de Finetti: if an agent's degrees of belief violate the probability axioms, there is a combination of bets, each fair by its own beliefs, that it loses whatever happens (a Dutch book). Here P(x or y) = 0.8 > P(x) + P(y) = 0.75, which is impossible since P(x or y) = P(x) + P(y) - P(x and y) <= 0.75. Agent 1 bets 40 on x (to win 60), 35 on y (to win 65) and 20 against x or y (to win 80); Agent 1 gains 105, 5, 5 or 5 in every outcome."
sources: ["AIMA 3e sec. 13.2.3 (de Finetti, Fig. 13.2)"]
---
**de Finetti's theorem** (2). If an agent's degrees of belief **violate the axioms of probability**, there is a combination of bets, each of which the agent considers fair, such that the agent **loses money in every possible outcome** (a "Dutch book"). An opponent can then always win against it. Rational beliefs must therefore obey probability theory.

**Agent 2's beliefs are incoherent** (5). It believes $P(x)=0.4$, $P(y)=0.35$ and $P(x\lor y)=0.8$. The axioms require

$$P(x\lor y)=P(x)+P(y)-P(x\land y)\le P(x)+P(y)=0.75,$$

but Agent 2 has $0.8>0.75$.

**Bets** (stakes in the ratio of Agent 2's probabilities, which Agent 2 regards as fair). Agent 1 proposes:

- bet 1: Agent 1 bets **on $x$**, staking 40 against Agent 2's 60 (odds 4:6 from $P(x)=0.4$);
- bet 2: Agent 1 bets **on $y$**, staking 35 against 65 (from $P(y)=0.35$);
- bet 3: Agent 1 bets **against $x\lor y$**: Agent 2 stakes 80 on $x\lor y$ against Agent 1's 20 (from $P(x\lor y)=0.8$).

**Agent 1's net payoff in each outcome:**

| Outcome | Bet 1 (on $x$) | Bet 2 (on $y$) | Bet 3 (against $x\lor y$) | Total for Agent 1 |
|:--|:-:|:-:|:-:|:-:|
| $x\land y$ | +60 | +65 | $-20$ | **+105** |
| $x\land\neg y$ | +60 | $-35$ | $-20$ | **+5** |
| $\neg x\land y$ | $-40$ | +65 | $-20$ | **+5** |
| $\neg x\land\neg y$ | $-40$ | $-35$ | +80 | **+5** |

Agent 1 **wins in every outcome**: the outcomes are always in favour of Agent 1. Agent 2's incoherent beliefs are exploited.
