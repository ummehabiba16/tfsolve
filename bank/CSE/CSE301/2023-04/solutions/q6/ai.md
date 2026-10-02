---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(a) First failure time $=\min$ of 100 $\text{Expo}(1/2)$ $\sim\text{Expo}(50)$/year: $P(>1\text{ yr})=e^{-50}\approx1.9\times10^{-22}$. (b) With failed devices replaced, failures are Poisson with rate $50/12$ per month: $P(10)=e^{-50/12}(50/12)^{10}/10!\approx0.0067$. (c) Constant failure rate ignores infant mortality and wear-out, so it is only a rough model.'
sources: ['Ross, Introduction to Probability Models, Ch. 5 (exponential distribution, minimum of exponentials, Poisson process)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 5']
---
Each device's lifetime is $\text{Expo}(\lambda)$ with $\lambda=\frac12$ per year (mean 2 years), independently.

**(a) First failure after 1 year.** The first failure happens at $T=\min(T_1,\dots,T_{100})$, and

$$P(T>t)=\prod_{i=1}^{100}P(T_i>t)=\left(e^{-t/2}\right)^{100}=e^{-50t}$$

so $T\sim\text{Expo}(100\lambda)=\text{Expo}(50)$ per year (mean $\frac{1}{50}$ year, about a week). Hence

$$P(T>1\text{ year})=e^{-50}\approx1.9\times10^{-22}$$

i.e. it is practically certain that some device fails within the first year.

**(b) Exactly 10 failures in the 13th month.** In a data centre a failed device is replaced at once. With 100 devices always in service, each failing at rate $\frac12$ per year (memoryless), failures form a Poisson process with rate

$$100\times\frac12=50\text{ per year}=\frac{50}{12}\approx4.167\text{ per month}$$

By stationary increments, the number of failures in the 13th month (like any month) is Poisson with mean $\frac{50}{12}$:

$$P(N=10)=e^{-50/12}\frac{(50/12)^{10}}{10!}\approx\mathbf{0.0067}$$

*If failed devices are not replaced:* a device fails in the 13th month if it survives 12 months (probability $e^{-1/2}$) and then fails within one more month (probability $1-e^{-1/24}$), so the count is $\text{Bin}(100,\ 0.02475)$ and $P(10)=\binom{100}{10}(0.02475)^{10}(0.97525)^{90}\approx0.00016$.

**(c) Is the exponential model reasonable?** Only partly.

- The exponential distribution has a constant failure (hazard) rate: an old device is as reliable as a new one (memoryless property). Real storage devices follow a "bathtub" curve: a higher failure rate early on (manufacturing defects, infant mortality), a fairly flat middle period, and an increasing rate as they wear out. Field studies of disk failures find failure rates that clearly change with age.
- Failures in a data centre are also not fully independent (shared power, heat, firmware bugs, disks from the same batch).
- So the model is a reasonable first approximation for the middle period of the devices' life, with failed devices replaced, and it makes calculations such as (a) and (b) easy, but a Weibull or other ageing distribution is more realistic.
