---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Scan the 8x8 matrix column by column through the board's 8255: select column i (one-hot), put arr[i] on the green (or red) row port, wait about 2.5 ms; 8 columns = one 20 ms frame; repeat 100 frames = 2 s in green, then 100 frames in red, forever. Port addresses and polarities of the MDA-8086 are taken as assumptions."
sources: ["MDA-8086 user's manual (dot-matrix LED via 8255 PPI)", "Hall, Microprocessors and Interfacing, Ch. 9 (multiplexed LED displays, 8255 mode 0 output)"]
---
**Idea.** An 8 $\times$ 8 matrix cannot show all 64 LEDs at once; it is **scanned**: one column is switched on at a time with its 8 row bits, and the columns are repeated fast enough (about 50 frames/s) that the eye sees the whole pattern. Showing a colour for 2 s means repeating the scan for 2 s.

**Assumptions** (board wiring of the MDA-8086 dot-matrix LED; adjust the constants to the kit's manual):

- The matrix is driven by an 8255 at ports **19H (A), 1BH (B), 1DH (C), 1FH (control)**, all in mode 0 output (control word 80H).
- Port A = **green** row data, Port B = **red** row data, Port C = **column select** (one bit per column, bit 0 = leftmost column). All active high; bit $k$ of a row port drives row $k$ counted from the bottom, which matches "LSB = bottom LED" of `arr[]`.
- CPU clock 4.9152 MHz; `DELAY` below waits about 2.5 ms.

**Program (8086 assembly)**

```text
PPI_A   EQU 19H        ; green rows
PPI_B   EQU 1BH        ; red rows
PPI_C   EQU 1DH        ; column select
PPI_CW  EQU 1FH        ; control register

        ORG  1000H
        MOV  AL, 80H           ; mode 0, ports A, B, C all output
        OUT  PPI_CW, AL

FOREVER:
        MOV  BL, 0             ; 0 = green
        CALL SHOW_2S
        MOV  BL, 1             ; 1 = red
        CALL SHOW_2S
        JMP  FOREVER

; show arr[] for 2 s in the colour given by BL
SHOW_2S:
        MOV  CX, 100           ; 100 frames x 20 ms = 2 s
FRAME:  PUSH CX
        LEA  SI, ARR           ; arr[0] = leftmost column
        MOV  AH, 01H           ; column 0 selected
        MOV  CX, 8
COLUMN: MOV  AL, 0             ; blank both colours (no ghosting)
        OUT  PPI_A, AL
        OUT  PPI_B, AL
        MOV  AL, AH
        OUT  PPI_C, AL         ; select this column
        MOV  AL, [SI]          ; 8 row bits of this column
        CMP  BL, 0
        JNE  RED
        OUT  PPI_A, AL         ; green
        JMP  SHOWN
RED:    OUT  PPI_B, AL         ; red
SHOWN:  CALL DELAY             ; keep the column on ~2.5 ms
        INC  SI                ; next column data
        SHL  AH, 1             ; next column select
        LOOP COLUMN
        POP  CX
        LOOP FRAME
        RET

DELAY:  PUSH CX                ; ~2.5 ms at 4.9152 MHz
        MOV  CX, 680           ; 680 x (DEC + JNZ = 2 + 16 clocks) ~ 12240 clocks
D1:     DEC  CX
        JNZ  D1
        POP  CX
        RET

ARR     DB   8 DUP(?)          ; the given char arr[8]
```

**Timing check:** one column $\approx$ 2.5 ms, one frame $= 8 \times 2.5 = 20$ ms (50 Hz, no flicker), 100 frames $=$ 2 s per colour.

*Note:* if the board's columns or rows are active low, complement the values (`NOT AL`) before the `OUT` instructions.
