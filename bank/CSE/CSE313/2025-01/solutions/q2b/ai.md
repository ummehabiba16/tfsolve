---
author: ai
via: chat
status: unverified
summary: Add one binary semaphore per producer forming a token ring so producing happens strictly in the order P1$\to$P2$\to$...$\to$PM$\to$P1; keep the original empty/full/mutex for insertion (which may reorder).
sources: [IPC slides 29-39, 'Tanenbaum, MOS 4e, sec. 2.3.5']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
Introduce $turn[0..M-1]$, binary semaphores, with $turn[0]=1$ and the rest 0. Producer $P_k$ (for $k=0,\dots,M-1$) becomes:

```c
void producer(int k) {          /* k = 0 .. M-1 */
    int item;
    while (TRUE) {
        down(&turn[k]);         /* wait my turn to PRODUCE */
        item = produce_item();
        up(&turn[(k+1) % M]);   /* let the next producer produce */
        down(&empty);           /* usual buffer protocol below */
        down(&mutex);
        insert_item(item);
        up(&mutex);
        up(&full);
    }
}
```

$down(turn[k])$ blocks $P_k$ until the token reaches it; after producing it passes the token with $up(turn[(k{+}1)\bmod M])$, so the produce order is strictly cyclic. Because the token is released before $down(empty)$/$mutex$, the buffer-insertion order can differ from the produce order, as required. The consumer is unchanged.
