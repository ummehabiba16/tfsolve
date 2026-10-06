---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Programmed I/O polls the printer status per character, interrupt-driven I/O sends a character per interrupt, DMA hands the whole string to the DMA controller and gets one interrupt at the end."
sources: ["Tanenbaum MOS 4e, sec. 5.2.2-5.2.4 (programmed I/O, interrupt-driven I/O, I/O using DMA)"]
---
Let the first name be the string `p` (e.g. `"Rahim"`) of `count` characters; `buffer` is a kernel buffer.

**i. Programmed I/O** (the CPU does everything and busy-waits):

```c
copy_from_user(buffer, p, count);            // copy the string into the kernel
for (i = 0; i < count; i++) {                // loop over the characters
    while (*printer_status_reg != READY)     // busy wait (polling)
        ;
    *printer_data_register = buffer[i];      // output one character
}
return_to_user();
```

**ii. Interrupt-driven I/O** (the CPU is free between characters):

```c
// code run when the print system call is made
copy_from_user(buffer, p, count);
enable_interrupts();
while (*printer_status_reg != READY) ;       // wait for the first character only
*printer_data_register = buffer[0];          // print the first character
scheduler();                                 // block the caller, run another process

// interrupt service procedure (printer is ready for the next character)
if (count == 0) {
    unblock_user();                          // all characters printed
} else {
    *printer_data_register = buffer[i];
    count--; i++;
}
acknowledge_interrupt();
return_from_interrupt();
```

**iii. I/O using DMA** (one interrupt for the whole string):

```c
// code run when the print system call is made
copy_from_user(buffer, p, count);
set_up_DMA_controller();                     // address of buffer, count, printer
scheduler();                                 // block the caller

// interrupt service procedure (the DMA transfer has finished)
acknowledge_interrupt();
unblock_user();
return_from_interrupt();
```

*Key features.* PIO: CPU busy-waits for every character. Interrupt-driven: one interrupt per character, CPU free in between. DMA: the DMA controller feeds the printer, one interrupt per transfer (best for large amounts of data, since interrupts are replaced by the cheap DMA transfers).
