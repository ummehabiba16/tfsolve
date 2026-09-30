---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
No. Interrupts are preferable when device events are relatively *infrequent*, since polling in that case would waste CPU cycles repeatedly checking a device that rarely has anything ready. However, when a device generates events extremely frequently (a very fast/high-rate device), using an interrupt for every single event introduces significant fixed overhead (trap, context switch into the handler, return) that can dominate the CPU's time and even lead to *receive livelock*, where the system does nothing but service interrupts and never makes forward progress on actual work. In that high-frequency case, **polling** (or a hybrid interrupt-then-poll scheme, e.g. Linux's NAPI) performs better, because it avoids the per-event trap overhead. So the right choice depends on the expected event rate, not a fixed preference for interrupts.
