---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Pentium (IA-32) segmentation can be used as: (1) basic flat model: one code and one data segment, both base 0 and limit 4 GB (segmentation effectively off); (2) protected flat model: same but limits set to the real memory, and separate user/supervisor segments, so out-of-range accesses fault; (3) multi-segment model: each program/task has its own code, data and stack segments (GDT/LDT), giving full segment protection; paging can be combined with any of them."
sources: ["Intel IA-32 Architectures Software Developer's Manual, Vol. 3, Sec. 3.2 (using segments: basic flat, protected flat, multi-segment models)", "Brey, The Intel Microprocessors, Sec. 2-5 (flat mode memory)"]
---
The Pentium always uses segmentation in protected mode, but the operating system can choose how much of it to use:

**1. Basic flat model**

```text
 CS --+
 DS --+--> one descriptor pair: base 0, limit 4 GB --> whole linear space 0 - FFFFFFFFh
 SS --+
```

The OS defines just **one code and one data segment**, both with **base 0 and limit 4 GB**. All segment registers point to them, so linear address = offset: the program sees a single flat 4 GB space. Segmentation is effectively switched off (no protection from it).

**2. Protected flat model**

```text
 CS, DS, SS (user, DPL 3) --> base 0, limit = size of physical memory
 CS, DS, SS (kernel, DPL 0) -> base 0, limit = size of physical memory
```

Like the flat model, but the **limits are set to the actual memory size**, so an access beyond existing memory causes a general protection fault, and **separate code/data segments for user (PL 3) and supervisor (PL 0)** give two privilege levels. Usually combined with **paging** for per-page protection (this is how Windows and Linux use the Pentium).

**3. Multi-segment model**

```text
 task 1: CS1, DS1, SS1 --> its own segments (LDT 1)
 task 2: CS2, DS2, SS2 --> its own segments (LDT 2)
 shared OS segments --> GDT
```

Each program or task has **its own code, data and stack segments** (with their own bases, limits and access rights in the GDT/LDT). This uses the **full segment protection**: limit checks per segment, read-only/execute-only segments, privilege levels and separate address spaces per task.

In all three models **paging** can be enabled underneath to map the linear addresses to physical memory and provide virtual memory.
