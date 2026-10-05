---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Network: T-kick -> Low <- P-kick; Low -> Rain; Low -> Cyclone <- C-force. (ii) VE: f1(L) = sum_C P(C) P(y|C,L) = (0.4175, 0.115); f2(L,T) = sum_P P(P) P(L|T,P) = (l,t) 0.62, (l, not t) 0.31; f3(T) = (0.30255, 0.208775); times P(T) gives (0.19666, 0.07307), so P(T-kick | cyclone) = 0.729. (iii) P(no cyclone | T, P) = 1 - [0.8(0.4175) + 0.2(0.115)] = 1 - 0.357 = 0.643."
sources: ["MNM slides Uncertainty-2-BN and Uncertainty-4-BN-INF (variable elimination)", "AIMA 3e sec. 14.2 and 14.4.2"]
---
**(i) Bayesian network** (8). Boolean variables: $T$ = T-kick, $P$ = P-kick, $L$ = low-pressure zone, $R$ = moderate rainfall, $C$ = C-force (Coriolis), $Y$ = tropical cyclone.

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
| $L\mid T,P$ | $(t,p)$ 0.80; $(t,\neg p)$ 0.35; $(\neg t,p)$ 0.45; $(\neg t,\neg p)$ 0.10 |
| $R\mid L$ | $P(r\mid l)=0.48$ |
| $C$ | $P(c)=0.25$ |
| $Y\mid C,L$ | $(c,l)$ 0.95; $(c,\neg l)$ 0.22; $(\neg c,l)$ 0.24; $(\neg c,\neg l)$ 0.08 |

**(ii) $P(T\mid y)$ by variable elimination** (12).

$$P(T\mid y)=\alpha\,P(T)\sum_pP(p)\sum_lP(l\mid T,p)\sum_cP(c)P(y\mid c,l)\sum_rP(r\mid l)$$

$\sum_rP(r\mid l)=1$, since $R$ is a barren leaf.

*Eliminate $C$:* $f_1(L)=\sum_cP(c)P(y\mid c,L)$.

$$f_1(l)=0.25(0.95)+0.75(0.24)=0.4175,\qquad f_1(\neg l)=0.25(0.22)+0.75(0.08)=0.115$$

*Eliminate $P$:* $f_2(L,T)=\sum_pP(p)P(L\mid T,p)$.

| | $t$ | $\neg t$ |
|:--|:-:|:-:|
| $l$ | $0.6(0.8)+0.4(0.35)=0.62$ | $0.6(0.45)+0.4(0.10)=0.31$ |
| $\neg l$ | 0.38 | 0.69 |

*Eliminate $L$:* $f_3(T)=\sum_lf_2(l,T)f_1(l)$.

$$f_3(t)=0.62(0.4175)+0.38(0.115)=0.30255$$

$$f_3(\neg t)=0.31(0.4175)+0.69(0.115)=0.20878$$

*Multiply by $P(T)$ and normalize:* $0.65\times0.30255=0.19666$ and $0.35\times0.20878=0.07307$, with sum $P(y)=0.26973$.

$$P(\text{T-kick}\mid\text{cyclone})=\frac{0.19666}{0.26973}=\mathbf{0.729}$$

**(iii) $P(\neg y\mid t,p)$** (8).

$$P(y\mid t,p)=\sum_lP(l\mid t,p)\,f_1(l)=0.8(0.4175)+0.2(0.115)=0.357$$

$$P(\text{no cyclone}\mid t,p)=1-0.357=\mathbf{0.643}$$

*Note:* $P(r\mid\neg l)$ is not given and is not needed.
