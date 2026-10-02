---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Each parent passes on $\alpha$ with probability $p_0+r_0/2$, independently, so $p=(p_0+\frac{r_0}{2})^2$, $q=(q_0+\frac{r_0}{2})^2$, $r=2(p_0+\frac{r_0}{2})(q_0+\frac{r_0}{2})$; these proportions then stay fixed (Hardy-Weinberg).'
sources: ['CSE301 Markov_Chain slides 25-29 (Hardy-Weinberg law)', 'Ross, Introduction to Probability Models, Ch. 4 (Hardy-Weinberg law)']
---
Each individual has two genes, so in the current population the fraction of all genes that are of type $\alpha$ is

$$P(\alpha)=p_0+\frac{r_0}{2}$$

because an $\alpha\alpha$ individual (proportion $p_0$) passes on $\alpha$ for sure and an $\alpha\beta$ individual (proportion $r_0$) passes on $\alpha$ with probability $\frac12$. Similarly

$$P(\beta)=q_0+\frac{r_0}{2},\qquad P(\alpha)+P(\beta)=1$$

With random mating, the gene contributed by each parent is an independent draw with these probabilities. So the offspring of the next generation have

$$p=P(\alpha\alpha)=\left(p_0+\frac{r_0}{2}\right)^2$$

$$q=P(\beta\beta)=\left(q_0+\frac{r_0}{2}\right)^2$$

$$r=P(\alpha\beta)=2\left(p_0+\frac{r_0}{2}\right)\left(q_0+\frac{r_0}{2}\right)$$

(the factor 2 because $\alpha$ may come from either parent). Indeed $p+q+r=\big(P(\alpha)+P(\beta)\big)^2=1$.

**Hardy-Weinberg law.** In the next generation the fraction of $\alpha$ genes is

$$p+\frac r2=P(\alpha)^2+P(\alpha)P(\beta)=P(\alpha)\big(P(\alpha)+P(\beta)\big)=p_0+\frac{r_0}{2}$$

the same as before. So from the first generation on, the proportions $p$, $q$, $r$ stay constant forever. Following one individual's descendants (one child per generation), the genotype is a Markov chain whose stationary distribution is exactly $(p,q,r)$.
