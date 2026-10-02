---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Chain on "who is drawing" with $P_{11}=\frac{12}{13},P_{12}=\frac1{13}$; $P_{22}=\frac34,P_{23}=\frac14$; $P_{33}=\frac{10}{13},P_{31}=\frac3{13}$. Stationary: $\pi\propto(13,4,\frac{13}{3})$, i.e. Players I, II, III draw $\frac{39}{64},\frac{12}{64},\frac{13}{64}$ of the cards.'
sources: ['CSE301 Markov_Chain slides 3-6 (modelling) and 19-22 (limiting probabilities)', 'Ross, Introduction to Probability Models, Ch. 4 (limiting probabilities)']
---
**(i) States and state diagram.** Let $X_n$ be the player who draws the $n$-th card ($1$ = Player I, $2$ = Player II, $3$ = Player III). Draws are with replacement, so each card drawn by Player $i$ is his "target" with a fixed probability, independent of the past:

$$p_1=P(\text{ace})=\frac{4}{52}=\frac{1}{13},\qquad p_2=P(\text{diamond})=\frac{13}{52}=\frac14,\qquad p_3=P(\text{face card})=\frac{12}{52}=\frac{3}{13}$$

Player $i$ keeps drawing until he gets his target, so after each card the turn stays with him with probability $1-p_i$ and passes to the next player with probability $p_i$. $\{X_n\}$ is a Markov chain with

| From \ To | I | II | III |
|:-:|:-:|:-:|:-:|
| I | 12/13 | 1/13 | 0 |
| II | 0 | 3/4 | 1/4 |
| III | 3/13 | 0 | 10/13 |

State diagram: each state has a self-loop (I: $\frac{12}{13}$, II: $\frac34$, III: $\frac{10}{13}$) and a single arrow to the next player in the cycle $\text{I}\xrightarrow{1/13}\text{II}\xrightarrow{1/4}\text{III}\xrightarrow{3/13}\text{I}$.

**(ii) Long-run proportions of cards.** The proportion of cards drawn by player $i$ is the limiting probability $\pi_i$. The chain is irreducible and aperiodic. Balance between consecutive players (the flow around the cycle):

$$\pi_1\cdot\tfrac{1}{13}=\pi_2\cdot\tfrac14=\pi_3\cdot\tfrac{3}{13}$$

so $\pi_i\propto\frac{1}{p_i}$ (the expected length of player $i$'s turn): $\pi\propto\left(13,\ 4,\ \tfrac{13}{3}\right)\propto(39,\ 12,\ 13)$. Normalising (sum 64):

$$\pi_{\text{I}}=\frac{39}{64}\approx0.609,\qquad\pi_{\text{II}}=\frac{12}{64}=\frac{3}{16}\approx0.188,\qquad\pi_{\text{III}}=\frac{13}{64}\approx0.203$$

So in the long run Player I draws about 60.9% of the cards, Player II 18.8% and Player III 20.3%.
