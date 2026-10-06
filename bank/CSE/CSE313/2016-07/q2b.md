---
marks: 16
topics: [kernel-vs-user-mode, syscall-steps]
kind: conceptual
source: {page: 45-46}
---
Operating systems implement "dual-mode operation, represented by a single bit in the processor status register that signifies the current mode of the processor. In user mode, the processor checks each instruction before executing it to verify that it is permitted to be performed by that process. In kernel mode, the operating system executes with protection checks turned off." However, there is also another need of "safely transition from executing a user process to execute the kernel, and vice versa." These two transitions are known as "User to Kernel Mode Transfer" and "Kernel to User Mode Transfer" respectively. A special type of kernel to user mode transfer is "Upcall". From the following scenarios you need to identify the examples of user to kernel mode transfer, kernel to user mode transfer, and upcalls.

i. **Resume after an interrupt**: When handling the request is finished, "the execution of the interrupted process is resumed by restoring its program counter."

ii. **Processor Exception**: "A processor exception is a hardware event caused by user program behavior after which the hardware finishes all previous instructions, saves the current execution state, and starts running at a specially designated exception handler."

iii. **New process**: To start a new process, its program is copied into memory, the program counter is set to the first instruction, the stack pointer is set to the top of the stack, and then the process is started.

iv. **Resource allocation**: "Operating systems allocate resources - deciding which users and processes should get how much CPU time, how much memory, and so forth. In turn, many applications are resource adaptive - able to optimize their behavior to differing amounts of CPU time or memory. An example is Java garbage collection. Within limits, a Java process can adapt to different amounts of available memory by changing the frequency with which it runs its garbage collector. The more memory, the less time Java needs to run its collector, speeding execution. For this, the operating system must inform the process when its allocation changes, e. g., because some other processes need more or less memory."
