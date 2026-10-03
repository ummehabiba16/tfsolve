---
marks: 12
topics: [mdp]
kind: analysis
source: {page: 8}
---
Consider a rover that operates on a slope and uses solar panels to recharge. It can be in one of three states: "high", "medium" and "low" on the slope. At each time step, the robot either spins its wheels or not. Spinning the wheels moves the robot one step upward (from low to medium or from medium to high) or stays high with a probability of 0.7. Despite spinning, sometimes wheels malfunction, and the robot remains in the same slope with probability 0.1 or go one step downward (from high to medium or from medium to low) or stays low with probability 0.2. If the robot does not spin its wheels, it always slides down the slope (from high to medium or from medium to low) or stays low. Staying in each slope consumes one unit of energy per time step. However, being on "high" on the slope gains three units of energy per time step via the solar panels, while being on "low" and "medium" on the slope does not gain any energy per time step. The robot wants to gain as much energy as possible without ever exiting (i.e., the goal state is not a terminal state).

Formulate the above problem using a Markov Decision Process (MDP). Show the actions, states, transition model, and reward model.
