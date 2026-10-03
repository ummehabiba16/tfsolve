---
marks: 10
topics: [markov-hmm]
kind: analysis
source: {page: 27}
---
Brendan and Selen play a coin toss game to illustrate how we can use HMMs for sequence analysis problems. Brendan starts tossing first, and they take turns. The game finishes when "THT" appears, and the winner is the one who last flips the coin. At each timestep, they can flip the coin many times, and the stopping rules are as follows:

(i) At his turn, each time Brendan flips the coin, he also flips an extra biased coin ($P(H) = 0.4$.) He stops only if the extra coin lands H, otherwise he keeps flipping the fair and extra coins. The flips of the extra biased coin are not recorded.

(ii) At her turn, Selen flips the (fair) coin until T appears (all of her flips are recorded).

You are given a sequence of recorded coin flips, you would like to infer the winner and the flips of each player. Describe an HMM to model this game.
