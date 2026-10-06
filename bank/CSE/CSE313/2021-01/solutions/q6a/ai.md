---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A process is created at system initialisation, by a fork-like system call from a running process, by a user request, or by a batch job."
sources: ["Tanenbaum MOS 4e, sec. 2.1.2 (process creation)"]
---
1. **System initialisation:** when the OS boots, several processes are created: foreground processes that interact with users and background processes (**daemons**) for e-mail, printing, web pages, etc.
2. **Execution of a process-creation system call** (e.g. `fork`/`CreateProcess`) by a **running process**: a process creates one or more new processes to help it do its work.
3. **A user request** to create a new process: the user types a command or double-clicks an icon, and the shell/GUI creates the process.
4. **Initiation of a batch job:** on mainframe batch systems, when the system has the resources it takes the next job from the input queue and creates a process for it.
