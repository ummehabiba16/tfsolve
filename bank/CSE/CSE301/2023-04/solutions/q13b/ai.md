---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$pq-p-q+2=(p-1)(q-1)+1$. Mod $p$: if $p\mid n$ both sides are $0$; otherwise $n^{p-1}\equiv1$ (Fermat), so $n^{(p-1)(q-1)+1}\equiv n$. Same mod $q$; since $p\perp q$, the congruence holds mod $pq$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (Fermat''s theorem, independent residues)', 'Supplementary materials attached to the paper (number theory, items 9 and 11)']
---
**Rewrite the exponent.**

$$pq-p-q+2=(p-1)(q-1)+1$$

**Modulo $p$.**

- If $p\mid n$: both $n^{(p-1)(q-1)+1}$ and $n$ are $\equiv0\pmod p$.
- If $p\nmid n$ (i.e. $n\perp p$): by Fermat's little theorem $n^{p-1}\equiv1\pmod p$, so

$$n^{(p-1)(q-1)+1}=\left(n^{p-1}\right)^{q-1}\cdot n\equiv1^{q-1}\cdot n=n\pmod p$$

So $n^{pq-p-q+2}\equiv n\pmod p$ for every integer $n$.

**Modulo $q$.** In exactly the same way (exchanging the roles of $p$ and $q$), $n^{(q-1)(p-1)+1}\equiv n\pmod q$.

**Combine.** $p$ and $q$ are distinct primes, so $p\perp q$, and by the supplementary rule $a\equiv b\pmod{mn}\iff a\equiv b\pmod m$ and $a\equiv b\pmod n$ (for $m\perp n$),

$$n^{pq-p-q+2}\equiv n\pmod{pq}\qquad\text{for every integer }n\ \blacksquare$$

(This is the fact behind RSA decryption, since $(p-1)(q-1)=\varphi(pq)$. Example: $p=3$, $q=5$: exponent $15-3-5+2=9$, and $2^9=512=34\cdot15+2\equiv2\pmod{15}$.)

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
