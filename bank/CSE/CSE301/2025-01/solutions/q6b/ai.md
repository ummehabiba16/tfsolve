---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$10\equiv-1\pmod{11}$, so $n=\sum_kd_k10^k\equiv\sum_kd_k(-1)^k=S_{\text{odd}}-S_{\text{even}}\pmod{11}$ (positions counted from the units digit as position 1). Hence $11\mid n\iff11\mid(S_{\text{odd}}-S_{\text{even}})$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (congruences)']
---
Let $n$ have decimal digits $d_0,d_1,\dots,d_k$, where $d_0$ is the units digit:

$$n=d_0+d_1\cdot10+d_2\cdot10^2+\cdots+d_k\cdot10^k$$

Number the positions from the right, so that $d_0$ is in position 1 (odd), $d_1$ in position 2 (even), and so on. Let $S_{\text{odd}}=d_0+d_2+d_4+\cdots$ and $S_{\text{even}}=d_1+d_3+d_5+\cdots$.

**Key congruence.** $10=11-1\equiv-1\pmod{11}$. Congruences can be multiplied, so $10^j\equiv(-1)^j\pmod{11}$ for every $j\ge0$, and therefore

$$n\equiv d_0-d_1+d_2-d_3+\cdots=S_{\text{odd}}-S_{\text{even}}\pmod{11}$$

So $n$ and $S_{\text{odd}}-S_{\text{even}}$ leave the same remainder on division by 11, i.e. $11\mid n-(S_{\text{odd}}-S_{\text{even}})$.

**Both directions.**

- If $11\mid n$, then $11\mid n-\big(n-(S_{\text{odd}}-S_{\text{even}})\big)=S_{\text{odd}}-S_{\text{even}}$.
- If $11\mid S_{\text{odd}}-S_{\text{even}}$, then $11\mid(S_{\text{odd}}-S_{\text{even}})+\big(n-(S_{\text{odd}}-S_{\text{even}})\big)=n$.

Hence $11\mid n\iff11\mid(S_{\text{odd}}-S_{\text{even}})$. $\blacksquare$

(If the positions are counted from the left instead, the two sums may swap, which only changes the sign of the difference and not its divisibility by 11.)

**Example.** $918082$: from the right, $S_{\text{odd}}=2+0+1=3$ and $S_{\text{even}}=8+8+9=25$; the difference $-22$ is divisible by 11, and indeed $918082=11\times83462$.
