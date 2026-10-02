---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$11$ is prime and $11\nmid7$, so $7^{10}\equiv1\pmod{11}$ (Fermat); $10010=10\cdot1001$, so $7^{10010}=(7^{10})^{1001}\equiv1\pmod{11}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (Fermat''s theorem)']
---
$11$ is prime and $7\perp11$, so by Fermat's little theorem

$$7^{10}\equiv1\pmod{11}$$

The exponent is a multiple of 10: $10010=10\times1001$. Hence

$$7^{10010}=\left(7^{10}\right)^{1001}\equiv1^{1001}=1\pmod{11}$$

$$7^{10010}\bmod11=\mathbf{1}$$

(Check of Fermat here: $7^2=49\equiv5$, $7^4\equiv25\equiv3$, $7^5\equiv3\cdot7=21\equiv10\equiv-1$, so $7^{10}\equiv1\pmod{11}$.)
