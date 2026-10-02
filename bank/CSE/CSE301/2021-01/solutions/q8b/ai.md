---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'While $j$ items are alive the next failure comes after an $\text{Expo}(j/200)$ time (minimum of $j$ exponentials), mean $\frac{200}{j}$ h. $E[T]=200\left(\frac1{100}+\frac1{99}+\frac1{98}+\frac1{97}+\frac1{96}\right)\approx10.21$ hours.'
sources: ['Ross, Introduction to Probability Models, Ch. 5 (minimum of exponentials, memoryless property)']
---
Each lifetime is exponential with mean 200 hours, i.e. rate $\lambda=\frac{1}{200}$ per hour.

**Time to the first failure.** With 100 items running, the first failure occurs at $\min(X_1,\dots,X_{100})$, which is exponential with rate $100\lambda$ (since $P(\min>t)=e^{-100\lambda t}$). Its mean is $\frac{1}{100\lambda}=\frac{200}{100}$ hours.

**Later failures.** By the memoryless property, at the moment of each failure the surviving items are "as good as new". After $i$ failures, $100-i$ items remain and the time to the next failure is exponential with rate $(100-i)\lambda$, mean $\frac{200}{100-i}$ hours.

**Expected duration of the test.** The test ends at the 5th failure, so its length is the sum of the first five inter-failure times:

$$E[T]=\sum_{i=0}^{4}\frac{200}{100-i}=200\left(\frac{1}{100}+\frac{1}{99}+\frac{1}{98}+\frac{1}{97}+\frac{1}{96}\right)$$

$$=200\times0.051031\approx\mathbf{10.21\ hours}$$

(Approximately $5\times2=10$ hours, slightly more because the failure rate drops as items fail.)
