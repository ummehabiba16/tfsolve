---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Evidence -c, weight w = P(-c | p): 0.1 if +p, 0.7 if -p. W(+d) = 1.0, W(-d) = 3.6, so P(+d | -c) ~ 1.0/4.6 = 0.217 (exact value 0.418)."
sources: ["MNM slides Uncertainty-5-BN-Sampling (likelihood weighting)", "AIMA 4e sec. 13.4.1 (likelihood weighting)"]
---
**Likelihood weighting.** The evidence variable is fixed to its observed value ($C=-c$, unreliable communication), and the other variables are sampled from their CPTs in topological order. Each sample gets the weight

$$w=\prod_{\text{evidence } E_i}P(e_i\mid \text{parents}(E_i))=P(-c\mid p),$$

because $C$ is the only evidence variable and its only parent is $P$. From the CPT, $P(-c\mid +p)=1-0.9=0.1$ and $P(-c\mid -p)=1-0.3=0.7$.

| # | Sample | $P$ | weight $w$ |
|:-:|:--|:-:|:-:|
| 1 | +d, +t, +p, -m, -c | +p | 0.1 |
| 2 | +d, -t, -p, +m, -c | -p | 0.7 |
| 3 | +d, +t, +p, -m, -c | +p | 0.1 |
| 4 | -d, -t, -p, -m, -c | -p | 0.7 |
| 5 | -d, -t, -p, +m, -c | -p | 0.7 |
| 6 | +d, -t, +p, +m, -c | +p | 0.1 |
| 7 | -d, -t, -p, -m, -c | -p | 0.7 |
| 8 | -d, -t, +p, +m, -c | +p | 0.1 |
| 9 | -d, +t, -p, -m, -c | -p | 0.7 |
| 10 | -d, -t, -p, -m, -c | -p | 0.7 |

**Weighted counts for the query $D$.**

$$W(+d)=w_1+w_2+w_3+w_6=0.1+0.7+0.1+0.1=1.0$$

$$W(-d)=w_4+w_5+w_7+w_8+w_9+w_{10}=0.7+0.7+0.7+0.1+0.7+0.7=3.6$$

**Normalise.**

$$\hat P(+d\mid -c)=\frac{1.0}{1.0+3.6}=\mathbf{0.217},\qquad \hat P(-d\mid -c)=\frac{3.6}{4.6}=0.783.$$

**Comment.** The exact answer from Q5(b) is $P(+d\mid -c)=0.418$. Likelihood weighting is consistent: the estimate converges to the exact value as the number of samples grows. With only 10 samples (four of them $+d$, against a prior of 0.2), the estimate is still noisy. The values of $T$ and $M$ play no role, because they are not evidence and $M$ is not an ancestor of $C$.
