---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Network: Weather (W) and InTime (T) -> Cross (X); X and Sunny (S) -> Reach (R); R -> Flu (F). (ii) P(T | F) = 0.951 (with P(F | R) = 0.30, P(F | not R) = 0.24): f1(X) = sum_S P(S) sum_R P(R | X,S) P(f | R) = (0.28878, 0.26931); f2(T) = sum_W P(W) sum_X P(X | W,T) f1(X) = (0.28537, 0.28148); times P(T) gives (0.27110, 0.01407). (iii) P(R | not T, not W) = 0.45(0.813) + 0.55(0.4885) = 0.6345."
sources: ["MNM slides Uncertainty-2-BN and Uncertainty-4-BN-INF", "AIMA 3e sec. 14.2 and 14.4.2"]
---
**(i) Bayesian network** (8). Boolean variables: $W$ = good weather in the Himalayas; $T$ = the birds arrive in time; $X$ = the cranes cross the Himalayas successfully; $S$ = sunny weather in our country; $R$ = the birds reach our country; $F$ = bird flu spreads.

```text
   W (weather)     T (in time)
        \             /
         v           v
      X (cross Himalayas)      S (sunny here)
                 \              /
                  v            v
                R (reach our country)
                        |
                        v
                  F (bird flu)
```

| Node | CPT |
|:--|:--|
| $W$ | $P(w)=0.50$ |
| $T$ | $P(t)=0.95$ |
| $X\mid W,T$ | $P(x\mid w,t)=0.90$, $P(x\mid w,\neg t)=0.80$, $P(x\mid\neg w,t)=0.75$, $P(x\mid\neg w,\neg t)=0.45$ |
| $S$ | $P(s)=0.55$ |
| $R\mid X,S$ | $P(r\mid x,s)=0.84$, $P(r\mid x,\neg s)=0.78$, $P(r\mid\neg x,s)=0.52$, $P(r\mid\neg x,\neg s)=0.45$ |
| $F\mid R$ | $P(f\mid r)=0.30$, $P(f\mid\neg r)=0.24$ |

**(ii) $P(T\mid f)$ by variable elimination** (12).

$$P(T\mid f)=\alpha\,P(T)\sum_wP(w)\sum_xP(x\mid w,T)\sum_sP(s)\sum_rP(r\mid x,s)P(f\mid r)$$

*Eliminate $R$ and $S$:* $f_1(X)=\sum_sP(s)\sum_rP(r\mid X,s)P(f\mid r)$, where $\sum_rP(r\mid X,s)P(f\mid r)=0.24+0.06\,P(r\mid X,s)$.

$$f_1(x)=0.55(0.24+0.06\times0.84)+0.45(0.24+0.06\times0.78)=0.28878$$

$$f_1(\neg x)=0.55(0.24+0.06\times0.52)+0.45(0.24+0.06\times0.45)=0.26931$$

*Eliminate $X$ and $W$:* $f_2(T)=\sum_wP(w)\sum_xP(x\mid w,T)f_1(x)$.

$$f_2(t)=0.5[0.9(0.28878)+0.1(0.26931)]$$

$$\quad+0.5[0.75(0.28878)+0.25(0.26931)]$$

$$=0.28537$$

$$f_2(\neg t)=0.5[0.8(0.28878)+0.2(0.26931)]$$

$$\quad+0.5[0.45(0.28878)+0.55(0.26931)]$$

$$=0.28148$$

*Multiply by $P(T)$ and normalize:* $0.95\times0.28537=0.27110$ and $0.05\times0.28148=0.01407$.

$$P(T=\text{in time}\mid\text{flu})=\frac{0.27110}{0.28517}=\mathbf{0.951}$$

Almost unchanged from the prior 0.95: the flu evidence is only weakly informative, since $P(f\mid r)=0.30$ is close to $P(f\mid\neg r)=0.24$.

**(iii) $P(r\mid\neg t,\neg w)$** (8). Given $\neg w$ and $\neg t$, $P(x)=0.45$. Sum out $X$ and $S$ ($F$ is a barren descendant and drops out):

Let $f(X)=\sum_sP(s)P(r\mid X,s)$:

$$f(x)=0.55(0.84)+0.45(0.78)=0.813$$

$$f(\neg x)=0.55(0.52)+0.45(0.45)=0.4885$$

$$P(r\mid\neg t,\neg w)=0.45(0.813)+0.55(0.4885)=0.36585+0.26868=\mathbf{0.634}$$

*Note:* "30% due to the presence of Siberian cranes and 24% due to other causes" is read as $P(f\mid r)=0.30$ and $P(f\mid\neg r)=0.24$. Reading it as a noisy-OR, $P(f\mid r)=1-0.7\times0.76=0.468$, gives $P(T\mid f)=0.952$, almost the same.
