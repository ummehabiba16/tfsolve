---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "NUMA: single address space, remote access with LOAD/STORE, remote slower than local. Directory = 2^25 entries of 11 bits per node = 46 MB per node, about 1.07% of memory: feasible."
sources: ["Tanenbaum MOS 4e, sec. 8.1.3 (NUMA multiprocessors; directory-based cache coherence)"]
---
**Key characteristics of a NUMA machine** (Tanenbaum 8.1.3):

1. There is a **single address space** visible to all CPUs.
2. Access to **remote memory is by ordinary `LOAD` and `STORE`** instructions.
3. Access to remote memory is **slower** than access to local memory.

**Directory size.**

- Cache line $=128\text{ B}=2^7$ B; node memory $=4\text{ GB}=2^{32}$ B.
- Directory entries per node (one per local memory line): $2^{32}/2^{7}=2^{25}=33{,}554{,}432$.
- Each entry holds a **valid bit** and the **node number** of the node whose cache holds the line (the line may be cached by at most one node, as in Tanenbaum's design): $1+\log_2 1024 = 1+10 = 11$ bits.

$$\text{directory} = 2^{25}\times 11\text{ bits} = 369{,}098{,}752\text{ bits}\approx 46.1\text{ MB per node}$$

$$\text{overhead} = \frac{11\text{ bits}}{128\times 8\text{ bits}} = \frac{11}{1024}\approx \mathbf{1.07\%}$$

(Total memory $=1024\times4\text{ GB}=4\text{ TB}=2^{42}$ B, which fits in the 48-bit address space.)

**Feasibility.** An overhead of about 1% is small, so the scheme is **feasible**. Caveats: (a) the directory is looked up on every cache miss, so it must be fast (it is often kept in a special fast memory or the directory entries are cached); (b) 46 MB per node is too large for SRAM, so DRAM plus a small directory cache would be used; (c) this design records only *one* holder per line; allowing many sharers would need a bit-vector of 1024 bits per line (about 100% overhead), which is not feasible, so limited-pointer or coarse-vector schemes would then be used.
