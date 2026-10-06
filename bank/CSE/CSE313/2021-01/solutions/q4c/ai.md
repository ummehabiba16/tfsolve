---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Banker's algorithm needs the maximum demands in advance, a fixed set of processes and resources, and is expensive; circular wait is eliminated by a global resource ordering."
sources: ["Tanenbaum MOS 4e, sec. 6.5.4 and sec. 6.6.4 (attacking circular wait)"]
---
**Why Banker's algorithm is not useful in practice.**

- It needs every process to **declare its maximum resource needs in advance**, which is generally unknown.
- It assumes a **fixed number of processes** and of resources; in real systems processes come and go and resources (devices) can break.
- It must run on **every request** and costs $O(m\,n^2)$ for $n$ processes and $m$ resource types, which is too slow.
- It assumes that processes are independent (no synchronisation constraints) and is very conservative, so it limits concurrency.

**Eliminating circular wait (prevention).** Impose a **global numbering of all resources** and require that a process may request resources only in **increasing order of number**: a process holding resource $i$ may request only a resource $j>i$. (A weaker variant: a process may hold only one resource at a time.)

*Why it works:* in a resource graph, an arrow from a process to a resource goes to a higher-numbered resource, and a resource points to the holding process, so a cycle would need a process to hold a resource with a higher number while waiting for one with a lower number, which is forbidden. Example: number the scanner 1 and the printer 2; every process must request the scanner before the printer, so a process holding the printer can never wait for the scanner, and no cycle of waiting processes can form.
