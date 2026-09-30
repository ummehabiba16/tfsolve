---
marks: 18
topics: [producer-consumer-semaphores]
kind: code
source: {page: 8}
---
Consider a variation of the classical producer consumer problem. In this variation, there is only one consumer and M producers P1, P2, ..., PM and all producers belong to the same priority class. Producers produce item in a cyclic order. For example, producer P1 produces first, then producer P2, and so on. After producer PM produces an item, it enables producer P1 to produce an item. Note that, the order of producing items and the order of insertion in the buffer may not always be the same. A solution to the classical Producer-Consumer problem is presented in Figure for 2(b). Modify this solution with minimal changes to obtain a solution for the above mentioned problem. [You do not need to write down the consumer code.]

*Figure for 2(b): Producer-Consumer problem using semaphores*

```c
#define N 100                         /* number of slots in the buffer */
typedef int semaphore;                /* semaphores are a special kind of int */
semaphore mutex = 1;                  /* controls access to critical region */
semaphore empty = N;                  /* counts empty buffer slots */
semaphore full = 0;                   /* counts full buffer slots */

void producer(void)
{
    int item;

    while (TRUE) {                    /* TRUE is the constant 1 */
        item = produce_item();        /* generate something to put in buffer */
        down(&empty);                 /* decrement empty count */
        down(&mutex);                 /* enter critical region */
        insert_item(item);            /* put new item in buffer */
        up(&mutex);                   /* leave critical region */
        up(&full);                    /* increment count of full slots */
    }
}

void consumer(void)
{
    int item;

    while (TRUE) {                    /* infinite loop */
        down(&full);                  /* decrement full count */
        down(&mutex);                 /* enter critical region */
        item = remove_item();         /* take item from buffer */
        up(&mutex);                   /* leave critical region */
        up(&empty);                   /* increment count of empty slots */
        consume_item(item);           /* do something with the item */
    }
}
```
