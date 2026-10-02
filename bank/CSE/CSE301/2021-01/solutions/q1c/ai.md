---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Multinomial theorem: $\frac{9!}{3!\,3!\,1!\,2!}(1)^3(-1)^3(2)^1(-2)^2=5040\times(-8)=-40320$.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 5 (the multinomial theorem)']
---
By the multinomial theorem,

$$(y_1+y_2+y_3+y_4)^9=\sum_{n_1+n_2+n_3+n_4=9}\frac{9!}{n_1!\,n_2!\,n_3!\,n_4!}\,y_1^{n_1}y_2^{n_2}y_3^{n_3}y_4^{n_4}$$

Take $y_1=x_1$, $y_2=-x_2$, $y_3=2x_3$, $y_4=-2x_4$. The term $x_1^3x_2^3x_3x_4^2$ comes from $(n_1,n_2,n_3,n_4)=(3,3,1,2)$ (and $3+3+1+2=9$):

$$\frac{9!}{3!\,3!\,1!\,2!}\,(1)^3(-1)^3(2)^1(-2)^2$$

$$\frac{9!}{3!\,3!\,1!\,2!}=\frac{362880}{72}=5040,\qquad(1)^3(-1)^3(2)(-2)^2=-8$$

**Coefficient** $=5040\times(-8)=\mathbf{-40320}$.
