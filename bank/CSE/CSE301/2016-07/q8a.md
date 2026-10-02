---
marks: 13
topics: [queue-ctmc-models]
kind: analysis
source: {page: 45}
note: "Marks printed as 4+3+3+3."
---
Customers arrive at a single-server station in accordance with a Poisson process with rate $\lambda$. All arrivals that find the server free immediately enter service. All service times are exponential distributed with rate $\mu$. An arrival that finds the server busy will leave the system and roam around "in orbit" for an exponential time with rate $\theta$ at which time it will then return. If the server is busy when an orbiting customer returns, then that customer returns to orbit for another exponential time with rate $\theta$ before returning again. An arrival that finds the server busy and $N$ other customers in orbit will depart and not return. That is, $N$ is the maximum number of customers in orbit.

(i) Define states.

(ii) Give the balance equations.

In terms of the solution of the balance equations, find

(iii) the proportion of all customers that are eventually served;

(iv) the average time that a served customer spends waiting in orbit.
