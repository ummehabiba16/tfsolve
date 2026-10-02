---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Vertical dominoes cost 4 and horizontal ones come in stacked pairs costing 2, so the generating function by worth is $\frac{1}{1-z^4-z^2}$ and the number of tilings worth exactly $m$ is $F_{m/2+1}$ for even $m$ and 0 for odd $m$ (e.g. 3 tilings for $m=6$). For a fixed width $n$: $\binom{v+h}{v}$ with $v=\frac{m-n}{3}$, $h=\frac{4n-m}{6}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 7 (domino tilings; exercise on the eccentric collector)', 'Supplementary materials (generating functions, item 1)']
---
**Structure of a $2\times n$ tiling.** Reading a tiling from left to right, it is a sequence of blocks of two kinds: a single **vertical** domino (width 1) or a pair of **horizontal** dominoes stacked on top of each other (width 2). This is why the number of tilings is the coefficient of $z^n$ in $T=\frac{1}{1-z-z^2}$, a Fibonacci number.

**Worth of the blocks.** A vertical domino is worth 4; a stacked pair of horizontal dominoes is worth $1+1=2$. Mark the worth with the variable $w$: a vertical block contributes $w^4$ and a horizontal pair $w^2$. A tiling is a sequence of blocks, so the generating function for tilings (of any width) by worth is

$$W(w)=\sum_{k\ge0}\left(w^4+w^2\right)^k=\frac{1}{1-w^2-w^4}$$

**Coefficients.** Put $u=w^2$: $W=\frac{1}{1-u-u^2}=\sum_jF_{j+1}u^j$. Hence

$$\#\{\text{tilings worth exactly }m\}=[w^m]\,\frac{1}{1-w^2-w^4}=\begin{cases}F_{m/2+1},&m\text{ even}\\0,&m\text{ odd}\end{cases}$$

**Examples.** $m=6$: $F_4=3$ tilings: six horizontal dominoes ($2\times6$), or one vertical domino plus one horizontal pair in either order ($2\times3$). $m=8$: $F_5=5$. (A computer enumeration of all tilings up to width 24 confirms the counts for $m\le20$.)

**If the width $n$ is fixed.** A tiling of the $2\times n$ rectangle with $v$ vertical dominoes and $h$ horizontal pairs has $v+2h=n$ and worth $4v+2h=m$. Solving,

$$v=\frac{m-n}{3},\qquad h=\frac{4n-m}{6}$$

and the blocks can be ordered in $\binom{v+h}{v}$ ways. So the number of $2\times n$ tilings worth $m$ is $\binom{v+h}{v}$ when $v$ and $h$ are non-negative integers, and 0 otherwise. In two variables, $\frac{1}{1-zw^4-z^2w^2}$ ($z$ marking width, $w$ worth).
