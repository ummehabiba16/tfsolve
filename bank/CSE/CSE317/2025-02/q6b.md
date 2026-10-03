---
marks: 23
topics: [markov-hmm]
kind: numerical
source: {page: 8}
note: "'low temperature is 0.4' is printed so (the states are Cold and Hot)."
---
Suppose we want to determine the average annual temperature at a particular location over a series of years in a distant past where thermometers did not exist. Since we can't go back in time, we look for indirect evidence of the temperature, say in terms of the size of a tree. For simplicity, assume that we consider the two temperatures Cold and Hot, which we denote by $C$ and $H$, and three different sizes of the tree: Small, Medium, and Large, which we denote by $S$, $M$, $L$. Suppose, $X_t$ and $E_t$ represent the temperature and tree size at time step $t$. The initial probability for hot temperature is 0.6 and low temperature is 0.4. The transition and observation models are shown in Figure 6(b)

| $X_t$ | $P(X_{t+1} = C)$ |
|:-:|:-:|
| $C$ | 0.6 |
| $H$ | 0.3 |

| $X_t$ | $P(E_t = S)$ | $P(E_t = M)$ |
|:-:|:-:|:-:|
| $C$ | 0.7 | 0.2 |
| $H$ | 0.1 | 0.4 |

*Figure 6(b)*

Suppose we observe the sequence of first three tree sizes: $e_1 = M$, $e_2 = M$, $e_3 = L$. Answer the following questions:

i. Compute the probability $P(X_3 \mid e_1, e_2, e_3)$. Show the forward probability table.

ii. Compute the probability $P(X_1 \mid e_1, e_2, e_3)$. Show the backward probability table.
