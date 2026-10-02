---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P\{T_1>t\}=P\{N(t)=0\}=e^{-\lambda t}$; given $T_1=s_1,\dots,T_{n-1}=s_{n-1}$, $P\{T_n>t\}=P\{\text{no event in }(s,s+t]\}=e^{-\lambda t}$ by independent and stationary increments, so the $T_n$ are i.i.d. $\text{Expo}(\lambda)$ with mean $1/\lambda$.'
sources: ['Ross, Introduction to Probability Models, Ch. 5 (interarrival and waiting time distributions)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 5 (Poisson processes)']
---
**Poisson process.** $\{N(t),t\ge0\}$ is a Poisson process with rate $\lambda$ if $N(0)=0$, it has independent increments, and the number of events in any interval of length $t$ is Poisson with mean $\lambda t$:

$$P\{N(s+t)-N(s)=k\}=e^{-\lambda t}\frac{(\lambda t)^k}{k!},\qquad k=0,1,2,\dots$$

**$T_1$.** The first event happens after time $t$ exactly when there is no event in $[0,t]$:

$$P\{T_1>t\}=P\{N(t)=0\}=e^{-\lambda t}$$

so $T_1\sim\text{Expo}(\lambda)$, with mean $1/\lambda$.

**$T_2$.** Condition on $T_1=s$:

$$P\{T_2>t\mid T_1=s\}=P\{0\text{ events in }(s,s+t]\mid T_1=s\}$$

$$=P\{0\text{ events in }(s,s+t]\}=e^{-\lambda t}$$

The second equality uses independent increments (what happens in $(s,s+t]$ does not depend on what happened in $[0,s]$), and the third uses stationary increments. The answer does not depend on $s$, so $T_2$ is independent of $T_1$ and $T_2\sim\text{Expo}(\lambda)$.

**General $T_n$.** In the same way, given $T_1=s_1,\dots,T_{n-1}=s_{n-1}$, with $s=s_1+\cdots+s_{n-1}$,

$$P\{T_n>t\mid T_1=s_1,\dots,T_{n-1}=s_{n-1}\}=P\{0\text{ events in }(s,s+t]\}=e^{-\lambda t}$$

which does not depend on $s_1,\dots,s_{n-1}$. Hence $T_1,T_2,\dots$ are independent, each exponential with rate $\lambda$, i.e. i.i.d. with mean $E[T_n]=\int_0^\infty e^{-\lambda t}\,dt=1/\lambda$.

(Intuitively: the process probabilistically restarts at every event, because of independent and stationary increments and the memoryless property.)
