---
marks: 9
topics: [buffer-cache]
kind: code
source: {page: 58-59}
---
Describe the "continue" statements in the given algorithm for buffer allocation in UNIX using illustrative examples.

```text
algorithm getblk
input:  file system number
        block number
output: locked buffer that can now be used for block
{
    while (buffer not found)
    {
        if (block in hash queue)
        {
            if (buffer busy)
            {
                sleep (event buffer becomes free);
                continue;
            }
            mark buffer busy;
            remove buffer from free list;
            return buffer;
        }
        else
        {
            if (there are no buffers on free list)
            {
                sleep (event any buffer becomes free);
                continue;
            }
            remove buffer from free list;
            if (buffer marked for delayed write) {
                asynchronous write buffer to disk;
                continue;
            }
            remove buffer from old hash queue;
            put buffer onto new hash queue;
            return buffer;
        }
    }
}
```

*Algorithm for Question 8 (b)*
