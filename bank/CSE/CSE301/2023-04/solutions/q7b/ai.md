---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'From $P_{ij}(t+h)=\sum_kP_{ik}(h)P_{kj}(t)$ (backward) or $\sum_kP_{ik}(t)P_{kj}(h)$ (forward), letting $h\to0$ gives $\mathbf P^{\prime}(t)=\mathbf R\mathbf P(t)$ and $\mathbf P^{\prime}(t)=\mathbf P(t)\mathbf R$; the solution with initial value $\mathbf P(0)$ is $\mathbf P(t)=\mathbf P(0)e^{\mathbf Rt}$ (and $\mathbf P(0)=I$).'
sources: ['Ross, Introduction to Probability Models, Ch. 6 (Kolmogorov''s backward and forward equations)']
---
**Notation.** $q_{ij}$ ($i\ne j$) is the instantaneous rate from $i$ to $j$ and $\nu_i=\sum_{j\ne i}q_{ij}$ is the total rate out of $i$. For small $h$,

$$P_{ij}(h)=q_{ij}h+o(h)\ (i\ne j),\qquad1-P_{ii}(h)=\nu_ih+o(h)$$

Collect the rates in the matrix $\mathbf R$ with $r_{ij}=q_{ij}$ for $i\ne j$ and $r_{ii}=-\nu_i$ (each row sums to 0).

**Backward equations.** Use Chapman-Kolmogorov with the short interval first:

$$P_{ij}(t+h)=\sum_kP_{ik}(h)P_{kj}(t)$$

$$P_{ij}(t+h)-P_{ij}(t)=\sum_{k\ne i}P_{ik}(h)P_{kj}(t)-\big[1-P_{ii}(h)\big]P_{ij}(t)$$

Divide by $h$ and let $h\to0$ (the interchange of limit and sum is valid, e.g. for a finite state space):

$$P_{ij}'(t)=\sum_{k\ne i}q_{ik}P_{kj}(t)-\nu_iP_{ij}(t)\qquad\Longleftrightarrow\qquad\mathbf P'(t)=\mathbf R\,\mathbf P(t)$$

**Forward equations.** Now put the short interval last:

$$P_{ij}(t+h)=\sum_kP_{ik}(t)P_{kj}(h)$$

$$P_{ij}(t+h)-P_{ij}(t)=\sum_{k\ne j}P_{ik}(t)P_{kj}(h)-\big[1-P_{jj}(h)\big]P_{ij}(t)$$

$$P_{ij}'(t)=\sum_{k\ne j}P_{ik}(t)\,q_{kj}-\nu_jP_{ij}(t)\qquad\Longleftrightarrow\qquad\mathbf P'(t)=\mathbf P(t)\,\mathbf R$$

**Solution $\mathbf P(t)=\mathbf P(0)e^{\mathbf Rt}$.** Define the matrix exponential $e^{\mathbf Rt}=\sum_{n\ge0}\frac{(\mathbf Rt)^n}{n!}$, which satisfies $\frac{d}{dt}e^{\mathbf Rt}=e^{\mathbf Rt}\mathbf R$ (differentiate the series term by term). Then $\mathbf Y(t)=\mathbf P(0)e^{\mathbf Rt}$ satisfies

$$\mathbf Y'(t)=\mathbf P(0)e^{\mathbf Rt}\mathbf R=\mathbf Y(t)\,\mathbf R,\qquad\mathbf Y(0)=\mathbf P(0)$$

so $\mathbf Y$ solves the forward equation with the same initial value as $\mathbf P$. A linear system of ODEs with a given initial value has a unique solution, hence

$$\mathbf P(t)=\mathbf P(0)\,e^{\mathbf Rt}$$

Since $\mathbf P(0)=I$, this is $\mathbf P(t)=e^{\mathbf Rt}$; the same formula holds for the state distribution, $\mathbf p(t)=\mathbf p(0)e^{\mathbf Rt}$. (It also satisfies the backward equation, because $\mathbf R$ commutes with $e^{\mathbf Rt}$.)
