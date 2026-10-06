---
marks: 6
topics: [producer-consumer-semaphores]
kind: code
source: {page: 41}
---
Consider the following code of producer process for a producer consumer system.

```c
semaphore empty = 10;
semaphore full = 0;
mutex m;
void producer(void) {
    int item;
    while(TRUE) {
        item = produce_item();
        lock(&m);
        down(&empty);
        insert_item(item);
        up(&full);
        unlock(&m);
    }
}
```

Will the above code work correctly? If not, explain the problems and write down the correct code for producer. If you think this code to be correct, write down the corresponding code for consumer.
