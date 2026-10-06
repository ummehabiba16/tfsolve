---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "fork() then execvp(hello) in the child; parent waitpid()s."
sources: ["OSTEP ch. 5 (Process API)"]
---
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void) {
    pid_t pid = fork();
    if (pid < 0) {                       // fork failed
        perror("fork");
        exit(1);
    } else if (pid == 0) {               // child
        char *args[] = { "hello", NULL };
        execvp("hello", args);           // replaces the child's image
        perror("execvp");                // reached only if exec fails
        exit(1);
    } else {                             // parent
        int status;
        waitpid(pid, &status, 0);        // wait for the child to finish
        printf("child %d is done\n", pid);
    }
    return 0;
}
```

`fork()` creates a copy of the parent; the child calls `exec` to load the program `hello` (with no arguments except `argv[0]`), and the parent blocks in `waitpid()` until the child terminates.
