---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A buffer header holds the device and block number, status flags (locked, valid, delayed-write, being read/written, wanted), pointers to the data area, and the hash-queue and free-list links."
sources: ["Bach, ch. 3 (buffer headers)"]
---
A **buffer** has two parts: the **data area** (memory holding a copy of a disk block) and the **buffer header** (the control information). The header contains:

| Field | Purpose |
|:--|:--|
| **device number** | logical file-system/device the block belongs to |
| **block number** | which block of the device is in the buffer |
| **pointer to the data area** | where the copy of the disk block is in memory |
| **status flags** | *locked (busy)*; *valid* (the data is valid); *delayed write* (kernel must write it to disk before reuse); *kernel is currently reading/writing the buffer* (I/O in progress); *a process is waiting for the buffer to become free* |
| **pointers to next and previous buffer on the hash queue** | links of the doubly linked hash queue (chosen by hashing device and block number) |
| **pointers to next and previous buffer on the free list** | links of the doubly linked free list (valid only when the buffer is not busy) |

Together, the device and block number identify the cached block, the flags tell the kernel whether it can be used or must be written, and the two pairs of pointers allow fast lookup (hash queue) and LRU reuse (free list).
