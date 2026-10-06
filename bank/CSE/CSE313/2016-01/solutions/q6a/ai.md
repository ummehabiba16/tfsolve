---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Linux is a UNIX-like (POSIX) system: same architecture (monolithic kernel, processes, files, devices as files), same system calls, shell, permissions, hierarchy; it is a re-implementation rather than UNIX code."
sources: ["Tanenbaum MOS 4e, sec. 10.1-10.2 (UNIX and Linux)"]
---
Linux is not derived from the AT&T UNIX source code (it was written from scratch by Linus Torvalds), but it **implements the UNIX interface and design** (POSIX / Single UNIX Specification), so it is an **example of a UNIX(-like) operating system**. Comparison:

| Feature | UNIX | Linux |
|:--|:--|:--|
| Kernel structure | monolithic kernel (file subsystem + process control subsystem), device drivers in the kernel | monolithic kernel (with loadable modules), same two subsystems |
| Process model | processes created by `fork`, programs loaded with `exec`, `wait`, signals, process states, `init` as ancestor | the same system calls and semantics (`clone` underlies `fork`/threads) |
| Files | everything is a file (devices as special files), hierarchical file system with `/`, inodes, links, permission bits rwx for owner/group/others, mount | the same: VFS with ext2/3/4 (inode-based, block groups), `/dev`, `/proc`, mount |
| User interface | shell (`sh`, `csh`, `bash`), pipes, redirection, filters (`grep`, `sort`) | bash and the same GNU tools; pipes and redirection |
| Standard | System V / BSD / POSIX | POSIX-compliant API (can run UNIX programs after recompilation) |
| Multi-user, multitasking | yes | yes |

So the statement is justified: the same design, system-call interface and tools, though they differ in origin and licence (UNIX proprietary, Linux GPL).
