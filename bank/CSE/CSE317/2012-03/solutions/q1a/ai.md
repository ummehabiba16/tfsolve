---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Supervised learning learns a function from labeled input-output pairs (classification, regression); unsupervised learning finds structure in unlabeled inputs (clustering, density estimation). Reinforcement learning: the agent learns a policy from rewards and punishments received after its actions, by trial and error, without being told the correct action."
sources: ["AIMA 3e sec. 18.1 (forms of learning), ch. 21 (reinforcement learning)"]
---
| | **Supervised learning** | **Unsupervised learning** |
|:--|:--|:--|
| Training data | **labeled** pairs $(x_j,y_j)$, with $y_j=f(x_j)$ given by a "teacher" | **unlabeled** inputs $x_j$ only |
| Goal | learn $h\approx f$ to predict $y$ for new $x$ | discover structure or patterns in the data |
| Tasks | classification (spam or not), regression (price) | clustering (group customers), density estimation, dimensionality reduction |
| Evaluation | accuracy or error on a labeled test set | no direct "correct answer"; internal criteria |
| Examples | decision trees, naive Bayes, neural networks | k-means, EM for mixture models, PCA |

**Reinforcement learning.** The agent learns from a series of **reinforcements: rewards or punishments**, received as it acts in an environment, rather than from labeled examples. It must discover by trial and error which actions maximize its long-term expected reward (learning a policy or utility function). The feedback is often delayed. *Example:* a game-playing agent receives +1 for a win and $-1$ for a loss at the end of a game, and must work out which moves were responsible (Q-learning, TD learning).
