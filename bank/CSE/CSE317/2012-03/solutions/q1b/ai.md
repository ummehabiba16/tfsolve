---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Prior P(elected) = 3/5 = 0.6; poll accuracy 98.5% in both directions. (i) P(elected | poll against) = 0.015 x 0.6 / (0.015 x 0.6 + 0.985 x 0.4) = 0.009/0.403 = 0.0223. (ii) P(defeated | poll in favour) = 0.015 x 0.4 / (0.015 x 0.4 + 0.985 x 0.6) = 0.006/0.597 = 0.0101."
sources: ["MNM slides Uncertainty-1-(quantifying) (Bayes rule)", "AIMA 3e sec. 13.5"]
---
**Model.** $E$ = the candidate is elected and $D=\neg E$ = defeated. The prior comes from the data: 3 in 5 people favour X, so $P(E)=0.6$ and $P(D)=0.4$. The poll is right 98.5% of the time:

$$P(\text{favor}\mid E)=0.985,\quad P(\text{against}\mid E)=0.015,\quad P(\text{against}\mid D)=0.985,\quad P(\text{favor}\mid D)=0.015.$$

**(i) $P(E\mid\text{against})$.**

$$P(E\mid\text{against})=\frac{P(\text{against}\mid E)P(E)}{P(\text{against}\mid E)P(E)+P(\text{against}\mid D)P(D)}$$

$$=\frac{0.015\times0.6}{0.015\times0.6+0.985\times0.4}$$

$$=\frac{0.009}{0.009+0.394}=\frac{0.009}{0.403}=\mathbf{0.0223}$$

**(ii) $P(D\mid\text{favor})$.**

$$P(D\mid\text{favor})=\frac{0.015\times0.4}{0.015\times0.4+0.985\times0.6}=\frac{0.006}{0.006+0.591}=\frac{0.006}{0.597}=\mathbf{0.0101}$$

*Note (assumptions):* "3 in 5 people are in favour" is taken as the prior probability that the candidate wins, and the 98.5% accuracy is taken to apply equally to both outcomes (sensitivity = specificity = 0.985).
