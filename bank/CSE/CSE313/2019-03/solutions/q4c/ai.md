---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Stable storage = two disks with stable write, stable read and crash recovery; a crash at any of five points leaves the block either wholly old or wholly new, so stable writes survive CPU crashes."
sources: ["Tanenbaum MOS 4e, sec. 5.4.4 (stable storage)"]
---
**Stable storage** is storage that is guaranteed to survive any single disk or CPU failure: a write is either completed or leaves the old value intact. It uses **two identical disks**; corresponding blocks form one error-free block. Block errors are detectable through the ECC.

**Three operations**

1. **Stable write:** write the block on disk 1 and verify by reading back (retry on error); only then write it on disk 2 and verify.
2. **Stable read:** read the block from disk 1; if the ECC is bad, retry, and finally read it from disk 2.
3. **Crash recovery:** after a crash scan both disks block by block: if both are good and equal, do nothing; if one has a bad ECC, copy the good one onto it; if both are good but different, copy disk 1's block to disk 2 (disk 1 is always written first).

**Surviving CPU crashes: all possible crash points during a stable write** (old value $o$, new value $n$):

| Crash occurs | State after the crash | Recovery action | Final value |
|:--|:--|:--|:-:|
| before disk 1 is written | disk 1 = $o$, disk 2 = $o$ | none | $o$ (write never happened) |
| during the write of disk 1 | disk 1 = bad ECC, disk 2 = $o$ | copy disk 2 $\to$ disk 1 | $o$ |
| after disk 1, before disk 2 | disk 1 = $n$, disk 2 = $o$ (both good, different) | copy disk 1 $\to$ disk 2 | $n$ |
| during the write of disk 2 | disk 1 = $n$, disk 2 = bad ECC | copy disk 1 $\to$ disk 2 | $n$ |
| after both disks | disk 1 = $n$, disk 2 = $n$ | none | $n$ |

In every case the recovered block is **either completely old or completely new, never garbage**, and both disks agree again; so the stable write is atomic with respect to a CPU crash.
