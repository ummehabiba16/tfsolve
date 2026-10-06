---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Example: the C library functions fread/fgets/printf wrap read/write and add buffering, so many small requests become few system calls; malloc wraps brk/sbrk."
sources: ["Tanenbaum MOS 4e, sec. 1.6 (system calls, libraries); OSTEP ch. 5"]
---
**Example 1: the standard I/O library (`stdio`).** The system call `read(fd, buf, n)` transfers data directly, and each call costs a trap into the kernel. The library function `fgetc`/`fgets`/`fread` **wraps** it and adds **user-level buffering**: the first call reads a whole block (e.g. 4 KB) into a buffer in the process with one `read`, and the following calls are served from that buffer without entering the kernel. `printf`/`fwrite` similarly collect output in a buffer and call `write` only when the buffer is full or on a newline/flush; `fopen` adds formatted access and a `FILE` structure.

```c
// without the library: one system call per byte
char c;
while (read(fd, &c, 1) == 1) process(c);

// with the library: one system call per 4 KB, the rest are function calls
int c;
while ((c = fgetc(fp)) != EOF) process(c);
```

**Example 2: `malloc`/`free`** wrap the system call `brk`/`sbrk` (or `mmap`): the library asks the kernel for big chunks of memory and manages free lists in user space to serve small allocations quickly and with finer granularity, which the system call alone cannot do.

These wrappers add **functionality (buffering, formatting, memory management) and efficiency, and portability** on top of the minimal kernel interface.
