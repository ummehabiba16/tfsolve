---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Search-Insert-Delete with lightswitches: searchers and inserters each form a group that locks out deleters; inserters also exclude each other; a deleter takes both locks."
sources: ["Downey, The Little Book of Semaphores, sec. 6.3 (search-insert-delete)"]
---
**Requirements.** Searchers can run together; inserters exclude each other but can run with searchers; a deleter excludes everybody.

Use the **lightswitch** pattern: the first process of a group locks a semaphore on behalf of the group and the last one unlocks it.

```c
struct lightswitch { int counter = 0; semaphore mutex = 1; };

void ls_lock(lightswitch *ls, semaphore *sem) {      /* first in locks sem */
    down(&ls->mutex);
    if (++ls->counter == 1) down(sem);
    up(&ls->mutex);
}
void ls_unlock(lightswitch *ls, semaphore *sem) {    /* last out unlocks sem */
    down(&ls->mutex);
    if (--ls->counter == 0) up(sem);
    up(&ls->mutex);
}

semaphore noSearcher = 1;      /* held while searchers are active or a deleter works */
semaphore noInserter = 1;      /* held while inserters are active or a deleter works */
semaphore insertMutex = 1;     /* inserters mutually exclusive */
lightswitch searchSwitch, insertSwitch;

void searcher(void) {
    ls_lock(&searchSwitch, &noSearcher);      /* searchers share; deleter is locked out */
    /* search the list */
    ls_unlock(&searchSwitch, &noSearcher);
}

void inserter(void) {
    ls_lock(&insertSwitch, &noInserter);      /* inserters as a group lock out deleters */
    down(&insertMutex);                       /* only one inserter at a time */
    /* insert at the end of the list */
    up(&insertMutex);
    ls_unlock(&insertSwitch, &noInserter);
}

void deleter(void) {
    down(&noSearcher);                        /* wait until no searcher is active */
    down(&noInserter);                        /* and no inserter is active */
    /* delete an item */
    up(&noInserter);
    up(&noSearcher);
}
```

A searcher and an inserter can be active at the same time (they hold different semaphores); searchers do not exclude each other (one lightswitch); inserters exclude each other through `insertMutex`; a deleter obtains both `noSearcher` and `noInserter`, which can only happen when no searcher and no inserter is active, and holds them during the deletion.
