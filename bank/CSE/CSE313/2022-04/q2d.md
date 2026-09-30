---
marks: 5
topics: [producer-consumer-race]
kind: analysis
source: {page: 26}
note: Printed 'inset(item)' and 'remove-item()'; normalised to insert_item/remove_item in the figure file.
---
Explain the race-condition that exists in the following solution to the producer-consumer problem.

*Sleep/wakeup producer-consumer (Question 2(d))*

```c
#define N 100
int count = 0;

void producer(void)
{
    int item;
    while (TRUE) {
        item = produce();
        if (count == N) sleep();
        insert_item(item);
        count = count + 1;
        if (count == 1)
            wakeup(consumer);
    }
}

void consumer(void)
{
    int item;
    while (TRUE) {
        if (count == 0) sleep();
        item = remove_item();
        count = count - 1;
        if (count == N-1)
            wakeup(producer);
        consume(item);
    }
}
```
