---
marks: 8
topics: [propositional-logic]
kind: analysis
source: {page: 76}
---
Consider the following knowledge-base which describes the rules to identify when the car should brake?

$PersonInFrontofCar \Rightarrow Brake$

$(YellowLight \land Policeman \land \neg Slippery) \Rightarrow Brake$

$Policecar \Rightarrow Policeman$

$Snow \Rightarrow Slippery$

$Slippery \Rightarrow \neg Dry$

$RedLight \Rightarrow Brake$

$Winter \Rightarrow Snow$

Observation from sensors:

$YellowLight \land RedLight \land Dry \land Policecar \land \neg PersonInFrontofCar$

Using the Backward chaining inference strategy can the agent infer "Brake"?
