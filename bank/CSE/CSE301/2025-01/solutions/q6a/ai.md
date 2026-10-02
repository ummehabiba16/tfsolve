---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Terms are $x^ay^bz^c$ with $a+b+c=9$, $a,b,c\ge0$; by stars and bars there are $\binom{9+2}{2}=55$ of them.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 3 and 5 (combinations with repetition, multinomial theorem)']
---
By the multinomial theorem,

$$(x+y+z)^9=\sum_{a+b+c=9}\frac{9!}{a!\,b!\,c!}\,x^ay^bz^c$$

and every coefficient is positive, so no terms cancel. The number of terms is the number of non-negative integer solutions of

$$a+b+c=9$$

**Stars and bars.** Such a solution corresponds to a row of 9 stars and 2 bars (the bars split the stars into three groups of sizes $a,b,c$). Choosing the positions of the 2 bars among $11$ places:

$$\binom{9+3-1}{3-1}=\binom{11}{2}=\mathbf{55}$$

(In general, $(x_1+\cdots+x_k)^n$ has $\binom{n+k-1}{k-1}$ terms.)
