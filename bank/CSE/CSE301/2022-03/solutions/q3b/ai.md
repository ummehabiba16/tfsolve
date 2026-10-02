---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'A dominant parent ($AA$ or $Aa$) passes on $a$ with probability $\frac{r/2}{p+r}$, a recessive parent always does; so $S_{10}=\frac{r}{2(p+r)}$ and $S_{11}=\left(\frac{r}{2(p+r)}\right)^2=S_{10}^2$.'
sources: ['CSE301 Markov_Chain slides 25-29 (Hardy-Weinberg law)', 'Ross, Introduction to Probability Models, Ch. 4 (Hardy-Weinberg law)']
---
An offspring is recessive ($aa$) exactly when **both** parents pass on an $a$ gene. Parents are chosen at random from the stabilized population (proportions $p$, $q$, $r$ for $AA$, $aa$, $Aa$), and each parent passes on one of its two genes at random, independently of the other parent.

**Probability that a dominant parent passes on $a$.** A dominant individual is $AA$ or $Aa$, so

$$P(AA\mid\text{dominant})=\frac{p}{p+r},\qquad P(Aa\mid\text{dominant})=\frac{r}{p+r}$$

An $AA$ parent never passes on $a$, and an $Aa$ parent passes on $a$ with probability $\frac12$:

$$P(\text{dominant parent passes }a)=\frac{p}{p+r}\cdot0+\frac{r}{p+r}\cdot\frac12=\frac{r}{2(p+r)}$$

A recessive parent ($aa$) passes on $a$ with probability 1.

**$S_{10}$: one dominant and one recessive parent.**

$$S_{10}=\frac{r}{2(p+r)}\cdot1=\frac{r}{2(p+r)}$$

**$S_{11}$: two dominant parents** (independently chosen):

$$S_{11}=\frac{r}{2(p+r)}\cdot\frac{r}{2(p+r)}=\left(\frac{r}{2(p+r)}\right)^2$$

Therefore

$$S_{11}=S_{10}^2$$

(Since the population has stabilized, Hardy-Weinberg gives $q=P(a)^2$ with $P(a)=q+\frac r2=\sqrt q$, and then $S_{10}=\frac{\sqrt q}{1+\sqrt q}$ and $S_{11}=\frac{q}{(1+\sqrt q)^2}$.)
