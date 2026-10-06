---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) boundaries and controlled crossing: referee; (ii) messages and shared memory: glue; (iii) virtual memory: illusionist."
sources: ["Anderson and Dahlin, OSPP, ch. 1 (the OS as referee, illusionist, glue)"]
---
**The three roles** (Anderson & Dahlin):

- **Referee:** manages the resources shared by applications and users: protects them from each other, and allocates the resources fairly.
- **Illusionist:** hides the details and limitations of the hardware, giving each application the *illusion* of its own machine with abundant (virtual) resources.
- **Glue:** provides common services and a standard interface so that applications can work together and with the hardware (windowing, file systems, communication).

| Task | Role | Why |
|:--|:--|:--|
| (i) sets up boundaries that prevent bugs and malicious users from affecting others, but lets the boundaries be crossed in carefully controlled ways | **Referee** | isolation, protection and controlled sharing between applications |
| (ii) standard way for applications to pass messages and to share memory | **Glue** | common services (IPC) that let programs communicate and cooperate |
| (iii) virtual memory that compensates for a shortage of physical memory by moving pages to disk | **Illusionist** | gives each program the illusion of a large private memory |
