---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\ell=n_o\log\theta+n_p\log(1-\theta)+g_o\log\theta_1+y_o\log(1-\theta_1)+g_p\log\theta_2+y_p\log(1-\theta_2)$ (base 10); maximising gives $\hat\theta=\frac{n_o}{n_o+n_p}$, $\hat\theta_1=\frac{g_o}{n_o}$, $\hat\theta_2=\frac{g_p}{n_p}$; with the data $\hat\theta=\frac{50}{90}\approx0.556$, $\hat\theta_1=\frac{30}{50}=0.6$, $\hat\theta_2=\frac{25}{40}=0.625$.'
sources: ['CSE301 MLE slides 4-8 (likelihood, MLE examples)', 'CSE301 Bayesian_Inference slides (Bayesian networks as factorised models)', 'Wasserman, All of Statistics, Ch. 9']
---
**Model.** The network $S\to L$ factorises the joint distribution as $P(S,L)=P(S)\,P(L\mid S)$:

$$P(\text{oak})=\theta,\quad P(\text{pine})=1-\theta,\quad P(\text{green}\mid\text{oak})=\theta_1,\quad P(\text{green}\mid\text{pine})=\theta_2$$

so a single tree has probability $\theta\theta_1$ (green oak), $\theta(1-\theta_1)$ (yellow oak), $(1-\theta)\theta_2$ (green pine) or $(1-\theta)(1-\theta_2)$ (yellow pine).

**(i) Log-likelihood.** With independent trees, the likelihood is the product over trees:

$$L=(\theta\theta_1)^{g_o}\,\big(\theta(1-\theta_1)\big)^{y_o}\,\big((1-\theta)\theta_2\big)^{g_p}\,\big((1-\theta)(1-\theta_2)\big)^{y_p}$$

Using $n_o=g_o+y_o$ and $n_p=g_p+y_p$, the base-10 log-likelihood is

$$\ell(\theta,\theta_1,\theta_2)=n_o\log\theta+n_p\log(1-\theta)$$

$$+\,g_o\log\theta_1+y_o\log(1-\theta_1)+g_p\log\theta_2+y_p\log(1-\theta_2)$$

**(ii) Maximising.** The log-likelihood splits into three separate terms, one for each parameter, so each can be maximised on its own. Since $\frac{d}{dx}\log_{10}x=\frac{1}{x\ln10}$, the constant $\frac{1}{\ln10}$ does not affect where the derivative vanishes:

$$\frac{\partial\ell}{\partial\theta}=\frac{1}{\ln10}\left(\frac{n_o}{\theta}-\frac{n_p}{1-\theta}\right)=0\ \Rightarrow\ \hat\theta=\frac{n_o}{n_o+n_p}$$

$$\frac{\partial\ell}{\partial\theta_1}=\frac{1}{\ln10}\left(\frac{g_o}{\theta_1}-\frac{y_o}{1-\theta_1}\right)=0\ \Rightarrow\ \hat\theta_1=\frac{g_o}{g_o+y_o}=\frac{g_o}{n_o}$$

$$\frac{\partial\ell}{\partial\theta_2}=\frac{1}{\ln10}\left(\frac{g_p}{\theta_2}-\frac{y_p}{1-\theta_2}\right)=0\ \Rightarrow\ \hat\theta_2=\frac{g_p}{g_p+y_p}=\frac{g_p}{n_p}$$

Each second derivative is negative (e.g. $-\frac{1}{\ln10}\big(\frac{n_o}{\theta^2}+\frac{n_p}{(1-\theta)^2}\big)<0$), so these are maxima. The MLEs are just the observed relative frequencies.

**(iii) Numerical estimates.** From Table 1: $g_o=30$, $y_o=20$, $n_o=50$, $g_p=25$, $y_p=15$, $n_p=40$, 90 trees in all.

$$\hat\theta=\frac{50}{90}=\frac59\approx0.556,\qquad\hat\theta_1=\frac{30}{50}=0.6,\qquad\hat\theta_2=\frac{25}{40}=0.625$$
