---
marks: 8
topics: [fork-process-tree, syscall-steps]
kind: code
source: {page: 63}
---
Consider a simple command interpreter, called E_SHELL (like Linux shell) which serves user commands using operating system features. When started, E_SHELL asks for one command from the user. When the user types a command and press enter E_SHELL waits for the command to complete and then asks for the next command. If the user puts an ampersand (&) after a command, E_SHELL does not wait for it to complete. Instead it just asks for the next command immediately. Now write a code in C language for E_SHELL using the system calls shown in the following Figure. Make necessary assumptions and mention those assumptions.

| Call | Description |
|:--|:--|
| `pid = fork()` | Create a child process identical to the parent |
| `pid = waitpid(pid, &statloc, options)` | Wait for a child to terminate |
| `s = execve(name, argv, environp)` | Replace a process' core image |
| `exit(status)` | Terminate process execution and return status |

*Figure for Questions 8(b)*
