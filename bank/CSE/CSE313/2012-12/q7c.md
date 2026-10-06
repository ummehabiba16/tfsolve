---
marks: 15
topics: [mutex-requirements]
kind: code
source: {page: 69}
note: "The code is transcribed as printed: it uses 'id' inside the procedures while the parameter is 'process_id', and the types are printed 'Boolean' and 'Int'."
---
Verify whether the following code snippet solves the critical section problem for a two process environment. Two processes, say Process 1 and Process 2, running infinitely call **enter_critical_section** and **leave_critical_section** procedures with their corresponding ids before entering and after leaving the critical section respectively.

```c
Boolean blocked [2];
Int turn;

void enter_critical_section(int process_id)
{
    blocked[process_id] = true;
    while(turn != id) {
        while(blocked[1 - process_id]) {
            //do nothing
        }
        turn=id;
    }
}
void leave_critical_section(int process_id)
{
    blocked[id] = false;
}
```
