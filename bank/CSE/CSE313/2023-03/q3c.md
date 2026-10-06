---
marks: 15
topics: [producer-consumer-race]
kind: analysis
source: {page: 20}
note: "In the scan the function headers read 'void *producer (void *arg) (' and 'void *consumer (void *arg) (' with a round bracket instead of '{'. Transcribed as printed."
---
Consider the producer/consumer problem and the (broken) solution mentioned below. Briefly describe why solution is broken, and demonstrate it with a specific example of thread interleaving (*Hint: you can assume two consumers and one producer*).

**Producer**

```c
void *producer (void *arg) (
  int i;
  while (1) {
      mutex_lock (&mutex);                //p1
      if (count == MAX)                   //p2
        cond_wait(&empty, &mutex);        //p3
      put (i);                            //p4
      cond_signal (&full);                //p5
      mutex_unlock (&mutex);              //p6
  }
}
```

**Consumer**

```c
void *consumer (void *arg) (
  int i;
  while (1) {
      mutex_lock (&mutex);                //c1
      if (count == 0)                     //c2
          cond_wait (&full, &mutex);      //c3
      int tmp = get ();                   //c4
      cond_signal (&empty);               //c5
      mutex_unlock (&mutex);              //c6
      printf ("%d\n", tmp);
  }
}
```
