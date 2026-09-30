---
author: ai
via: chat
status: unverified
summary: Push arguments, call the library wrapper, load the call number, execute TRAP to switch to kernel mode, the kernel dispatches to the handler, then returns to user mode.
sources: [Introduction slides 17-20, 'Tanenbaum, MOS 4e, sec. 1.6']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
Using $read(fd, buffer, nbytes)$ as the example:

1. The caller pushes the parameters (or loads them into registers).
2. It calls the C library wrapper for the call.
3. The wrapper places the system-call number in a register.
4. It executes a TRAP instruction, switching user$\to$kernel mode and jumping to a fixed kernel entry point.
5. The kernel uses the call number to index the system-call table and invoke the right handler.
6. The handler performs the requested service.
7. Control returns to the wrapper (back in user mode).
8. The wrapper returns to the caller, which cleans up the stack, like any ordinary procedure return.
