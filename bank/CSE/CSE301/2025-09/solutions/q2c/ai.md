---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Assuming independence, $z_1-z_2\sim N(0,2)$, so $|z_1-z_2|$ is half-normal: $f(y)=\frac{1}{\sqrt\pi}e^{-y^2/4}$ for $y\ge0$ (CDF $2\Phi(y/\sqrt2)-1$), with mean $2/\sqrt\pi\approx1.128$ and variance $2-4/\pi\approx0.727$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 6 (MGFs of sums) and Ch. 7 (expected distance between two Normals)']
---
Assume, as usual, that $z_1$ and $z_2$ are **independent** $N(0,1)$ random variables.

**Step 1: the distribution of $W=z_1-z_2$.** The MGF of $N(0,1)$ is $e^{t^2/2}$, and $-z_2\sim N(0,1)$ as well. By independence,

$$M_W(t)=M_{z_1}(t)\,M_{-z_2}(t)=e^{t^2/2}\,e^{t^2/2}=e^{2t^2/2}$$

which is the MGF of $N(0,2)$. So $W=z_1-z_2\sim N(0,2)$, with standard deviation $\sqrt2$.

**Step 2: the distribution of $Y=|W|$.** For $y\ge0$,

$$F_Y(y)=P(-y\le W\le y)=2\Phi\!\left(\frac{y}{\sqrt2}\right)-1$$

and $F_Y(y)=0$ for $y<0$. Differentiating,

$$f_Y(y)=\frac{2}{\sqrt2}\,\varphi\!\left(\frac{y}{\sqrt2}\right)=\frac{2}{\sqrt{2\pi\cdot2}}\,e^{-y^2/4}$$

$$f_Y(y)=\frac{1}{\sqrt{\pi}}\,e^{-y^2/4},\qquad y\ge0$$

So $|z_1-z_2|$ has a **half-normal distribution** with scale $\sigma=\sqrt2$, i.e. it has the same distribution as $\sqrt2\,|Z|$ with $Z\sim N(0,1)$.

**Mean and variance.**

$$E|z_1-z_2|=\int_0^\infty\frac{y}{\sqrt\pi}\,e^{-y^2/4}\,dy$$

$$=\frac{1}{\sqrt\pi}\Big[-2e^{-y^2/4}\Big]_0^\infty=\frac{2}{\sqrt\pi}\approx1.128$$

$$E\big[|z_1-z_2|^2\big]=\mathrm{Var}(W)=2,\qquad\mathrm{Var}|z_1-z_2|=2-\frac{4}{\pi}\approx0.727$$

Equivalently, $(z_1-z_2)^2/2\sim\chi^2_1$. (If $z_1,z_2$ had correlation $\rho$, the same steps give a half-normal with $\sigma^2=2(1-\rho)$.)
