---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A hybrid Bayesian network has both discrete and continuous variables. Continuous children of continuous (and discrete) parents use conditional linear Gaussians (the mean is linear in the continuous parents, with parameters chosen by the discrete parents); discrete children of continuous parents use a soft threshold (probit or logit). Example: Subsidy (discrete) and Harvest (continuous) -> Cost (linear Gaussian) -> Buys (probit)."
sources: ["AIMA 3e sec. 14.3 (efficient representation of conditional distributions, hybrid networks, Fig. 14.5-14.7)"]
---
**Hybrid Bayesian network.** A Bayesian network that contains **both discrete and continuous** random variables. Continuous variables have infinitely many values, so they cannot have CPTs. Their conditional distributions are given by **parametrized families** instead.

**Example** (AIMA): a customer buys fruit depending on its cost, which depends on the harvest size and on whether the government gives a subsidy.

```text
 Subsidy (discrete: T/F)     Harvest (continuous)
            \                     /
             v                   v
              Cost (continuous)
                    |
                    v
            Buys (discrete: T/F)
```

**How the four kinds of link are handled.**

1. **Discrete parent to discrete child:** an ordinary CPT.
2. **Continuous child with continuous parents** (Cost given Harvest): the **linear Gaussian** model. The child is Gaussian, with mean linear in the parent:

$$P(c\mid h,subsidy)=N(a_th+b_t,\ \sigma_t^2)(c)$$

3. **Continuous child with discrete parents** (Cost given Subsidy): enumerate the discrete parent values. Each value has its own linear-Gaussian parameters: $(a_t,b_t,\sigma_t)$ for subsidy and $(a_f,b_f,\sigma_f)$ for no subsidy. A network with only these kinds of continuous node is a **conditional Gaussian** network.
4. **Discrete child with a continuous parent** (Buys given Cost): a **soft threshold**. Either the probit model, $P(buys\mid c)=\Phi\big((-c+\mu)/\sigma\big)$ (the cumulative normal), or the logit (sigmoid) model, $P(buys\mid c)=\frac{1}{1+e^{-2(-c+\mu)/\sigma}}$. The probability of buying drops smoothly as the cost rises past the threshold $\mu$.

Inference sums over the discrete variables and integrates over the continuous ones. With linear-Gaussian nodes, the joint distribution of the continuous variables is a multivariate Gaussian, which keeps exact inference tractable.
