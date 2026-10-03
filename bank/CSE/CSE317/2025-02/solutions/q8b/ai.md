---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Evaluate the initial policy (L, L, R, R) by solving 4 linear equations with U(s5) = 10: U = (-34.76, -26.29, -1.46, 5.94, 10). Improvement gives Right in every state (e.g. s2: Q(R) = -8.12 > Q(L) = -28.10). New policy (R, R, R, R); a second round leaves it unchanged, so it is optimal."
sources: ["MNM slides MDP-1-SB (policy iteration: evaluation and improvement)", "AIMA 3e sec. 17.3"]
---
**Model.** States $s_1..s_5$, with rewards $R=(-5,-1,-1,-1,+10)$. $s_5$ is terminal, so $U(s_5)=R(s_5)=10$. An action goes the intended way with probability 0.8 and the opposite way with 0.2. Moving left from $s_1$ hits the wall, so the robot stays in $s_1$. $\gamma=0.9$.

**Initial policy** $\pi_0$: $s_1\leftarrow$, $s_2\leftarrow$, $s_3\rightarrow$, $s_4\rightarrow$.

**Step 1: policy evaluation.** Use $U(s)=R(s)+\gamma\sum_{s'}P(s'\mid s,\pi_0(s))\,U(s')$, one linear equation per state:

$$U_1=-5+0.9\,[0.8\,U_1+0.2\,U_2]\quad(\text{L from }s_1\text{: wall, stay})$$

$$U_2=-1+0.9\,[0.8\,U_1+0.2\,U_3]$$

$$U_3=-1+0.9\,[0.8\,U_4+0.2\,U_2]$$

$$U_4=-1+0.9\,[0.8\,U_5+0.2\,U_3]=6.2+0.18\,U_3$$

Simplified:

$$0.28\,U_1=-5+0.18\,U_2$$

$$U_2=-1+0.72\,U_1+0.18\,U_3$$

$$U_3=-1+0.72\,U_4+0.18\,U_2$$

$$U_4=6.2+0.18\,U_3$$

Solving the linear system:

| | $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ |
|:--|:-:|:-:|:-:|:-:|:-:|
| $U^{\pi_0}$ | $-34.76$ | $-26.29$ | $-1.46$ | $5.94$ | $10$ |

(Check for $s_4$: $6.2+0.18(-1.46)=5.94$.)

**Step 2: policy improvement.** $\pi_1(s)=\arg\max_a\sum_{s'}P(s'\mid s,a)\,U^{\pi_0}(s')$:

| State | Left: $0.8\,U(\text{left})+0.2\,U(\text{right})$ | Right: $0.8\,U(\text{right})+0.2\,U(\text{left})$ | $\pi_1$ |
|:-:|:-:|:-:|:-:|
| $s_1$ | $0.8(-34.76)+0.2(-26.29)=-33.06$ | $0.8(-26.29)+0.2(-34.76)=-27.98$ | R |
| $s_2$ | $0.8(-34.76)+0.2(-1.46)=-28.10$ | $0.8(-1.46)+0.2(-34.76)=-8.12$ | R |
| $s_3$ | $0.8(-26.29)+0.2(5.94)=-19.84$ | $0.8(5.94)+0.2(-26.29)=-0.51$ | R |
| $s_4$ | $0.8(-1.46)+0.2(10)=0.84$ | $0.8(10)+0.2(-1.46)=7.71$ | R |

(For $s_1$, "left" is $s_1$ itself, because of the wall.)

**Improved policy after one iteration:** $\pi_1=(\rightarrow,\rightarrow,\rightarrow,\rightarrow)$ for $s_1..s_4$.

*Check (one more iteration):* evaluating $\pi_1$ gives $U=(-5.12,\ 1.11,\ 4.21,\ 6.96,\ 10)$. Improving again leaves every action Right, so $\pi_1$ is already optimal.
