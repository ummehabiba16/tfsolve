---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Yes. Backward chaining on Brake: rule 1 needs PersonInFrontofCar (observed false) and fails; rule 2 needs YellowLight (observed), Policeman (from Policecar, observed) and not Slippery (Slippery is unprovable: Snow needs Winter, which is unknown, so it holds by negation as failure; also Dry is observed); and RedLight => Brake succeeds directly because RedLight is observed. So Brake is inferred."
sources: ["AIMA 3e sec. 7.5.4 (backward chaining)", "logic programming: negation as failure"]
---
**Knowledge base.**

1. $PersonInFrontofCar\Rightarrow Brake$
2. $YellowLight\land Policeman\land\neg Slippery\Rightarrow Brake$
3. $Policecar\Rightarrow Policeman$
4. $Snow\Rightarrow Slippery$
5. $Slippery\Rightarrow\neg Dry$
6. $RedLight\Rightarrow Brake$
7. $Winter\Rightarrow Snow$

Facts (sensors): $YellowLight$, $RedLight$, $Dry$, $Policecar$, $\neg PersonInFrontofCar$.

**Backward chaining from the goal $Brake$.** Try the rules whose head is $Brake$, in order:

```text
Brake?
|-- rule 1: PersonInFrontofCar?  -- sensors say NOT PersonInFrontofCar  -> fails
|-- rule 2: YellowLight?          -- fact                                 -> yes
|           Policeman?            -- rule 3: Policecar? -- fact           -> yes
|           not Slippery?         -- try to prove Slippery:
|                                      rule 4: Snow? -- rule 7: Winter? -- unknown -> fails
|                                    Slippery cannot be proved, so not Slippery holds
|                                    (also: Dry is observed and Slippery => not Dry,
|                                     so Slippery would contradict Dry)
|                                 -> rule 2 succeeds:  Brake proved
`-- rule 6: RedLight?             -- fact                                 -> Brake proved
```

**Answer: yes, the agent infers $Brake$.** The simplest proof is through rule 6: the goal $Brake$ needs the subgoal $RedLight$, which is an observed fact.

Rule 2 also succeeds: $YellowLight$ is observed; $Policeman$ follows from $Policecar$ (rule 3); and $\neg Slippery$ holds, by negation as failure (the only route to $Slippery$ is $Snow$ via $Winter$, which is unknown) and also by modus tollens from $Dry$ and rule 5.

*Note:* rule 2 has a negated premise, so it is not a definite clause. Plain backward chaining handles $\neg Slippery$ by negation as failure, as in Prolog. Rule 6 alone suffices anyway.
