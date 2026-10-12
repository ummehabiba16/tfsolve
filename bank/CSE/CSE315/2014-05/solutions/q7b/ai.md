---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Pentium (IA-32) segmentation can be used as: (1) basic flat model: one code and one data segment, both base 0 and limit 4 GB (segmentation effectively off); (2) protected flat model: same but limits set to the real memory, and separate user/supervisor segments, so out-of-range accesses fault; (3) multi-segment model: each program/task has its own code, data and stack segments (GDT/LDT), giving full segment protection; paging can be combined with any of them."
sources: ["Intel IA-32 Architectures Software Developer's Manual, Vol. 3, Sec. 3.2 (using segments: basic flat, protected flat, multi-segment models)", "Brey, The Intel Microprocessors, Sec. 2-5 (flat mode memory)"]
changes:
  - "2026-10-12: replaced the three ASCII sketches by TikZ figures (answer unchanged)"
---
The Pentium always uses segmentation in protected mode, but the operating system can choose how much of it to use:

**1. Basic flat model**

![Basic flat model](figures/flat.png)

The OS defines just **one code and one data segment**, both with **base 0 and limit 4 GB**. All segment registers point to them, so linear address = offset: the program sees a single flat 4 GB space. Segmentation is effectively switched off (no protection from it).

**2. Protected flat model**

![Protected flat model](figures/protflat.png)

Like the flat model, but the **limits are set to the actual memory size**, so an access beyond existing memory causes a general protection fault, and **separate code/data segments for user (PL 3) and supervisor (PL 0)** give two privilege levels. Usually combined with **paging** for per-page protection (this is how Windows and Linux use the Pentium).

**3. Multi-segment model**

![Multi-segment model](figures/multi.png)

Each program or task has **its own code, data and stack segments** (with their own bases, limits and access rights in the GDT/LDT). This uses the **full segment protection**: limit checks per segment, read-only/execute-only segments, privilege levels and separate address spaces per task.

In all three models **paging** can be enabled underneath to map the linear addresses to physical memory and provide virtual memory.
