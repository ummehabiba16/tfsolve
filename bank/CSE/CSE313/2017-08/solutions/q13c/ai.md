---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Page sharing: the page-table entries of several processes point to the same physical frame (read-only code, shared libraries, copy-on-write data), with per-process protection bits."
sources: ["Tanenbaum MOS 4e, sec. 3.5.3 (shared pages)"]
---
**Sharing pages through the MMU.** The page tables of the sharing processes simply have **entries that point to the same physical page frame**. The MMU translates each process's virtual page number through its own page table, so each process may map the shared frame at a **different virtual address** (or the same one).

- **Code (text) and shared libraries:** the program text is **read-only**, so several processes running the same program map the same frames (marked read-only); only one copy is in memory.
- **Data pages:** sharing writable data needs care: pages are shared **copy-on-write**: both mappings are read-only; when a process writes, a protection fault occurs and the OS gives it its own **private copy** of the page (used by `fork`). Truly shared memory (IPC) maps the same writable frame in all processes.
- **Protection:** each page-table entry has its own protection bits per process, so one process may have read/write access and another read-only.
- **Bookkeeping:** the OS keeps a **reference count** per shared frame; the frame is freed when the last mapping is removed, and a shared page cannot be removed from memory without updating all page tables mapping it.
