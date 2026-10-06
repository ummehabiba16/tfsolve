---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "RPC: calling a procedure on another machine through stubs; scheduler activations: the kernel makes upcalls to the user-level thread package when events occur; the FSM model: a single thread with non-blocking system calls and saved state."
sources: ["Tanenbaum MOS 4e, sec. 8.2.4 (RPC), 2.2.6-2.2.8 (scheduler activations, single-threaded servers)"]
---
**(i) Remote Procedure Call (RPC).** A mechanism that lets a process call a procedure that executes on **another machine** as if it were a local call. The caller's *client stub* **marshals** the parameters into a message, the message is sent over the network, the *server stub* **unmarshals** them, calls the real procedure and sends back the **result**, which the client stub returns to the caller. Hides the network, byte-order and message passing from the programmer; must handle lost messages (timeouts), server crashes and binding (finding the server).

**(ii) Upcall in scheduler activations.** A scheme (Anderson et al.) to combine the performance of user threads with the correctness of kernel threads: the kernel gives each process **virtual processors (activations)** and, whenever an event of interest happens (a user thread blocks in the kernel, an I/O completes, a processor is allocated or taken away), the **kernel calls up into the user-level run-time system** (an **upcall**, a call from the lower layer to the higher one). The run-time then decides which user thread to run on the activation, so a blocking call does not block the whole process and the kernel need not know about the user threads' details.

**(iii) System-call implementation in the finite-state-machine (FSM) thread model.** A server built as **one thread** that uses **non-blocking system calls** (e.g. a non-blocking `read`, `select`/`poll`, or signals/interrupts): when a request needs I/O, the thread **records the state of that request in a table**, starts a non-blocking (asynchronous) disk read and goes on to the next request or event; when the I/O completion arrives (interrupt/signal), the thread looks up the saved state and **continues the request from where it stopped**. It gives concurrency without threads, but the "sequential process" model is lost: the program is a state machine whose state must be saved and restored explicitly, and the system calls have to be non-blocking (asynchronous).
