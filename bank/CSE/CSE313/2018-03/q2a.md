---
marks: 12
topics: [buffer-cache]
kind: conceptual
source: {page: 37}
---
Consider a case when a process P is waiting for a buffer #99 to become free (currently process Q is using it). Is it possible (due to some race condition) that suddenly process P discovers buffer #99 is not in the buffer cache list? Explain with necessary diagram.
