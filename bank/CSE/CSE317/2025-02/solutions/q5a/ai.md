---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Network Difficulty -> Grade <- Intelligence, Grade -> Letter. P(I=high) = 100/500 = 0.2, P(D=difficult) = 25/150 = 1/6; P(G=good | high, *) = 0.9, | low, easy = 0.8, | low, difficult = 0.6; P(L=recommend | good) = 0.95, | bad = 0.2."
sources: ["MNM slides Uncertainty-2-BN (Bayesian network, CPTs)", "AIMA 4e sec. 13.2", "Koller & Friedman, Probabilistic Graphical Models, the 'student network'"]
---
**Variables** (all Boolean):

- $D$ = course Difficulty $\in\{\text{difficult},\text{easy}\}$
- $I$ = Intelligence $\in\{\text{high},\text{low}\}$
- $G$ = Grade $\in\{\text{good},\text{bad}\}$
- $L$ = Letter $\in\{\text{recommend},\text{not recommend}\}$

**Structure.** The grade depends on difficulty and intelligence. The letter depends only on the grade.

```text
   Difficulty (D)     Intelligence (I)
            \             /
             v           v
              Grade (G)
                  |
                  v
             Letter (L)
```

$$P(D,I,G,L)=P(D)\,P(I)\,P(G\mid D,I)\,P(L\mid G).$$

$D$ and $I$ have no parents (they are independent a priori), and $L$ is conditionally independent of $D$ and $I$ given $G$.

**CPTs.**

Priors, estimated from the counts: $P(I=\text{high})=\frac{100}{500}=0.2$ and $P(D=\text{difficult})=\frac{25}{150}=\frac16\approx0.167$.

| $D$ | $P(D)$ |
|:--|:-:|
| difficult | 0.167 |
| easy | 0.833 |

| $I$ | $P(I)$ |
|:--|:-:|
| high | 0.2 |
| low | 0.8 |

| $I$ | $D$ | $P(G=\text{good}\mid I,D)$ | $P(G=\text{bad}\mid I,D)$ |
|:--|:--|:-:|:-:|
| high | difficult | 0.9 | 0.1 |
| high | easy | 0.9 | 0.1 |
| low | difficult | 0.6 | 0.4 |
| low | easy | 0.8 | 0.2 |

| $G$ | $P(L=\text{recommend}\mid G)$ | $P(L=\text{not}\mid G)$ |
|:--|:-:|:-:|
| good | 0.95 | 0.05 |
| bad | 0.20 | 0.80 |

The network needs $1+1+4+2=8$ independent numbers, against $2^4-1=15$ for the full joint distribution.

*Note:* the priors are the relative frequencies in the given counts (500 students, 150 courses).
