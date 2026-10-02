---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$72=2^3\cdot3^2$; $\epsilon_2(200!)=100+50+25+12+6+3+1=197$ and $\epsilon_3(200!)=66+22+7+2=97$, so the multiplicity of 72 is $\min(\lfloor197/3\rfloor,\lfloor97/2\rfloor)=\min(65,48)=48$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (factorial factors)']
---
**Factor 72.** $72=2^3\cdot3^2$, so $72^m$ divides $200!$ exactly when $2^{3m}$ and $3^{2m}$ both divide it.

**Prime multiplicities in $200!$** (Legendre: $\epsilon_p(n!)=\sum_{k\ge1}\lfloor n/p^k\rfloor$):

$$\epsilon_2(200!)=\left\lfloor\frac{200}{2}\right\rfloor+\left\lfloor\frac{200}{4}\right\rfloor+\left\lfloor\frac{200}{8}\right\rfloor+\left\lfloor\frac{200}{16}\right\rfloor+\left\lfloor\frac{200}{32}\right\rfloor+\left\lfloor\frac{200}{64}\right\rfloor+\left\lfloor\frac{200}{128}\right\rfloor$$

$$=100+50+25+12+6+3+1=197$$

$$\epsilon_3(200!)=\left\lfloor\frac{200}{3}\right\rfloor+\left\lfloor\frac{200}{9}\right\rfloor+\left\lfloor\frac{200}{27}\right\rfloor+\left\lfloor\frac{200}{81}\right\rfloor=66+22+7+2=97$$

**Multiplicity of 72.**

$$m=\min\left(\left\lfloor\frac{197}{3}\right\rfloor,\left\lfloor\frac{97}{2}\right\rfloor\right)=\min(65,\ 48)=\mathbf{48}$$

So $72^{48}$ divides $200!$ but $72^{49}$ does not (the factor 3 is the bottleneck).
