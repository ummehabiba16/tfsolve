---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) $P=\begin{pmatrix}0&\frac12&\frac12\\\frac14&0&\frac34\\\frac14&\frac34&0\end{pmatrix}$ (order A, B, C). (ii) Time 2: $(P_A,P_B,P_C)=(0,\frac12,\frac12)$; time 3: $P(A)=\frac12\cdot\frac14+\frac12\cdot\frac14=\frac14$.'
sources: ['CSE301 Markov_Chain slides 3-10 (transition matrix, n-step probabilities)', 'Ross, Introduction to Probability Models, Ch. 4 (Chapman-Kolmogorov equations)']
---
**(i) Transition matrix** (states in the order A = airport, B, C = hotels):

$$P=\begin{pmatrix}0&\frac12&\frac12\\\frac14&0&\frac34\\\frac14&\frac34&0\end{pmatrix}$$

From the airport the cab goes to either hotel with probability $\frac12$; from a hotel it goes to the airport with probability $\frac14$ and to the **other** hotel with probability $\frac34$. Each row sums to 1.

**(ii) Distribution at times 2 and 3.** At time 1 the cab is at the airport: $\mathbf p(1)=(1,0,0)$.

$$\mathbf p(2)=\mathbf p(1)P=(0,\ \tfrac12,\ \tfrac12)$$

so at time 2 the cab is at the airport with probability 0 and at each hotel with probability $\frac12$.

$$\mathbf p(3)=\mathbf p(2)P=\left(\tfrac12\cdot\tfrac14+\tfrac12\cdot\tfrac14,\ \ \tfrac12\cdot\tfrac34,\ \ \tfrac12\cdot\tfrac34\right)=\left(\tfrac14,\ \tfrac38,\ \tfrac38\right)$$

So the probability that the taxicab is at the airport at time 3 is $\left(P^2\right)_{AA}=\mathbf{\tfrac14}$.
