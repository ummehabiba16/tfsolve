---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The joint PDF is $1/(abc)$ on the box, so $X,Y,Z$ are independent uniforms: mean $(a/2,b/2,c/2)$, variances $a^2/12$, $b^2/12$, $c^2/12$ and zero covariances (total variance $(a^2+b^2+c^2)/12$).'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 5 (uniform distribution) and Ch. 7 (joint distributions)']
---
Let the point $(X,Y,Z)$ be uniform over the box $B=(0,a)\times(0,b)\times(0,c)$. Its joint PDF is constant on $B$ and integrates to 1 over a volume $abc$:

$$f(x,y,z)=\frac{1}{abc},\qquad 0<x<a,\ 0<y<b,\ 0<z<c$$

**Marginals and independence.** Integrating out $y$ and $z$,

$$f_X(x)=\int_0^c\!\int_0^b\frac{1}{abc}\,dy\,dz=\frac1a,\qquad 0<x<a$$

so $X\sim\text{Unif}(0,a)$; likewise $Y\sim\text{Unif}(0,b)$ and $Z\sim\text{Unif}(0,c)$. Since $f(x,y,z)=\frac1a\cdot\frac1b\cdot\frac1c=f_X(x)f_Y(y)f_Z(z)$, the three coordinates are independent.

**Mean and variance of each coordinate.**

$$E[X]=\int_0^a\frac{x}{a}\,dx=\frac a2,\qquad E[X^2]=\int_0^a\frac{x^2}{a}\,dx=\frac{a^2}{3}$$

$$\mathrm{Var}(X)=\frac{a^2}{3}-\frac{a^2}{4}=\frac{a^2}{12}$$

In the same way $E[Y]=b/2$, $\mathrm{Var}(Y)=b^2/12$, $E[Z]=c/2$ and $\mathrm{Var}(Z)=c^2/12$. By independence all covariances are 0; for example $\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]=\frac a2\cdot\frac b2-\frac a2\cdot\frac b2=0$.

**Answer.** The mean is the centre of the box and the covariance matrix is diagonal:

$$\boldsymbol\mu=\left(\frac a2,\ \frac b2,\ \frac c2\right)$$

$$\Sigma=\mathrm{diag}\!\left(\frac{a^2}{12},\ \frac{b^2}{12},\ \frac{c^2}{12}\right)$$

The total variance (the expected squared distance from the centre) is $\frac{a^2+b^2+c^2}{12}$. For a true cube ($a=b=c$): mean $(a/2,a/2,a/2)$, each variance $a^2/12$.
