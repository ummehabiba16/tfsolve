---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Pickup zone is a Markov chain with $P=\begin{pmatrix}0.6&0.4\\0.3&0.7\end{pmatrix}$, $\pi_A=3/7$, $\pi_B=4/7$. Average profit per trip $=\frac{3}{7}(0.6\cdot6+0.4\cdot12)+\frac47(0.3\cdot12+0.7\cdot8)=62/7\approx8.86$.'
sources: ['CSE301 Markov_Chain slides 19-22 (limiting probabilities)', 'Ross, Introduction to Probability Models, Ch. 4 (limiting probabilities, long-run averages)']
---
**Model.** A fare's destination is where the driver picks up the next fare. Let $X_n$ be the zone where the $n$-th fare is picked up. Then $\{X_n\}$ is a Markov chain on $\{A,B\}$ with

$$P=\begin{pmatrix}P_{AA}&P_{AB}\\P_{BA}&P_{BB}\end{pmatrix}=\begin{pmatrix}0.6&0.4\\0.3&0.7\end{pmatrix}$$

**Limiting probabilities.** The chain is irreducible and aperiodic.

$$\pi_A=0.6\,\pi_A+0.3\,\pi_B\ \Rightarrow\ 0.4\,\pi_A=0.3\,\pi_B$$

$$\pi_A+\pi_B=1\ \Rightarrow\ \pi_A=\frac37,\quad\pi_B=\frac47$$

**Long-run fraction of each kind of trip.** A trip starting in zone $i$ and ending in zone $j$ happens a fraction $\pi_iP_{ij}$ of the time:

| Trip | Fraction $\pi_iP_{ij}$ | Profit |
|:-:|:-:|:-:|
| $A\to A$ | $\frac37\times0.6=\frac{9}{35}$ | 6 |
| $A\to B$ | $\frac37\times0.4=\frac{6}{35}$ | 12 |
| $B\to A$ | $\frac47\times0.3=\frac{6}{35}$ | 12 |
| $B\to B$ | $\frac47\times0.7=\frac{14}{35}$ | 8 |

**Average profit per trip.**

$$\frac{9}{35}(6)+\frac{6+6}{35}(12)+\frac{14}{35}(8)=\frac{54+144+112}{35}=\frac{310}{35}=\frac{62}{7}$$

**Answer:** the driver's long-run average profit is $\mathbf{62/7\approx8.86}$ per trip.
