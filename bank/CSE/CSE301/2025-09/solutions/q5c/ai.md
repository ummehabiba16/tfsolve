---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) $T=\sum\frac{(O-E)^2}{E}=\frac{4+1+1+4+9}{20}=0.95<\chi^2_{4,0.05}=9.488$ (p-value $\approx0.917$): do not reject $H_0$; the sightings are consistent with a uniform distribution. (ii) Bonferroni threshold $0.05/4=0.0125$: none of the p-values $0.917,0.015,0.04,0.22$ is below it, so no test remains significant.'
sources: ['CSE301 Hypothesis_Test slides 23-27 (Pearson''s chi-squared test) and 32-34 (Bonferroni method)', 'Wasserman, All of Statistics, Ch. 10']
---
**(i) Chi-squared goodness-of-fit test.**

$H_0$: sightings are uniformly distributed over the 5 regions ($p_j=\frac15$ for each region), versus $H_1$: they are not. Under $H_0$ each expected count is $E_j=100\times\frac15=20$.

| Region | $O_j$ | $E_j$ | $O_j-E_j$ | $(O_j-E_j)^2/E_j$ |
|:--|:-:|:-:|:-:|:-:|
| North | 18 | 20 | $-2$ | 0.20 |
| South | 21 | 20 | 1 | 0.05 |
| East | 19 | 20 | $-1$ | 0.05 |
| West | 22 | 20 | 2 | 0.20 |
| Central | 17 | 20 | $-3$ | 0.45 |
| **Total** | 97 | 100 | | **0.95** |

Pearson's statistic:

$$T=\sum_{j=1}^{5}\frac{(O_j-E_j)^2}{E_j}=0.95$$

Under $H_0$, $T$ is approximately $\chi^2_{k-1}=\chi^2_4$ ($k=5$ categories, no parameters estimated). From the table, the critical value at $\alpha=0.05$ is

$$\chi^2_{4,\,0.05}=9.488$$

Since $T=0.95<9.488$, we **do not reject $H_0$**. The p-value is $P(\chi^2_4>0.95)=e^{-0.475}(1+0.475)\approx0.917$, far above 0.05.

**Conclusion:** at the 5% level there is no evidence against a uniform distribution; the differences between regions are well within chance variation. (The observed total is 97 rather than the 100 implied by the expected counts; using $E_j=97/5=19.4$ instead gives $T\approx1.09$ and the same conclusion.)

**(ii) Bonferroni method.** There are $m=4$ tests with p-values

$$P_1\approx0.917\ (\text{part (i)}),\qquad P_2=0.015,\qquad P_3=0.04,\qquad P_4=0.22$$

The Bonferroni method rejects $H_{0i}$ only if $P_i<\frac{\alpha}{m}=\frac{0.05}{4}=0.0125$. This keeps the probability of **any** false rejection at most $\alpha$ (by the union bound $P\big(\bigcup R_i\big)\le\sum P(R_i)\le m\cdot\frac{\alpha}{m}$).

| Test | p-value | $<0.0125$? |
|:-:|:-:|:-:|
| Forest of part (i) | 0.917 | no |
| Forest 2 | 0.015 | no |
| Forest 3 | 0.04 | no |
| Forest 4 | 0.22 | no |

**None of the four tests remains significant.** (Without the correction, forests 2 and 3 would have been significant at 5%; equivalently, the Bonferroni-adjusted p-values $\min(1,4P_i)=1,\ 0.06,\ 0.16,\ 0.88$ are all above 0.05.)

*Table used: [Chi-square distribution table (opens in a new tab)](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/chi-square-table.png).*
