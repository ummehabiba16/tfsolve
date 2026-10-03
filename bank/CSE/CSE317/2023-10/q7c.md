---
marks: 12
topics: [markov-hmm]
kind: analysis
source: {page: 14}
---
Consider the following random process. A magician has three coins, each of which has a distinct type. One is a fair coin (50/50 odds of heads vs tails). The other two are tricky coins: one has heads on both sides and the other has tails on both sides. At every time step, the magician picks a coin randomly with the exception that a fair coin is not picked at two successive time steps (in which case remaining coins are equally likely to be chosen). After picking a coin (without actually showing you which coin was picked), the magician flips (toss) it, and shows you the result, However, unfortunately, the magician only shows you the coin very briefly, and 10% of the time you make a mistake when you observe the true side of the coin (e.g., you see heads when it was actually tails). Construct a hidden Markov model (HMM) to formulate the problem. Show the state transition probabilities (transition model) and observation probabilities (sensor model).
