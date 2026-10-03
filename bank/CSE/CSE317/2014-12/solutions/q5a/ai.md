---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Network: T-kick -> Low <- P-kick; Low -> Rain; Low -> Cyclone <- C-force. (ii) Variable elimination: f1(L) = sum_C P(C) P(y|C,L) = (0.4175, 0.115); f2(L,P) = sum_T P(T) P(L|T,P); f3(P) = sum_L f2 f1 = (0.3199, 0.1944); times P(P) gives (0.19197, 0.07776), so P(P-kick | cyclone) = 0.712. (iii) P(cyclone | T, P) = 0.8(0.4175) + 0.2(0.115) = 0.357."
sources: ["MNM slides Uncertainty-2-BN and Uncertainty-4-BN-INF (variable elimination)", "AIMA 3e sec. 14.2 and 14.4.2"]
---
**(i) Bayesian network** (8). Variables (Boolean): $T$ = T-kick, $P$ = P-kick, $L$ = low-pressure zone, $R$ = moderate rainfall, $C$ = C-force (Coriolis), $Y$ = cyclone.

```text
   T-kick (T)        P-kick (P)
          \            /
           v          v
           Low zone (L)        C-force (C)
            /        \            /
           v          v          v
      Rain (R)          Cyclone (Y)
```

| Node | CPT |
|:--|:--|
| $T$ | $P(t)=0.65$ |
| $P$ | $P(p)=0.60$ |
| $L\mid T,P$ | $P(l\mid t,p)=0.80$, $P(l\mid t,\neg p)=0.35$, $P(l\mid\neg t,p)=0.45$, $P(l\mid\neg t,\neg p)=0.10$ |
| $R\mid L$ | $P(r\mid l)=0.48$ (with $\neg l$ not given) |
| $C$ | $P(c)=0.25$ |
| $Y\mid C,L$ | $P(y\mid c,l)=0.95$, $P(y\mid c,\neg l)=0.22$, $P(y\mid\neg c,l)=0.24$, $P(y\mid\neg c,\neg l)=0.08$ |

**(ii) $P(P\mid y)$ by variable elimination** (12).

$$P(P\mid y)=\alpha\,P(P)\sum_l\Big[\sum_tP(t)P(l\mid t,P)\Big]\Big[\sum_cP(c)P(y\mid c,l)\Big]\sum_rP(r\mid l).$$

$R$ is a barren leaf: $\sum_rP(r\mid l)=1$, so it drops out.

*Eliminate $C$:* $f_1(L)=\sum_cP(c)P(y\mid c,L)$.

$$f_1(l)=0.25(0.95)+0.75(0.24)=0.4175,\qquad f_1(\neg l)=0.25(0.22)+0.75(0.08)=0.115$$

*Eliminate $T$:* $f_2(L,P)=\sum_tP(t)P(L\mid t,P)$.

| | $p$ | $\neg p$ |
|:--|:-:|:-:|
| $l$ | $0.65(0.8)+0.35(0.45)=0.6775$ | $0.65(0.35)+0.35(0.10)=0.2625$ |
| $\neg l$ | 0.3225 | 0.7375 |

*Eliminate $L$:* $f_3(P)=\sum_lf_2(l,P)f_1(l)$.

$$f_3(p)=0.6775(0.4175)+0.3225(0.115)=0.31994$$

$$f_3(\neg p)=0.2625(0.4175)+0.7375(0.115)=0.19441$$

*Multiply by $P(P)$ and normalize:*

$$0.6\times0.31994=0.19197,\qquad 0.4\times0.19441=0.07776,\qquad P(y)=0.26973$$

$$P(\text{P-kick}\mid\text{cyclone})=\frac{0.19197}{0.26973}=\mathbf{0.712}$$

**(iii) $P(y\mid t,p)$** (8). Given both kicks, $P(l\mid t,p)=0.8$. Then sum out $L$ and $C$:

$$P(y\mid t,p)=\sum_lP(l\mid t,p)\sum_cP(c)P(y\mid c,l)=0.8\,(0.4175)+0.2\,(0.115)=0.334+0.023=\mathbf{0.357}$$

*Note:* $P(r\mid\neg l)$ is not given. It is not needed, because $R$ is irrelevant to both queries.
