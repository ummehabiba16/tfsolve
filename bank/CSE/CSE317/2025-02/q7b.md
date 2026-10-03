---
marks: 10
topics: [markov-hmm]
kind: analysis
source: {page: 9}
---
Suppose you are the host of a game and you ask a series of questions to the participants. The difficulty of the question depends on the color of a randomly selected ball from one of two different boxes (Box1 and Box2). The first box (Box1) contains 3 red and 5 green balls. The second box (Box2) contains 4 red and 3 green balls. Each time, you select a box randomly and then choose a ball randomly from the selected box. If the color of the ball is red, then you ask a difficult question; otherwise, you ask an easy question. There is no numbering on the boxes and thus you remember them in your memory. Suppose you start the game with Box1. You always want to select Box1 in the subsequent time steps; however, inadvertently you forget and mistakenly select Box2. You make this mistake 20% of the time if Box1 was chosen in the previous time step and 10% of the time if Box2 was chosen in the previous time step.

Construct a Hidden Markov Model (HMM) for the above problem. Show the transition model and observation model.
