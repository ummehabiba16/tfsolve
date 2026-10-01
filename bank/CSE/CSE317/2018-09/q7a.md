---
marks: 25
topics: [minimax]
kind: analysis
source: {page: 30}
---
How can a game be formally defined as a kind of search problem? Consider a two-player game with the rules given below. The game starts with a single stack of 5 tokens. At each move, a player selects one stack and divides it into two non-empty, non-equal stacks. A player who is unable to move loses the game. (5+20)

Assume two players, min and max, play it. Min plays first. If a terminal state in the search tree developed above is a win for min, a utility function of zero is assigned to that state. A utility function of 1 is assigned to a state if max wins the game. Draw the complete search tree. Apply the minimax algorithm to the search tree to assign utility functions to all states in the search tree. If both min and max play a perfect game, who will win? Explain your answer.
