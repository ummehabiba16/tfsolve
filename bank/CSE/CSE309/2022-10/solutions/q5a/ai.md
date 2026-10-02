---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Java uses a hybrid compiler: javac compiles source (.java) to platform-independent bytecode (.class); the Java Virtual Machine loads and verifies the bytecode and executes it by interpreting it, while a just-in-time (JIT) compiler translates frequently executed bytecode into native machine code. This gives portability (write once, run anywhere), safety checks and good speed."
sources: ["MMA introduction slides 4-13 (Language Processors, hybrid compiler)", "Dragon book 2e sec. 1.1 (Fig. 1.4)"]
---
Java uses a **hybrid compiler**: compilation followed by interpretation (Dragon book Fig. 1.4).

```text
 source program (.java)
        |
        v
   [ translator: javac ]
        |
        v
 intermediate program: bytecode (.class)
        |
        v
   [ virtual machine (JVM) ] <---- input
        |
        v
      output
```

**Working principle:**

1. **Compilation to bytecode.** The Java compiler `javac` performs lexical, syntax and semantic analysis (type checking) on the source, then translates it into **bytecode**: a compact, machine-independent intermediate language for a stack-based virtual machine. The bytecode is stored in `.class` files.
2. **Loading and verification.** On the target computer, the **Java Virtual Machine** loads the classes (class loader), possibly over a network, and the **bytecode verifier** checks that the bytecode is type-safe and well formed before it runs.
3. **Execution by interpretation.** The JVM **interprets** the bytecode: it executes each bytecode instruction in turn on the input.
4. **Just-in-time (JIT) compilation.** To achieve faster processing, the JVM's JIT compiler translates frequently executed bytecode (hot methods and loops) into the **native machine code** of the computer immediately before running it, and caches it.

**Consequences:**

- *Portability:* the same bytecode runs on any machine with a JVM ("write once, run anywhere").
- *Safety:* verification and run-time checks.
- *Speed:* JIT-compiled code approaches the speed of compiled code, while interpretation keeps start-up fast.
