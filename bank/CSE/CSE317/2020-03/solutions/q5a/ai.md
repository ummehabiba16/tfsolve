---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "P(v | A+) = 0.95(0.001) / [0.95(0.001) + 0.10(0.999)] = 0.0094; P(v | B+) = 0.90(0.001) / [0.90(0.001) + 0.05(0.999)] = 0.0177. A positive Test B is more indicative (about twice as likely to mean a real virus)."
sources: ["MNM slides Uncertainty-1-(quantifying) (Bayes' rule)", "AIMA 4e sec. 12.5"]
---
**Given.** $P(v)=0.001$; Test A: $P(A^+\mid v)=0.95$, $P(A^+\mid\neg v)=0.10$; Test B: $P(B^+\mid v)=0.90$, $P(B^+\mid\neg v)=0.05$. Only one test is done.

**Bayes' rule.**

$$P(v\mid T^+)=\frac{P(T^+\mid v)P(v)}{P(T^+\mid v)P(v)+P(T^+\mid\neg v)P(\neg v)}$$

**Test A positive.**

$$P(A^+)=0.95(0.001)+0.10(0.999)=0.00095+0.0999=0.10085$$

$$P(v\mid A^+)=\frac{0.00095}{0.10085}=\mathbf{0.0094}\ (0.94\%)$$

**Test B positive.**

$$P(B^+)=0.90(0.001)+0.05(0.999)=0.0009+0.04995=0.05085$$

$$P(v\mid B^+)=\frac{0.0009}{0.05085}=\mathbf{0.0177}\ (1.77\%)$$

**Conclusion.** $P(v\mid B^+)>P(v\mid A^+)$, so **a positive result from Test B is more indicative** of really carrying the virus, even though Test A is more sensitive.

The virus is rare, so almost all positives are false positives. The posterior is then driven by the false-positive rate: Test B's is half of Test A's. The likelihood ratios show the same: $0.95/0.10=9.5$ for A and $0.90/0.05=18$ for B.
