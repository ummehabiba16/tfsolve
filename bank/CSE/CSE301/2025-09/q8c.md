---
marks: 15
topics: [tandem-networks]
kind: numerical
source: {page: 4}
---
Consider a network of three stations, each with a single server. Customers arrive at stations 1, 2, and 3 according to independent Poisson processes with rates 5, 10, and 15 per hour, respectively. The service times at the stations are exponentially distributed with rates 10, 50, and 100 per hour, respectively. Upon completing service at station 1, a customer is equally likely to go to station 2, go to station 3, or leave the system. A customer completing service at station 2 always proceeds to station 3. A customer completing service at station 3 is equally likely to return to station 2 or leave the system.

(i) Compute the average number of customers in the system.

(ii) Determine the average time a customer spends in the system.

It is known that for an M/M/1 queue with arrival rate $\lambda$ and service rate $\mu$ that, the long-run probability of having $n$ customers in the system is $(1-\rho)\rho^n$ where $\rho=\frac{\lambda}{\mu}$, and the average number of customers in the system is $L=\frac{\rho}{1-\rho}$.
