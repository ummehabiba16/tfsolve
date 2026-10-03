---
marks: 15
topics: [mdp]
kind: numerical
source: {page: 10}
---
Consider a Markov Decision Process (MDP) for navigating a robot on a one-dimensional grid. The grid-world is shown in Figure 8(b) which has five states $s_1, s_2, s_3, s_4$, and $s_5$. The numbers inside each cell in the grid-world denote the reward values of the corresponding states. Initially, the robot will be in the state $s_2$. In each state, the robot has two actions: L (left) and R (right). Each action takes the robot to the intended direction with a probability of 0.8 and to the opposite direction with a probability of 0.2. If the robot hits the leftmost wall, then it remains in the state $s_1$, Once the robot reaches the goal state $s_5$ (with a reward + 10), the navigation ends. The robot wants to maximize the utility.

| | $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ |
|:--|:-:|:-:|:-:|:-:|:-:|
| Grid world (reward) | $-5$ | $-1$ | $-1$ | $-1$ | $+10$ |
| Initial policy | $\leftarrow$ | $\leftarrow$ | $\rightarrow$ | $\rightarrow$ | $+10$ |

*Figure 8(b)*

Suppose you want to solve the above MDP using the policy iteration algorithm with a discount factor of 0.9. You are given an initial policy $\pi$ as shown in Figure 8(b). Based on this initial policy, perform one iteration of the policy iteration algorithm. Compute the utility $U^\pi(s)$ for all states using the policy evaluation step, and then determine the improved policy.
