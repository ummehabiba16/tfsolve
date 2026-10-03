---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Q(s,a) moves a fraction alpha of the way from the old estimate towards the TD target r + gamma max_a' Q(s',a'). Large alpha: fast learning but noisy, may not converge; small alpha: stable but slow. Large gamma: far-sighted, values future rewards; small gamma: myopic, values immediate reward."
sources: ["AIMA 4e sec. 22.3.3 (Q-learning)", "Sutton & Barto, Reinforcement Learning, sec. 6.5"]
---
**The update.**

$$Q(s,a)\leftarrow Q(s,a)+\alpha\Big(\underbrace{r+\gamma\max_{a'}Q(s',a')}_{\text{TD target (new estimate)}}-\underbrace{Q(s,a)}_{\text{old estimate}}\Big)$$

Equivalently, $Q(s,a)\leftarrow(1-\alpha)\,Q(s,a)+\alpha\,[\,r+\gamma\max_{a'}Q(s',a')\,]$, a weighted average of old and new knowledge.

**Intuition behind each component.**

- $Q(s,a)$: the current estimate of the total discounted reward from taking $a$ in $s$ and acting optimally afterwards.
- $r$: the reward actually received. This is real evidence from the environment.
- $\max_{a'}Q(s',a')$: the value of the best action in the next state. It estimates everything that comes after, so the agent does not wait for the episode to end (it *bootstraps*). Using the **max**, not the action actually taken, makes Q-learning **off-policy**: it learns the optimal $Q^*$ while exploring.
- TD target minus $Q(s,a)$: the **temporal-difference error**, i.e. how surprised the agent is. If the error is positive, the action was better than expected and $Q$ goes up; if negative, $Q$ goes down. At convergence the average error is 0 and $Q$ satisfies the Bellman equation $Q(s,a)=E[r+\gamma\max_{a'}Q(s',a')]$.
- No transition model $P(s'\mid s,a)$ is needed (model-free). Sampling $s'$ from the environment averages over the outcomes automatically.

**Effect of $\alpha$ (learning rate, $0<\alpha\le1$).**

- *Larger $\alpha$:* new experience gets more weight and old estimates are overwritten quickly. Learning is fast and adapts to a changing environment, but the estimates are noisy, oscillate with random rewards and transitions, and may not converge. At $\alpha=1$ the old value is discarded completely.
- *Smaller $\alpha$:* each sample changes $Q$ only a little, so the estimates are a smooth average of many samples. Learning is stable but slow. At $\alpha=0$ nothing is learned.
- Convergence to $Q^*$ needs $\alpha$ to decrease over time, with $\sum\alpha_t=\infty$ and $\sum\alpha_t^2<\infty$ (for example $\alpha=1/N(s,a)$).

**Effect of $\gamma$ (discount factor, $0\le\gamma\le1$).**

- *Larger $\gamma$ (near 1):* future rewards count almost as much as immediate ones. The agent is far-sighted and plans long-term, for example accepting small costs now for a big reward later. Learning is slower and values are larger and higher-variance.
- *Smaller $\gamma$ (near 0):* the agent is myopic. At $\gamma=0$, $Q(s,a)$ estimates only the immediate reward $r$, and the agent ignores long-term consequences.
