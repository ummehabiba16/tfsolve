---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'MAP chooses the posterior mode: $\hat\theta_{MAP}=\arg\max_\theta f(\theta\mid x^n)=\arg\max_\theta[\ell(\theta)+\log f(\theta)]$. It reduces to the MLE $\arg\max_\theta\ell(\theta)$ when the prior is uniform (flat), since $\log f(\theta)$ is then constant; it also approaches the MLE as $n\to\infty$.'
sources: ['CSE301 Bayesian_Inference slides 8-9 (MAP estimation, MAP vs MLE) and 14-18 (Bernoulli example)', 'Wasserman, All of Statistics, Ch. 11']
---
**Maximum a posteriori (MAP) learning.** In the Bayesian approach the parameter $\theta$ has a prior density $f(\theta)$. After observing data $x^n=(x_1,\dots,x_n)$, Bayes' theorem gives the posterior

$$f(\theta\mid x^n)=\frac{L(\theta)f(\theta)}{\int L(\theta')f(\theta')\,d\theta'}\ \propto\ L(\theta)\,f(\theta)$$

where $L(\theta)=f(x^n\mid\theta)$ is the likelihood. The MAP estimate is the most probable parameter value after seeing the data, the mode of the posterior:

$$\hat\theta_{MAP}=\arg\max_\theta f(\theta\mid x^n)=\arg\max_\theta L(\theta)f(\theta)=\arg\max_\theta\big[\ell(\theta)+\log f(\theta)\big]$$

with $\ell(\theta)=\log L(\theta)$. The normalising constant does not depend on $\theta$, so it can be ignored. So MAP maximises the log-likelihood **plus** the log-prior: the prior acts as a penalty (regulariser) that pulls the estimate towards values the prior favours.

**When does it reduce to maximum likelihood?** The MLE maximises the log-likelihood alone, $\hat\theta_{MLE}=\arg\max_\theta\ell(\theta)$.

- **Uniform (flat) prior:** if $f(\theta)=c$ is constant over the parameter space, then $\log f(\theta)=\log c$ does not depend on $\theta$ and cannot move the maximiser, so $\hat\theta_{MAP}=\hat\theta_{MLE}$. MLE is MAP under a uniform prior.
- **Large samples:** $\ell(\theta)$ is a sum of $n$ terms and grows with $n$, while $\log f(\theta)$ stays fixed, so as $n\to\infty$ the data dominate and $\hat\theta_{MAP}\to\hat\theta_{MLE}$.

**Example (Bernoulli).** With $s$ successes in $n$ trials and a $\text{Beta}(\alpha,\beta)$ prior, the posterior is $\text{Beta}(s+\alpha,\ n-s+\beta)$ and

$$\hat p_{MAP}=\frac{s+\alpha-1}{n+\alpha+\beta-2},\qquad\hat p_{MLE}=\frac sn$$

They coincide for the uniform prior $\alpha=\beta=1$, and they agree in the limit $n\to\infty$ for any prior.
