---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "P(B | D = T, E = F) = alpha P(B) sum_C [sum_A P(A) P(C | A, B)] P(D | C) P(not E | C). P(c | b) = 0.356 and P(c | not b) = 0.103; P(d, not e | c) = 0.27 and P(d, not e | not c) = 0.0495; B = T: 0.3 x 0.128 = 0.0384, B = F: 0.7 x 0.0722 = 0.0505; P(B = T | D = T, E = F) = 0.432."
sources: ["MNM slides Uncertainty-4-BN-INF (exact inference)", "AIMA 3e sec. 14.4"]
---
**Network.** $A\to C\leftarrow B$, $C\to D$, $C\to E$:

$$P(A,B,C,D,E)=P(A)P(B)P(C\mid A,B)P(D\mid C)P(E\mid C).$$

**Query.** $P(B\mid d,\neg e)$, with hidden variables $A$ and $C$:

$$P(B\mid d,\neg e)=\alpha\,P(B)\sum_c\Big[\sum_aP(a)P(c\mid a,B)\Big]P(d\mid c)\,P(\neg e\mid c).$$

**Step 1: sum out $A$.** $f(C,B)=\sum_aP(a)P(C\mid a,B)$:

$$P(c\mid b)=0.1(0.95)+0.9(0.29)=0.095+0.261=0.356$$

$$P(c\mid\neg b)=0.1(0.94)+0.9(0.01)=0.094+0.009=0.103$$

**Step 2: evidence factor for each value of $C$.**

$$P(d\mid c)P(\neg e\mid c)=0.90\times0.30=0.27$$

$$P(d\mid\neg c)P(\neg e\mid\neg c)=0.05\times0.99=0.0495$$

**Step 3: sum out $C$ and multiply by $P(B)$.**

$$B=T:\ 0.3\,[0.356(0.27)+0.644(0.0495)]=0.3\,(0.09612+0.03188)=0.3\times0.12800=0.03840$$

$$B=F:\ 0.7\,[0.103(0.27)+0.897(0.0495)]=0.7\,(0.02781+0.04440)=0.7\times0.07221=0.05055$$

**Step 4: normalize.** $P(d,\neg e)=0.03840+0.05055=0.08895$.

$$P(B=T\mid D=T,E=F)=\frac{0.03840}{0.08895}=\mathbf{0.432},\qquad P(B=F\mid D=T,E=F)=0.568.$$

