---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'States $(a,b)$ = (station A busy?, station B busy?). Balance equations give $P_{00}=\frac13$, $P_{10}=\frac29$, $P_{01}=\frac13$, $P_{11}=\frac19$. Consultation completed by $\frac{4P_{10}}{2(P_{00}+P_{01})}=\frac23$ of admitted patients; $L=P_{10}+P_{01}+2P_{11}=\frac79$; $W=L/\lambda_a=\frac{7/9}{4/3}=\frac{7}{12}$ hour (35 minutes).'
sources: ['CSE301 Queueing_Theory slides 26-31 (choosing a state space; balance equations) and 3-11 (Little''s law)', 'Ross, Introduction to Probability Models, Ch. 6 (limiting probabilities)']
---
Rates: arrivals $\lambda=2$ per hour, screening $\mu_A=4$ per hour, consultation $\mu_B=2$ per hour.

**(i) States.** Station A holds at most one patient (arrivals are admitted only when A is idle) and so does B (a patient who finds B busy leaves). Let the state be $(a,b)$ with $a=1$ if station A is busy and $b=1$ if station B is busy:

| From | To | Rate | Event |
|:-:|:-:|:-:|:--|
| $(0,0)$ | $(1,0)$ | 2 | patient admitted to A |
| $(1,0)$ | $(0,1)$ | 4 | screening done, B idle: patient goes to B |
| $(0,1)$ | $(0,0)$ | 2 | consultation done |
| $(0,1)$ | $(1,1)$ | 2 | patient admitted to A |
| $(1,1)$ | $(0,1)$ | 4 | screening done, B busy: patient leaves |
| $(1,1)$ | $(1,0)$ | 2 | consultation done |

**(ii) Steady-state probabilities.** Balance equations (rate out = rate in):

$$(0,0):\quad2P_{00}=2P_{01}$$

$$(1,0):\quad4P_{10}=2P_{00}+2P_{11}$$

$$(0,1):\quad(2+2)P_{01}=4P_{10}+4P_{11}$$

$$(1,1):\quad(4+2)P_{11}=2P_{01}$$

From the first and last equations, $P_{00}=P_{01}=x$ and $P_{11}=\frac x3$. Then $4P_{10}=2x+\frac{2x}{3}$, so $P_{10}=\frac{2x}{3}$ (the $(0,1)$ equation checks: $4x=\frac{8x}{3}+\frac{4x}{3}$). Normalising, $x+\frac{2x}{3}+x+\frac x3=3x=1$:

$$P_{00}=\frac13,\qquad P_{10}=\frac29,\qquad P_{01}=\frac13,\qquad P_{11}=\frac19$$

**(iii) Admitted patients who see the specialist.** Patients are admitted when A is idle, at rate (PASTA)

$$\lambda_a=\lambda\,(P_{00}+P_{01})=2\left(\frac13+\frac13\right)=\frac43\text{ per hour}$$

They reach the specialist when screening ends while B is idle, i.e. at rate $\mu_AP_{10}=4\cdot\frac29=\frac89$ per hour (equal to the consultation completion rate $\mu_B(P_{01}+P_{11})=2\cdot\frac49$). So the proportion is

$$\frac{8/9}{4/3}=\frac23$$

**(iv) Average number of patients in the clinic.**

$$L=1\cdot P_{10}+1\cdot P_{01}+2\cdot P_{11}=\frac29+\frac39+\frac29=\frac79\approx0.78$$

**(v) Average time an admitted patient spends in the clinic.** By Little's law,

$$W=\frac{L}{\lambda_a}=\frac{7/9}{4/3}=\frac{7}{12}\text{ hour}=35\text{ minutes}$$

(Check: every admitted patient spends $\frac14$ hour in screening and, with probability $\frac23$, a further $\frac12$ hour in consultation: $\frac14+\frac23\cdot\frac12=\frac{7}{12}$.)
