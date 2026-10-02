---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Men''s hats must be a derangement of the $n$ male hats and women''s hats a derangement of the $n$ female hats, independently: $D_n^2=\left(n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}\right)^2$ ways.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 6 (derangements)']
---
Since every man gets a male hat, the $n$ male hats go to the $n$ men, and the $n$ female hats go to the $n$ women. These two assignments are independent of each other.

- No man gets his own hat: the men's hats form a derangement of $n$ objects, in $D_n$ ways.
- No woman gets her own hat: likewise $D_n$ ways.

By the multiplication principle the number of ways is

$$D_n\cdot D_n=D_n^2=\left(n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}\right)^2$$

where $D_n=n!\left(1-\frac1{1!}+\frac1{2!}-\cdots+\frac{(-1)^n}{n!}\right)\approx\frac{n!}{e}$. For example, $n=3$ gives $D_3^2=2^2=4$.
