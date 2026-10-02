---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'True. $ed=1+kt$ with $t=(p-1)(q-1)=\varphi(n)$, so $M''\equiv C^d\equiv M^{ed}=M\cdot\big(M^{\varphi(n)}\big)^k\equiv M\pmod n$ by Euler''s theorem ($M\perp n$).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (Euler''s totient function and Euler''s theorem)', 'Supplementary materials (number theory, items 13-14)']
---
**Yes, $M\equiv M'\pmod n$.**

**Proof.** Since $ed\equiv1\pmod t$, write $ed=1+kt$ for some integer $k\ge0$. For $n=pq$ with $p\ne q$ prime,

$$\varphi(n)=\varphi(p)\varphi(q)=(p-1)(q-1)=t$$

Bob computes

$$M'=C^d\bmod n,\qquad C=M^e\bmod n$$

so, working modulo $n$,

$$M'\equiv C^d\equiv\left(M^e\right)^d=M^{ed}=M^{1+kt}=M\cdot\left(M^{\varphi(n)}\right)^k\pmod n$$

Because $M\perp n$, Euler's theorem gives $M^{\varphi(n)}\equiv1\pmod n$. Therefore

$$M'\equiv M\cdot1^k=M\pmod n$$

So the statement is **true**: decryption recovers the message, and if $0\le M<n$ then $M'=M$ exactly. (This is why RSA works.)

**Remark.** The condition $M\perp n$ is not even necessary: if, say, $p\mid M$, then $M^{ed}\equiv0\equiv M\pmod p$, while $M^{ed}\equiv M\pmod q$ by Fermat; the Chinese Remainder Theorem then gives $M^{ed}\equiv M\pmod{pq}$.

**Tiny example.** $p=3$, $q=11$, $n=33$, $t=20$, $e=3$, $d=7$ ($21\equiv1\pmod{20}$). For $M=4$: $C=4^3\bmod33=31$ and $M'=31^7\bmod33=4$.
