---
marks: 7
topics: [producer-consumer-semaphores]
kind: code
source: {page: 61}
---
Consider the following code for the producer-consumer problem using semaphore.

```c
semaphore mutex = 1 ;
semaphore empty = 5;
semaphore full = 0;
```

**Producer**

```c
void producer(void)
{
    int item;
    while (TRUE) {
        item = produce_item();
        /*generate something to put in buffer*/
        down(&mutex);
        down(&empty);
        insert_item(item);
        /*put new item in buffer*/
        up(&mutex);
        up(&full);
    }
}
```

**Consumer**

```c
void consumer(void)
{
    int item;
    while (TRUE) {
        down(&full);
        down(&mutex);
        item = remove_ item();
        /*take item from buffer*/
        up(&mutex);
        up(&empty);
        consume_item(item);
        /*do something with the item*/
    }
}
```

The above code will work properly - Prove or disprove?
