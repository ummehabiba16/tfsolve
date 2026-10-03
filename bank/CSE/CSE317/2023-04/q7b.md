---
marks: 15
topics: [reinforcement-learning]
kind: conceptual
source: {page: 18}
---
Q-Learning is a model of reinforcement learning, where a function $Q(s, a)$ outputs an estimate of the utility value of taking action a in state s. Every time we take an action a in state s to reach a new state s' and observe a reward r, we update $Q(s, a)$ based on the following mechanism.

$$Q(s, a) \leftarrow Q(s, a) + \alpha\left(\left(r + \gamma \max_{a'} Q(s', a')\right) - Q(s, a)\right)$$

Explain the intuitions behind the components of this update mechanism. You must discuss the effect of increasing/decreasing the values of $\alpha$ and $\gamma$.
