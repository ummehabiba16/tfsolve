---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "GNU/Linux = the Linux kernel plus the GNU system software (compiler, shell, libraries, utilities); a distribution packages these with installer, package manager and applications."
sources: ["Tanenbaum MOS 4e, sec. 10.1 (history of UNIX and Linux)"]
---
**(i) GNU/Linux OS.** **Linux** is only the *kernel* (written by Linus Torvalds from 1991, released under the GPL). A usable operating system also needs a C library, compiler, shell, editors and utilities; most of these come from the **GNU project** (started by Richard Stallman in 1983: `gcc`, `glibc`, `bash`, `coreutils`, ...). The complete system, the Linux kernel plus the GNU tools and libraries, is called **GNU/Linux**. It is a free, open-source, UNIX-like (POSIX-compatible) system running on everything from phones to supercomputers.

**(ii) Linux distributions.** A **distribution** is a packaged, ready-to-install collection of the Linux kernel, the GNU and other system software, a **package manager** (apt, rpm), an installer, a desktop environment and applications, plus configuration defaults and support. Examples: Debian, Ubuntu, Fedora, Red Hat Enterprise Linux, SUSE, Arch. Distributions differ in their package format, release policy, target use (server, desktop, embedded) and support, but share the same kernel.
