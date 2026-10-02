---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Given $N_1$ passengers board at station 1, the number getting off at station 2 is $\text{Bin}(N_1,0.1)$, so $E=E[0.1N_1]=0.1(0\cdot0.3+1\cdot0.5+2\cdot0.2)=0.09$.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations by conditioning)']
---
Let $N_1$ be the number of passengers who get on at the 1st station and $Y$ the number who get off at the 2nd station. The bus arrives at station 1 empty, so nobody gets off there, and $N_1$ passengers are on board on the way to station 2:

$$E[N_1]=0(0.3)+1(0.5)+2(0.2)=0.9$$

At station 2 each of these $N_1$ passengers gets off independently with probability 0.1, so

$$Y\mid N_1\sim\text{Bin}(N_1,\ 0.1),\qquad E[Y\mid N_1]=0.1\,N_1$$

By the law of total expectation,

$$E[Y]=E\big[E[Y\mid N_1]\big]=0.1\,E[N_1]=0.1\times0.9=\mathbf{0.09}$$

(Check by conditioning explicitly: $E[Y]=0.3(0)+0.5(1\times0.1)+0.2(2\times0.1)=0.05+0.04=0.09$.)
