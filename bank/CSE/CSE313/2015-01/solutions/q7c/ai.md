---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Compute-bound processes have long CPU bursts and rare I/O; I/O-bound processes have short CPU bursts between long waits (figure)."
sources: ["Tanenbaum MOS 4e, sec. 2.4.1 (fig. 2-39: bursts of CPU usage alternate with periods of waiting for I/O)"]
---
Processes alternate between **CPU bursts** (computing) and **I/O waits**:

```text
(a) compute-bound (CPU-bound) process:   long CPU bursts, rare short I/O waits
    |##########|.|##########|.|##########|.|##########|
(b) I/O-bound process:                   short CPU bursts, long waits for I/O
    |#|........|#|........|#|........|#|........|#|
    # = using the CPU    . = waiting for I/O
```

| | **Compute-bound** | **I/O-bound** |
|:--|:--|:--|
| Time spent | mostly **computing** | mostly **waiting for I/O** |
| CPU bursts | **long** | **short** (just enough to issue the next request) |
| Examples | scientific computation, compilers, video encoding | database queries, file copy, interactive programs |
| Scheduling | needs long uninterrupted CPU time; low priority is fine | should get the CPU **promptly** when it becomes ready, to keep the I/O devices busy |

The trend is that CPUs get faster than disks, so processes become more and more I/O-bound; scheduling should favour the I/O-bound ones.
