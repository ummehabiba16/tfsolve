---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "E_SHELL: read a command, fork; the child execve()s it; the parent waitpid()s unless the command ends with &."
sources: ["Tanenbaum MOS 4e, sec. 1.6.2 (a stripped-down shell); OSTEP ch. 5"]
---
**Assumptions:** the command line is parsed into `name` and `argv[]` by a helper `read_command()`, which also reports whether the line ended with `&`; `environp` is the shell's own environment; the program is found by a full path name (a path search would be added by trying each directory of `PATH`).

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

extern char **environ;

/* parses a line into name and argv[]; sets *background if the last word is "&" */
int read_command(char *name, char *argv[], int *background);

int main(void) {
    char  name[256];
    char *argv[64];
    int   background, status;
    pid_t pid;

    while (1) {
        printf("E_SHELL> ");                         /* prompt */
        if (!read_command(name, argv, &background))  /* read a command */
            continue;

        pid = fork();                                /* create a child */
        if (pid < 0) {                               /* fork failed */
            perror("fork");
        } else if (pid == 0) {                       /* child */
            execve(name, argv, environ);             /* replace the core image */
            perror("execve");                        /* only if exec failed */
            exit(1);
        } else {                                     /* parent (the shell) */
            if (!background)
                waitpid(pid, &status, 0);            /* wait for the child to terminate */
            /* with '&': do not wait, ask for the next command at once */
        }
    }
}
```

With `&`, finished background children remain zombies until the shell collects them: a refinement is to call `waitpid(-1, &status, WNOHANG)` before each prompt.
