---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Condition on the first step and use gambler''s ruin: $P=p\frac{1-q/p}{1-(q/p)^n}+q\frac{1-p/q}{1-(p/q)^n}=\frac{(p-q)(p^n+q^n)}{p^n-q^n}$ for $p\ne q$, and $1/n$ for $p=q=\frac12$.'
sources: ['CSE301 Markov_Chain slides 30-36 (gambler''s ruin)', 'Ross, Introduction to Probability Models, Ch. 4 (gambler''s ruin problem)']
---
Number the vertices $0,1,\dots,n$ clockwise around the circle; vertices $1$ and $n$ are the neighbours of $0$. Condition on the first step.

**First step clockwise (probability $p$), to vertex 1.** The particle visits every vertex before returning to 0 exactly when, starting from 1, it reaches vertex $n$ before vertex $0$. (Moving one step at a time between 0 and $n$ along the arc $1,2,\dots,n$, it must pass through all of them.) This is the gambler's ruin problem: fortune 1, target $n$, each step $+1$ with probability $p$ and $-1$ with probability $q$. With $r=q/p$,

$$P(\text{reach }n\text{ before }0\mid\text{start at }1)=\frac{1-q/p}{1-(q/p)^n}\qquad(p\ne q)$$

**First step counterclockwise (probability $q$), to vertex $n$.** By symmetry, it must now reach vertex 1 before 0 going the other way, which is gambler's ruin with the roles of $p$ and $q$ swapped:

$$P=\frac{1-p/q}{1-(p/q)^n}\qquad(p\ne q)$$

**Combine.**

$$P(\text{all visited by }T)=p\,\frac{1-q/p}{1-(q/p)^n}+q\,\frac{1-p/q}{1-(p/q)^n}=\frac{p-q}{1-(q/p)^n}+\frac{q-p}{1-(p/q)^n}$$

Multiplying the first fraction by $p^n/p^n$ and the second by $q^n/q^n$ simplifies this to

$$P(\text{all visited by }T)=\frac{(p-q)(p^n+q^n)}{p^n-q^n}\qquad(p\ne q)$$

**Symmetric case $p=q=\frac12$.** Gambler's ruin gives $\frac1n$ for each direction, so

$$P(\text{all visited by }T)=\frac12\cdot\frac1n+\frac12\cdot\frac1n=\frac1n$$

(which is also the limit of the general formula as $p\to\frac12$). For example, with $n+1=5$ vertices and $p=0.7$ the formula gives $0.428$, and a simulation agrees.
