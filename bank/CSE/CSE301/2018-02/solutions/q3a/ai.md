---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Surjections from 16 people onto 5 rooms: $\sum_{j=0}^{5}(-1)^j\binom5j(5-j)^{16}=5!\,\genfrac\{\}{0pt}{}{16}{5}=131{,}542{,}866{,}000$.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 6 (inclusion-exclusion)', 'Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (Stirling numbers of the second kind)']
---
The 16 persons are distinguishable, the 5 rooms are distinguishable, and a room can hold any number of persons. An accommodation is a function from the persons to the rooms, and "no room empty" means the function is onto.

**Inclusion-exclusion.** There are $5^{16}$ functions in all. Let $A_i$ be the set of functions that leave room $i$ empty; any $j$ given rooms are empty in $(5-j)^{16}$ functions. So the number of onto functions is

$$\sum_{j=0}^{5}(-1)^j\binom5j(5-j)^{16}=5^{16}-5\cdot4^{16}+10\cdot3^{16}-10\cdot2^{16}+5\cdot1^{16}-0$$

| Term | Value |
|:--|--:|
| $5^{16}$ | 152,587,890,625 |
| $-5\cdot4^{16}$ | $-$21,474,836,480 |
| $+10\cdot3^{16}$ | 430,467,210 |
| $-10\cdot2^{16}$ | $-$655,360 |
| $+5\cdot1^{16}$ | 5 |
| **Total** | **131,542,866,000** |

**With Stirling numbers.** Equivalently, partition the 16 persons into 5 non-empty groups ($\genfrac\{\}{0pt}{}{16}{5}=1{,}096{,}190{,}550$ ways) and assign the groups to the 5 distinguishable rooms ($5!$ ways): $5!\cdot\genfrac\{\}{0pt}{}{16}{5}=120\times1{,}096{,}190{,}550=131{,}542{,}866{,}000$.

**Answer:** $\mathbf{131{,}542{,}866{,}000}$ ways. (If the rooms were indistinguishable, the answer would be $\genfrac\{\}{0pt}{}{16}{5}$.)
