---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Shift to $y_A+y_B+y_C+y_D=13$ with $0\le y_A\le5$, $0\le y_B\le7$, $0\le y_C,y_D\le4$; inclusion-exclusion: $\binom{16}{3}-(120+56+165+165)+(10+10+1+1+20)=560-506+42=96$.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 6 (inclusion-exclusion, combinations with repetition)']
---
**Remove the lower bounds.** Put $y_A=X_A-1$, $y_B=X_B$, $y_C=X_C-4$, $y_D=X_D-2$. Then $X_A+X_B+X_C+X_D=20$ becomes

$$y_A+y_B+y_C+y_D=13,\qquad0\le y_A\le5,\ 0\le y_B\le7,\ 0\le y_C\le4,\ 0\le y_D\le4$$

The number of non-negative integer solutions of $y_1+\cdots+y_4=m$ is $\binom{m+3}{3}$.

**Without the upper bounds:** $\binom{13+3}{3}=\binom{16}{3}=560$.

**Inclusion-exclusion over the violated upper bounds.** Let $A_1$: $y_A\ge6$, $A_2$: $y_B\ge8$, $A_3$: $y_C\ge5$, $A_4$: $y_D\ge5$. Subtracting the lower limit leaves a smaller total:

| Event | Remaining total | Count |
|:-:|:-:|:-:|
| $A_1$ | $13-6=7$ | $\binom{10}{3}=120$ |
| $A_2$ | $13-8=5$ | $\binom83=56$ |
| $A_3$ | $13-5=8$ | $\binom{11}{3}=165$ |
| $A_4$ | $8$ | $165$ |
| $A_1A_2$ | $-1$ | 0 |
| $A_1A_3$, $A_1A_4$ | $2$ | $\binom53=10$ each |
| $A_2A_3$, $A_2A_4$ | $0$ | $\binom33=1$ each |
| $A_3A_4$ | $3$ | $\binom63=20$ |
| any three or four | negative | 0 |

$$N=560-(120+56+165+165)+(10+10+1+1+20)-0=560-506+42=\mathbf{96}$$

So there are **96** valid integer bandwidth allocations (a direct enumeration confirms 96).
