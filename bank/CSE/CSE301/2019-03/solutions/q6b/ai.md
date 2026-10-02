---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Node matrix $M=\begin{pmatrix}n&n''\\m&m''\end{pmatrix}$ (ancestors $\frac mn$, $\frac{m''}{n''}$), root $=I$; going left/right multiplies by $L=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $R=\begin{pmatrix}1&0\\1&1\end{pmatrix}$. Algorithm: while $m\ne n$: if $m<n$ output L, $n:=n-m$; else output R, $m:=m-n$ (e.g. $\frac37=LLRR$).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (the Stern-Brocot tree: matrix representation (4.33)-(4.39))']
---
**Matrix representation.** Every fraction in the Stern-Brocot tree is the mediant $\frac{m+m'}{n+n'}$ of its nearest left ancestor $\frac mn$ and nearest right ancestor $\frac{m'}{n'}$. Describe the node by the matrix of its two ancestors,

$$M=\begin{pmatrix}n&n'\\m&m'\end{pmatrix},\qquad f(M)=\frac{m+m'}{n+n'}$$

The root $\frac11$ has ancestors $\frac01$ and $\frac10$, so $M(\text{root})=\begin{pmatrix}1&0\\0&1\end{pmatrix}=I$.

**Going left.** The left child of $\frac{m+m'}{n+n'}$ lies between $\frac mn$ and the node itself, so its ancestors are $\frac mn$ and $\frac{m+m'}{n+n'}$:

$$M(SL)=\begin{pmatrix}n&n+n'\\m&m+m'\end{pmatrix}=\begin{pmatrix}n&n'\\m&m'\end{pmatrix}\begin{pmatrix}1&1\\0&1\end{pmatrix}$$

$$L=\begin{pmatrix}1&1\\0&1\end{pmatrix}$$

**Going right.** The right child lies between the node and $\frac{m'}{n'}$:

$$M(SR)=\begin{pmatrix}n+n'&n'\\m+m'&m'\end{pmatrix}=\begin{pmatrix}n&n'\\m&m'\end{pmatrix}\begin{pmatrix}1&0\\1&1\end{pmatrix}$$

$$R=\begin{pmatrix}1&0\\1&1\end{pmatrix}$$

So a path $S$ (a string of L's and R's from the root) corresponds to the product of the matrices: $M(S)=$ the product of $L$'s and $R$'s in the same order, and the fraction at the node is $f(M(S))$. For example $M(LRR)=LRR=\begin{pmatrix}3&1\\2&1\end{pmatrix}$, so $f=\frac{2+1}{3+1}=\frac34$.

**Algorithm (representing $\frac ab$ with $a\perp b$ as a string of L's and R's).**

```text
S := I                                  { the root, 1/1 }
while a/b != f(S):
    if a/b < f(S):  output "L";  S := S * L
    else:           output "R";  S := S * R
```

Equivalently, without matrices, using $m=a$, $n=b$:

```text
while m != n:
    if m < n:  output "L";  n := n - m
    else:      output "R";  m := m - n
```

*Why the short version works:* $\frac mn<1$ exactly when the fraction is in the left subtree of the root, and the left subtree is the whole tree transformed by $\frac mn\mapsto\frac{m}{n+m}$ (that is what $L$ does), so after an L we continue with $\frac{m}{n-m}$; similarly after an R we continue with $\frac{m-n}{n}$.

**Example.** $\frac37$: $(3,7)\to L\to(3,4)\to L\to(3,1)\to R\to(2,1)\to R\to(1,1)$, so $\frac37=LLRR$. (Check: $\frac11\to\frac12\to\frac13\to\frac25\to\frac37$.)
