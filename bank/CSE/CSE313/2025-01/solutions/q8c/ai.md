---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import): diagram redrawn as text; the one-line formula ran off the page."
---
A **Remote Procedure Call (RPC)** lets a program invoke a procedure that actually executes on a *different* machine across a network, while looking to the calling code just like an ordinary local function call -- the networking details are hidden behind the abstraction.

**How it works:**

1.  The client calls a local **client stub** with the same signature as the remote procedure.

2.  The client stub **marshals** (serializes) the arguments into a message and sends it over the network to the server.

3.  A **server stub** receives the message, **unmarshals** the arguments, and calls the real procedure implementation locally on the server.

4.  The result is marshaled by the server stub and sent back over the network.

5.  The client stub unmarshals the result and returns it to the calling code, exactly as if a local call had just returned.

**Diagram:**

```text
 client machine                               server machine
 --------------                               --------------
 client code
     | call f(args)
 client stub --- marshal args ---> network ---> server stub
                                                   | unmarshal, call
                                                procedure f
                                                   | return result
 client stub <--- network <--- marshal result --- server stub
     | unmarshal
 client code (the call returns)
```

Unlike a true local call, RPC must additionally cope with things that cannot happen locally: network failures/timeouts (the server, or the reply, may simply never arrive), the overhead of marshaling and network latency compared to a plain function call, and the fact that raw pointers/complex data structures cannot simply be passed across machines -- the data they reference must be serialized too.
