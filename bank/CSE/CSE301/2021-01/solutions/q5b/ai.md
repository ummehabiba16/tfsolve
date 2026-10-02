---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Revenue $=15N_1+10N_2$, where $N_1$, $N_2$ are the numbers boarding at stops 1 and 2, each with mean $0(0.5)+1(0.4)+2(0.1)=0.6$. Expected revenue $=15(0.6)+10(0.6)=$ Tk. 15 (alightings do not affect it).'
sources: ['Ross, Introduction to Probability Models, Ch. 2-3 (expectation, linearity)']
---
The company charges per boarding: Tk. 15 for each passenger who gets on at the first stop and Tk. 10 for each who gets on at the second stop. Let $N_1$ and $N_2$ be the numbers of passengers boarding at stops 1 and 2. Then

$$\text{revenue}=15N_1+10N_2$$

(Passengers getting off, with probability 0.2 each, do not change the fares already paid, and the bus never fills up, so everyone who wants to board can.)

Each $N_i$ takes the values 0, 1, 2 with probabilities 0.5, 0.4, 0.1:

$$E[N_i]=0(0.5)+1(0.4)+2(0.1)=0.6$$

By linearity of expectation,

$$E[\text{revenue}]=15\,E[N_1]+10\,E[N_2]=15(0.6)+10(0.6)=9+6=\textbf{Tk. 15}$$

(If the revenue were instead counted per passenger **on board** when the bus leaves stop 2, the alighting probability would matter: the first-stop passengers still on board would have mean $0.6\times0.8=0.48$.)
