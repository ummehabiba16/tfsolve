---
marks: 15
topics: [markov-hmm]
kind: analysis
source: {page: 18}
note: "'You hav 3 microphones', 'in a cornet' and 'moves to one the corners' are printed so."
---
Suppose you want to keep track of an animal in a triangular enclosure using sound. You hav 3 microphones that provide unreliable (noisy) binary information at each time step. The animal is either close to one of the 3 points of the triangle or in the middle of the triangle. If the animal is in a cornet, it will be detected by the microphone at that corner with probability 0.6, and will be independently detected by each of the other microphones with a probability of 0.1. If the animal is in the middle, it will be detected by each microphone with probability of 0.4. If the animal is in a corner it stays in the same corner with probability 0.8, goes to the middle with probability 0.1 or goes to one of the other corners with probability 0.05 each. If it is the middle, it stays in the middle with probability 0.7, otherwise it moves to one the corners, each with probability 0.1. Initially the animal is in one of the four states, with equal probability.

Now you have to formulate the above scenario using a Hidden Markov Model. What are the hidden states? List the possible observations at any time step? Construct the appropriate observation model and transition model in tabular format.
