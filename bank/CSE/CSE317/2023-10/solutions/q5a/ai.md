---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Network Coin -> X1, X2, X3 (P(Coin) uniform; P(Xi = head | a, b, c) = 0.2, 0.6, 0.8). For H, H, T: posterior proportional to p^2(1-p) = 0.032, 0.144, 0.128, giving (0.105, 0.474, 0.421); coin b is most likely."
sources: ["MNM slides Uncertainty-2-BN (Bayesian networks, CPTs)", "AIMA 4e sec. 13.2 and Exercise 13.BAYA (three biased coins)"]
---
**(i) Bayesian network.** Variables: $Coin\in\{a,b,c\}$, and the flips $X_1,X_2,X_3\in\{H,T\}$. Given the coin, the flips are independent, so each flip depends only on the coin:

```text
              Coin
           /   |    \
          v    v     v
         X1    X2    X3
```

$$P(Coin,X_1,X_2,X_3)=P(Coin)\prod_{i=1}^{3}P(X_i\mid Coin)$$

CPTs:

| $Coin$ | $P(Coin)$ |
|:-:|:-:|
| a | 1/3 |
| b | 1/3 |
| c | 1/3 |

| $Coin$ | $P(X_i=H\mid Coin)$ | $P(X_i=T\mid Coin)$ |
|:-:|:-:|:-:|
| a | 0.2 | 0.8 |
| b | 0.6 | 0.4 |
| c | 0.8 | 0.2 |

The same table is used for $X_1$, $X_2$ and $X_3$.

**(ii) Most likely coin given $H,H,T$.**

$$P(Coin\mid H,H,T)=\alpha\,P(Coin)\,P(H\mid Coin)^2\,P(T\mid Coin)$$

| Coin | $P(Coin)\,p^2(1-p)$ | Posterior |
|:-:|:-:|:-:|
| a | $\frac13(0.2)^2(0.8)=\frac13(0.032)=0.0107$ | $0.032/0.304=0.105$ |
| b | $\frac13(0.6)^2(0.4)=\frac13(0.144)=0.0480$ | $0.144/0.304=0.474$ |
| c | $\frac13(0.8)^2(0.2)=\frac13(0.128)=0.0427$ | $0.128/0.304=0.421$ |

Here $P(H,H,T)=0.0107+0.0480+0.0427=0.1013$, and $\alpha=1/0.1013$.

**Coin $b$ is the most likely**, with $P(b\mid H,H,T)\approx0.474$ (then $c$ with 0.421, then $a$ with 0.105). The prior is uniform, so this is also the maximum-likelihood coin.
