---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Number the resources and force every process to request them in increasing order: a cycle would need a decreasing request, which is forbidden."
sources: ["Tanenbaum MOS 4e, sec. 6.6.4 (attacking the circular wait condition)"]
---
**Method: global ordering of the resources.** Assign a unique **number** to every resource class and require that a process may request resources **only in increasing order of number**; a process holding resource $i$ can request only resources with number $>i$ (to get a lower one, it must first release).

**Example.** Number: 1 = scanner, 2 = CD recorder, 3 = printer. Process A holds the scanner (1) and requests the printer (3): allowed. Process B holds the printer (3) and wants the scanner (1): **not allowed** (1 < 3); B must release the printer first and ask in the order scanner, then printer.

Now A holding scanner and B holding printer waiting for the scanner is impossible, so the **circular wait** (A waits for B's resource while B waits for A's) can never arise: in a wait cycle every process would hold a resource with a number lower than the one it waits for, and going once around the cycle would give $n_1<n_2<\dots<n_1$, a contradiction. The weakness is that a numbering convenient for all processes may not exist.
