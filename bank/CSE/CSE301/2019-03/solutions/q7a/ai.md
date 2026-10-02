---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Root + left subtree ($k$ vertices) + right subtree ($n-1-k$): $b_0=1$, $b_n=\sum_{k=0}^{n-1}b_kb_{n-1-k}$, so $B(z)=1+zB(z)^2$, $B(z)=\frac{1-\sqrt{1-4z}}{2z}$, and $b_n=\frac{1}{n+1}\binom{2n}{n}$ (Catalan numbers: 1, 1, 2, 5, 14, 42, ...).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 7 (generating functions: binary trees and Catalan numbers)', 'Brualdi, Introductory Combinatorics, Ch. 8 (Catalan numbers)']
---
Let $b_n$ be the number of rooted ordered binary trees with $n$ vertices (each child is either a left or a right child; an empty tree has 0 vertices).

**Step 1: recurrence.** The empty tree gives $b_0=1$. A tree with $n\ge1$ vertices consists of a root, a left subtree with $k$ vertices and a right subtree with $n-1-k$ vertices, for some $0\le k\le n-1$, and the two subtrees can be chosen independently:

$$b_0=1,\qquad b_n=\sum_{k=0}^{n-1}b_k\,b_{n-1-k}\quad(n\ge1)$$

So $b_1=1$, $b_2=2$, $b_3=5$, $b_4=14$.

**Step 2: generating function.** Let $B(z)=\sum_{n\ge0}b_nz^n$. The sum is a convolution, so $\sum_{n\ge1}b_nz^n=z\,B(z)^2$:

$$B(z)=1+z\,B(z)^2$$

**Step 3: solve the quadratic.** $zB^2-B+1=0$ gives

$$B(z)=\frac{1\pm\sqrt{1-4z}}{2z}$$

We need $B(0)=b_0=1$ (finite), so we take the minus sign:

$$B(z)=\frac{1-\sqrt{1-4z}}{2z}$$

**Step 4: extract the coefficients.** By the binomial theorem, $\sqrt{1-4z}=\sum_{k\ge0}\binom{1/2}{k}(-4z)^k$, and

$$\binom{1/2}{k}(-4)^k=-\frac{2}{k}\binom{2k-2}{k-1}\qquad(k\ge1)$$

so $1-\sqrt{1-4z}=\sum_{k\ge1}\frac2k\binom{2k-2}{k-1}z^k$. Dividing by $2z$ and putting $n=k-1$:

$$B(z)=\sum_{n\ge0}\frac{1}{n+1}\binom{2n}{n}z^n$$

$$b_n=\frac{1}{n+1}\binom{2n}{n}=\frac{(2n)!}{n!\,(n+1)!}$$

These are the **Catalan numbers**: $1,1,2,5,14,42,132,\dots$ (they agree with the recurrence, checked up to $n=11$). For example, there are $b_3=\frac14\binom63=5$ binary trees with 3 vertices.
