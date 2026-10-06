---
marks: 15
topics: [producer-consumer-semaphores]
kind: analysis
source: {page: 19}
---
The variable **counter**, is shared within process A and process B. The initial value is `counter = 0` before execution of either process. Here, `R0` is a register.

| Process A | Process B |
|:--|:--|
| `LOAD (counter, R0)` | `LOAD (counter, R0)` |
| `ADD (R0, 1, R0)` | `ADD (R0, 2, R0)` |
| `STORE (R0, counter)` | `STORE (R0, counter)` |

i. Add semaphores (with initial values) so that the final value of counter **is 2**.

ii. Add semaphores (with initial values) so that the final value of counter is **not 3**.
